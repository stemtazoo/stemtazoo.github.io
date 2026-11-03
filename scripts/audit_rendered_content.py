#!/usr/bin/env python3
"""Report suspicious rendered study-article text; candidates never block deployment."""
import argparse
import json
import re
from time import perf_counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

THEMES = ('fe', 'gk', 'ds', 'sg')
SKIP = {'pre', 'code', 'script', 'style', 'template'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
        'link', 'meta', 'param', 'source', 'track', 'wbr'}
BLOCK = {'p', 'div', 'section', 'article', 'main', 'li', 'tr', 'td', 'th',
         'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'hr', 'dt', 'dd'}
META = re.compile(r'(?<![\w-])(?:layout|title|description|permalink|tags|date|'
                  r'last_modified_at|(?:fe|gk|ds|sg)_(?:section|subsection|order))\s*:')
# Match escape tokens, not the prefixes of TeX commands such as \rho/\right.
NEWLINE = re.compile(r'\\r\\n(?![A-Za-z])|\\[nr](?![A-Za-z])')
LIQUID = re.compile(r'\{\{[^\n]*?\}\}|\{%[^\n]*?%\}')
TAG = re.compile(r'<!doctype\s+html[^>]*>|</?(?:div|span|p|br|table|tr|td|th|script|style|section|h[1-6])\b[^>]*>', re.I)
TRUNCATION = re.compile(r'\b\d+\s+(?:tokens?|characters?|lines?)\s+truncated\b', re.I)
# Horizontal whitespace only: \s also matches newlines and repeatedly revisits
# long blank regions. A Markdown table row must stay on one line.
RAW_TABLE = re.compile(r'^[^\S\n]*\|[^\n|]+\|[^\n|]+\|[^\S\n]*$', re.M)


class TextRegions(HTMLParser):
    """Extract text, preferring article content over main/body fallback regions.

    Inline elements preserve text adjacency; block boundaries prevent invented tokens.
    This is an HTML text audit, not a CSS visibility or browser layout engine.
    """
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.parts = {x: [] for x in ('article', 'main', 'body')}
        self.seen = set()
        self.canonical = None
        self.refresh_target = None

    def emit(self, text):
        if any(skip for _, _, skip in self.stack):
            return
        active = {region for _, region, _ in self.stack if region}
        for region in active:
            self.parts[region].append(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and 'canonical' in attrs.get('rel', '').lower().split():
            self.canonical = attrs.get('href')
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            match = re.fullmatch(r'\s*\d+(?:\.\d+)?\s*;\s*url\s*=\s*(.+?)\s*',
                                 attrs.get('content', ''), re.I)
            if match:
                self.refresh_target = match.group(1).strip('\'"')
        classes = attrs.get('class', '').split()
        region = ('article' if 'data-pagefind-body' in attrs or 'post-content' in classes
                  else tag if tag in ('main', 'body') else None)
        skip = tag in SKIP or 'hidden' in attrs or attrs.get('aria-hidden') == 'true'
        if tag in BLOCK:
            self.emit('\n')
        if tag not in VOID:
            self.stack.append((tag, region, skip))
            if region:
                self.seen.add(region)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in BLOCK or tag in SKIP:
            self.emit('\n')
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break
        if tag in SKIP:
            self.emit('\n')

    def handle_data(self, data):
        self.emit(data)

    def text(self):
        for region in ('article', 'main', 'body'):
            if region in self.seen:
                return ''.join(self.parts[region]), region
        return '', None

    def is_redirect(self):
        """Recognize Jekyll's body-less redirect; do not certify its destination."""
        if not self.canonical or not self.refresh_target:
            return False
        target = urlsplit(self.canonical)
        return (target.scheme in ('http', 'https') and bool(target.netloc)
                and urljoin(self.canonical, self.refresh_target) == self.canonical)



class HeadingStructure(HTMLParser):
    """Read actual H1 elements and the document title from generated HTML."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.headings = []
        self.h1_parts = None
        self.title_parts = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self.h1_parts = []
        elif tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == 'h1' and self.h1_parts is not None:
            self.headings.append(' '.join(''.join(self.h1_parts).split()))
            self.h1_parts = None
        elif tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.h1_parts is not None:
            self.h1_parts.append(data)
        if self.in_title:
            self.title_parts.append(data)


def inspect_headings(html, redirect=False):
    """Report absent/multiple H1 and H1-title disagreement, except redirects."""
    if redirect:
        return []
    parser = HeadingStructure()
    parser.feed(html)
    headings = parser.headings
    if not headings:
        return [{'code': 'missing_h1', 'excerpt': 'No H1 in rendered page.'}]
    if len(headings) > 1:
        return [{'code': 'multiple_h1', 'excerpt': f'{len(headings)} H1 tags: {headings[:3]!r}'}]
    title = ' '.join(''.join(parser.title_parts).split())
    if title and headings[0] and headings[0] not in title:
        return [{'code': 'h1_title_mismatch',
                 'excerpt': f'H1={headings[0]!r}; title={title!r}'}]
    return []


def inspect_html(html):
    parser = TextRegions()
    parser.feed(html)
    text, region = parser.text()
    redirect = parser.is_redirect()
    if region is None:
        if redirect:
            return []
        return [{'code': 'missing_content_region', 'excerpt': 'No article/main/body region; inspect HTML.'}]
    findings = []
    for code, pattern in (('literal_newline', NEWLINE), ('unresolved_liquid', LIQUID),
                          ('escaped_html_tag', TAG), ('truncation_marker', TRUNCATION),
                          ('unrendered_markdown_table', RAW_TABLE)):
        match = pattern.search(text)
        if match:
            findings.append({'code': code, 'excerpt': text[max(0, match.start()-45):match.end()+90].strip()})
    # Multiple metadata keys near the opening suggest a leaked header. A lone
    # ordinary "title:" in a programming explanation is insufficient evidence.
    opening = text[:2000]
    keys = list(META.finditer(opening))
    if len({m.group().strip() for m in keys}) >= 2:
        findings.append({'code': 'frontmatter_leak', 'excerpt': opening[max(0, keys[0].start()-20):keys[-1].end()+80].strip()})
    return findings


def scan(site):
    started = perf_counter()
    files = set()
    for theme in THEMES:
        for directory in (site / theme, site / 'pages' / theme):
            files.update(directory.rglob('*.html'))
    if not files:
        raise ValueError('No rendered study HTML found; check --site/build output')
    findings = []
    timings = []
    total = len(files)
    print(f'Rendered text audit: starting {total} pages.', flush=True)
    for index, path in enumerate(sorted(files), 1):
        relative = path.relative_to(site).as_posix()
        if index == 1 or (index - 1) % 100 == 0:
            print(f'Scanning {index}/{total}: {relative} '
                  f'(elapsed {perf_counter() - started:.2f}s)', flush=True)
        page_started = perf_counter()
        html = path.read_text(encoding='utf-8')
        redirect_parser = TextRegions()
        redirect_parser.feed(html)
        page_findings = inspect_html(html)
        page_findings.extend(inspect_headings(html, redirect=redirect_parser.is_redirect()))
        for item in page_findings:
            findings.append({'path': relative, **item})
        seconds = perf_counter() - page_started
        timings.append({'path': relative, 'seconds': seconds})
        if seconds >= 1:
            print(f'Slow page: {relative} took {seconds:.2f}s', flush=True)
    elapsed = perf_counter() - started
    slowest = sorted(timings, key=lambda item: item['seconds'], reverse=True)[:5]
    print(f'Rendered text audit: completed {total}/{total} pages in {elapsed:.2f}s.',
          flush=True)
    for item in slowest:
        print(f"Slowest pages: {item['path']} ({item['seconds']:.3f}s)", flush=True)
    return {'scanned_pages': total, 'findings': findings,
            'elapsed_seconds': elapsed, 'slowest_pages': slowest,
            'limits': 'Text candidates only; excludes code/pre/script/style/template and explicit hidden regions. '
                      'Does not verify CSS layout, JavaScript, or all rendering defects. Review candidates before editing.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('_site'))
    parser.add_argument('--report', type=Path, default=Path('artifacts/rendered-content-audit.json'))
    args = parser.parse_args()
    result = scan(args.site)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Scanned {result['scanned_pages']} pages; {len(result['findings'])} review candidates. Report: {args.report}")
    # Keep reports out of published _site. Warnings are review cues, not failures.
    for item in result['findings'][:50]:
        message = f"{item['path']}: {item['code']}: {item['excerpt']}"
        message = message.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
        print('::warning::' + message)


if __name__ == '__main__':
    main()
