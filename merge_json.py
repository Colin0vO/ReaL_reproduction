#!/usr/bin/env python3
import json
from pathlib import Path

def merge_prompt_response(prompts_path: str, responses_path: str, out_path: str):
    prompts = json.loads(Path(prompts_path).read_text(encoding="utf-8"))
    responses = json.loads(Path(responses_path).read_text(encoding="utf-8"))

    # Build map from int ID → code
    resp_map = {}
    for r in responses:
        pid = r["problem_id"]
        if isinstance(pid, str) and pid.startswith("script_"):
            idx = int(pid.split("_", 1)[1])
        elif isinstance(pid, int):
            idx = pid
        else:
            continue
        code = r["response"].strip()
        if code.startswith("```"):
            # strip code fences
            code = code.split("\n", 1)[1].rsplit("```", 1)[0]
        resp_map[idx] = code

    # Now merge
    merged = []
    for p in prompts:
        idx = p["problem_id"]
        if idx in resp_map:
            merged.append({
                "problem_id": idx,
                "prompt": p["prompt"],
                "code": resp_map[idx]
            })

    Path(out_path).write_text(json.dumps(merged, indent=2), encoding="utf-8")
    print(f"Wrote {len(merged)} entries to {out_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("prompts_json",  help="Path to prompt.json")
    parser.add_argument("responses_json",help="Path to responses.json")
    parser.add_argument("output_json",   help="Path to output merged.json")
    args = parser.parse_args()
    merge_prompt_response(args.prompts_json, args.responses_json, args.output_json)
