import requests
from pathlib import Path

def fetch_content(source: str) -> str:
    if source.startswith('http://') or source.startswith('https://'):
        r = requests.get(source, timeout=15)
        r.raise_for_status()
        return r.text
    return Path(source).read_text(encoding='utf-8')
