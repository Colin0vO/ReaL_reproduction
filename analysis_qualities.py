import re
import sys
import argparse

def report_yes_percentage_from_file(file_path: str):
    """
    Reads the contents of the given file, parses YES/NO judgments,
    and prints the total count, YES count, NO count, and percentage of YES responses.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
    except Exception as e:
        print(f"Error: could not read file '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)

    # extract YES/NO labels following each '--- n ---'
    labels = re.findall(r'---\s*\d+\s*---\s*(YES|NO)', contents)
    total = len(labels)
    if total == 0:
        print("No YES/NO entries found in the file.", file=sys.stderr)
        sys.exit(1)

    yes_count = labels.count('YES')
    no_count = total - yes_count

    print(f"Total checks:       {total}")
    print(f"YES count:          {yes_count}")
    print(f"NO count:           {no_count}")
    print(f"Percentage of YES:  {yes_count / total * 100:.2f}%")

def main():
    parser = argparse.ArgumentParser(
        description="Report the percentage of 'YES' judgments in an LLM judge output file."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="llm_judge_result.txt",
        help="Path to the text file containing the judge results (default: llm_judge_result.txt)"
    )
    args = parser.parse_args()
    report_yes_percentage_from_file(args.file)

if __name__ == "__main__":
    main()
