#!/usr/bin/env python3
from pathlib import Path

path = Path("pages/ds/index.md")
text = path.read_text(encoding="utf-8-sig")

old_intro = "現行の試験範囲では、従来のビジネス力の多くが基盤へ移っています。論理的思考、課題の定義、目標・指標、データ理解、ITセキュリティの順に整理します。"
new_intro = "現行の試験範囲では、従来のビジネス力の多くが基盤へ移っています。行動規範・倫理、論理的思考、課題の定義、目標・指標、データ理解、AIの基礎、ITセキュリティの順に整理します。"
text = text.replace(old_intro, new_intro)

old_status = "> **ver.5 からの大きな変更**：従来の「ビジネス力」の多くは「基盤」へ移り、「価値創造」が新しい試験領域として加わりました。サイト内の既存記事は順次 ver.6 の分類へ整理します。"
new_status = "> **ver.5 からの大きな変更**：従来の「ビジネス力」の多くは「基盤」へ移り、「価値創造」が新しい試験領域として加わりました。通常記事の4領域への分類は完了しており、現在は旧スキルチェックページの ver.6 対応を進めています。"
text = text.replace(old_status, new_status)

# Foundation: action norms / ethics
logical_marker = "### 論理的思考\n"
action_norms = '''### 行動規範・倫理・権利
<ul>
{% for p in site.pages %}
  {% if p.ds_area == "foundation" and p.ds_section == "action-norms" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

'''
if "### 行動規範・倫理・権利\n" not in text:
    if logical_marker not in text:
        raise SystemExit("logical-thinking marker not found")
    text = text.replace(logical_marker, action_norms + logical_marker, 1)

# Existing foundation sections kept idempotently for older index states.
marker = "### データ理解・検証\n"
foundation_sections = '''### 論理的思考
<ul>
{% for p in site.pages %}
  {% if p.ds_area == "foundation" and p.ds_section == "logical-thinking" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 課題の定義・仮説
<ul>
{% for p in site.pages %}
  {% if p.ds_area == "foundation" and p.ds_section == "problem-definition" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 目標・指標
<ul>
{% for p in site.pages %}
  {% if p.ds_area == "foundation" and p.ds_section == "goal-setting" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

'''
if "### 論理的思考\n" not in text:
    if marker not in text:
        raise SystemExit("foundation insertion marker not found")
    text = text.replace(marker, foundation_sections + marker, 1)

# Foundation: AI fundamentals, inserted before security.
security_marker = "### ITセキュリティ\n"
ai_fundamentals = '''### AI・生成AIの基礎
<ul>
{% for p in site.pages %}
  {% if p.ds_area == "foundation" and p.ds_section == "ai-fundamentals" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

'''
if "### AI・生成AIの基礎\n" not in text:
    if security_marker not in text:
        raise SystemExit("foundation security marker not found")
    text = text.replace(security_marker, ai_fundamentals + security_marker, 1)

old_ds_data_understanding = '''### データの理解・検証
<ul>
{% for p in site.pages %}
  {% if p.tags contains "data-understanding" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
'''
new_ds_data_understanding = '''### データの理解・検証
<ul>
{% for p in site.pages %}
  {% if p.url contains "/ds/" %}
    {% if p.ds_area %}
      {% if p.ds_area == "datascience" and p.ds_section == "data-understanding" %}
        <li><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% endif %}
    {% elsif p.tags contains "data-understanding" %}
      <li><a href="{{ p.url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>
'''
if old_ds_data_understanding in text:
    text = text.replace(old_ds_data_understanding, new_ds_data_understanding, 1)
elif 'p.ds_area == "datascience" and p.ds_section == "data-understanding"' not in text:
    raise SystemExit("data-understanding block not found")

# Data engineering: programming articles were individually reviewed and should
# have a visible home rather than only being considered 'shown' internally.
de_security_marker = "### 🗄 ITセキュリティ\n"
programming = '''### プログラミング基礎
<ul>
{% for p in site.pages %}
  {% if p.ds_area == "dataengineering" and p.ds_section == "programming" and p.url contains "/ds/" %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

'''
if "### プログラミング基礎\n" not in text:
    if de_security_marker not in text:
        raise SystemExit("data-engineering security marker not found")
    text = text.replace(de_security_marker, programming + de_security_marker, 1)

path.write_text(text, encoding="utf-8")
print("Updated pages/ds/index.md for complete DS ver.6 section visibility.")
