from pathlib import Path
from jinja2 import Template
from datetime import datetime

TEMPLATE = """
<!doctype html>
<html><head><meta charset='utf-8'>
<title>Fruity Soup — Web Monitor Report</title>
<style>
body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial; margin:20px; color:#111; }
h1 { margin: 0 0 8px 0; }
.muted { color:#6b7280; }
.table { width:100%; border-collapse: collapse; margin-top: 10px; }
.table th, .table td { border-bottom:1px solid #eee; padding:8px; text-align:left; font-size:14px; vertical-align:top; }
.badge { display:inline-block; padding:.2rem .5rem; border-radius:999px; font-size:12px; border:1px solid #e5e7eb; }
.badge.changed { background:#fff7ed; border-color:#fdba74; color:#9a3412; }
.badge.ok { background:#f0fdf4; border-color:#86efac; color:#166534; }
code { background:#f3f4f6; padding:2px 4px; border-radius:4px; }
</style></head><body>
<h1>Fruity Soup — Web Monitor</h1>
<div class='muted'>Generated: {{generated}}</div>
<table class='table'>
<thead><tr><th>Item</th><th>Source</th><th>Selector</th><th>Previous</th><th>Current</th><th>Status</th></tr></thead>
<tbody>
{% for r in results %}
<tr>
  <td>{{r.label}}</td>
  <td><code>{{r.source}}</code></td>
  <td><code>{{r.selector}}</code></td>
  <td>{{r.old or '—'}}</td>
  <td>{{r.new or '—'}}</td>
  <td>
    {% if r.changed %}
      <span class='badge changed'>Changed</span> <span class='muted'>{{r.change_str}}</span>
    {% else %}
      <span class='badge ok'>No change</span>
    {% endif %}
  </td>
</tr>
{% endfor %}
</tbody>
</table>
<div class='muted' style='margin-top:12px;'>Local-first: snapshots saved under <code>data/snapshots/</code>.</div>
</body></html>
"""

def render_report(results, out_dir: Path):
    html = Template(TEMPLATE).render(results=results, generated=datetime.now().strftime('%Y-%m-%d %H:%M'))
    path = out_dir/'monitor_report.html'
    path.write_text(html, encoding='utf-8')
    return path
