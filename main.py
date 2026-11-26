"""The Self-Checkout Is Judging You: one funny remark from a judgmental
self-checkout machine, at most 200 characters, written to /output/entry.txt.

The line: the till looks at a basket of twelve yoghurts and nothing else,
diagnoses it as a cry for help, then turns its own signature catchphrase
("Please place the item in the bagging area") back on the shopper by
asking them to place their dignity there instead. One image, one turn,
no padding: the basket is the whole joke.
"""

import os
import sys

LINE = (
    "Twelve yoghurts and nothing else \u2014 that\u2019s not a shop, "
    "that\u2019s a cry for help. Please place your dignity in the "
    "bagging area."
)


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be blank", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            print("written entry does not match the line", file=sys.stderr)
            return 1
    print(LINE)
    print(f"({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
