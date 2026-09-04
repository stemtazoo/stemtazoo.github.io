#!/usr/bin/env python3
from pathlib import Path

path = Path("pages/ds/index.md")
text = path.read_text(encoding="utf-8-sig")

old_intro = "現行の試験範囲では、従来のビジネス力の多くが基盤へ移っています。まずは、既存記事のうち基盤と重なる「データ理解」「ITセキュリティ」を確認できます。"
new_intro = "現行の試験範囲では、従来のビジネス力の多くが基盤へ移っています。論理的思考、課題の定義、目標・指標、データ理解、ITセキュリティの順に整理します。"
text = text.replace(old_intro, new_intro)

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

path.write_text(text, encoding="utf-8")
print("Updated pages/ds/index.md for DS ver.6 foundation sections.")
