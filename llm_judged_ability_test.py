#!/usr/bin/env python3
import os
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any
import math

# New v1 client
from openai import OpenAI
# dotenv for .env loading
from dotenv import load_dotenv

load_dotenv()
JUDGE_NAME = os.getenv("JUDGE_NAME", "EDA Judge")

def load_pairs(pairs_json: str) -> List[Dict[str, Any]]:
    with open(pairs_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def verify_alignment(prompt: str, code: str, client: OpenAI, model: str = "gpt-4o-mini") -> str:
    system = (
        f"You are {JUDGE_NAME}, an EDA design verification assistan, focus on syntax. "
        "Answer with YES or NO, followed by a brief justification."
    )
    user = (
        f"Prompt:\n{prompt}\n\n"
        f"Script:\n```python\n{code}\n```\n\n"
        "Does this script correctly implement the prompt?"
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user}
        ],
        temperature=0.0
    )
    return resp.choices[0].message.content.strip()

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Verify a batch of EDA script↔prompt pairs"
    )
    p.add_argument("pairs_json",  help="Path to JSON file with prompt/code pairs")
    p.add_argument("--api-key",   help="OpenAI API key (env overrides)")
    args = p.parse_args()

    api_key = args.api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not provided. Set --api-key or OPENAI_API_KEY.")

    # Instantiate the new client
    client = OpenAI(api_key=api_key)

    pairs = load_pairs(args.pairs_json)
    for entry in pairs:
        pid    = entry["problem_id"]
        prompt = entry["prompt"]
        code   = entry["code"]
        print(f"--- {pid} ---")
        result = verify_alignment(prompt, code, client)
        print(result, "\n")
