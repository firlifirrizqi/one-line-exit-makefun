"""One-Line Exit — Make.fun entry.

Writes a single funny one-line resignation letter to /output/entry.txt.
Standard library only; nothing to install, nothing to configure.
"""

import os

ENTRY = (
    "Dear Team, I quit: the office plant I was told to water has outlived "
    "three managers, and I am not waiting to see who it takes next."
)

OUTPUT_PATH = "/output/entry.txt"


def verify() -> None:
    """Re-read the output and assert it is exactly the chosen line."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output differs from the chosen line"
    assert content == content.strip(), "entry has leading/trailing whitespace"
    assert 1 <= len(content) <= 200, "entry must be 1-200 characters"
    assert "\n" not in content and "\r" not in content, "entry must be one line"
    print(f"Verified: {len(content)} characters, single line, byte-identical.")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
