#!/usr/bin/env python3
import json
import re
from detector import run_all_detectors
from tqdm import tqdm

# 提取 ``` 或 ```python 标记之间的代码块
CODE_PATTERN = re.compile(r"```(?:python)?\s*\n(.*?)```", re.S)

def extract_code(text: str) -> str:
    matches = CODE_PATTERN.findall(text)
    if matches:
        return "\n".join(matches).strip()
    return text.strip()


def main():
    cand_path = "responses.json"
    with open(cand_path, 'r', encoding='utf-8') as f:
        cands = json.load(f)

    total = len(cands)
    pass_count = 0
    # detailed issues per candidate
    details = []
    for idx, cand in enumerate(tqdm(cands, desc="Running detectors")):
        response = cand.get('response', '')
        code_string = extract_code(response)
        # 捕获检测过程中的异常，异常视为检测失败
        try:
            issues = run_all_detectors(code_string)
        except Exception:
            issues = ['error']
        # record issues for this candidate
        details.append({
            "index": idx,
            "issues": issues
        })
        # count as pass if no issues found
        if not issues:
            pass_count += 1

    rate = pass_count / total * 100 if total else 0
    # output summary and save detailed results
    summary = {
        "pass_count": pass_count,
        "total": total,
        "pass_rate": rate,
        "details": details
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    with open("detect_results.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()










