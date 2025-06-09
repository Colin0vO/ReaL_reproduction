#!/usr/bin/env python3
import os
import json
import argparse
from glob import glob

def make_entry(path):
    """
    Read a .py file and return a dict with
    'problem_id' = full filename (sans extension),
    and 'response' wrapped in a ```python block.
    """
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read().rstrip()

    # Derive problem_id = full filename without extension
    fname = os.path.splitext(os.path.basename(path))[0]
    pid = fname

    response = f"```python\n{code}\n```"

    return {
        "problem_id": pid,
        "response": response
    }

def main(scripts_dir, out_json):
    py_files = sorted(glob(os.path.join(scripts_dir, "*.py")))

    entries = [make_entry(p) for p in py_files]
    # (Optional) sort by problem_id again
    entries.sort(key=lambda e: e["problem_id"])

    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    print(f"Converted {len(entries)} scripts → {out_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a folder of .py scripts into a JSON array of {problem_id,response} entries"
    )
    parser.add_argument(
        "scripts_dir",
        help="path to folder containing generated_scripts/*.py"
    )
    parser.add_argument(
        "--out", "-o",
        default="scp_sft_7b_responses.json",
        help="output JSON file (default: scp_sft_7b_responses.json)"
    )
    args = parser.parse_args()
    main(args.scripts_dir, args.out)
