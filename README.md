# fruity-soup-web-monitoring-agent

Local-first agent that watches web pages, extracts values (e.g., price/stock), compares with last run, and generates a clean HTML report.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python agent.py data/targets.json
open reports/monitor_report.html
```
