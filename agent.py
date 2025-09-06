#!/usr/bin/env python3
import sys, json
from pathlib import Path
from utils.loader import fetch_content
from utils.extract import extract_text
from utils.diff import compare_values
from utils.report import render_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py data/targets.json")
        sys.exit(1)
    cfg_path = Path(sys.argv[1])
    if not cfg_path.exists():
        print(f"🍲 Sorry, Fruity Soup couldn’t find your input: {cfg_path}")
        sys.exit(1)
    targets = json.loads(cfg_path.read_text(encoding='utf-8'))

    out_dir = Path('reports'); out_dir.mkdir(exist_ok=True)
    snap_dir = Path('data/snapshots'); snap_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for t in targets:
        tid, src, selector = t['id'], t['source'], t['selector']
        label = t.get('label', tid)
        html = fetch_content(src)
        value = extract_text(html, selector)
        snap_file = snap_dir / f"{tid}.txt"
        old_value = snap_file.read_text(encoding='utf-8') if snap_file.exists() else None
        changed, change_str = compare_values(old_value, value)
        snap_file.write_text(value or '', encoding='utf-8')
        results.append({'id':tid,'label':label,'source':src,'selector':selector,'old':old_value,'new':value,'changed':changed,'change_str':change_str})
    report_path = render_report(results, out_dir)
    changed_count = sum(1 for r in results if r['changed'])
    print(f"👀 Your Dish is ready! {changed_count} change(s). Your fresh monitor report is served: {report_path}")

if __name__ == '__main__':
    main()

    # Created By Jevante Boxley
    # All Rights Reserved : Fruity Soup
