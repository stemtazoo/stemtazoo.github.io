#!/usr/bin/env python3
"""Report suspicious rendered study-article text; candidates never block deployment."""
import argparse
import json
import re
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


def inspect_html(html):
    parser = TextRegions()
    parser.feed(html)
    text, region = parser.text()
    if region is None:
        if parser.is_redirect():
            return []
        return [{'code': 'missing_content_region', 'excerpt': 'No article/main/body region; inspect HTML.'}]
    findings = []
    for code, pattern in (('literal_newline', NEWLINE), ('unresolved_liquid', LIQUID),
                          ('escaped_html_tag', TAG)):
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
    files = set()
    for theme in THEMES:
        for directory in (site / theme, site / 'pages' / theme):
            files.update(directory.rglob('*.html'))
    if not files:
        raise ValueError('No rendered study HTML found; check --site/build output')
    findings = []
    for path in sorted(files):
        for item in inspect_html(path.read_text(encoding='utf-8')):
            findings.append({'path': path.relative_to(site).as_posix(), **item})
    return {'scanned_pages': len(files), 'findings': findings,
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
