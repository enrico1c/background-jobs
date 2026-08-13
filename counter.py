#!/usr/bin/env python3
"""Increment the counter in counter.txt, creating it at 0 if missing."""
from pathlib import Path

COUNTER_FILE = Path(__file__).parent / "counter.txt"


def bump() -> int:
    current = int(COUNTER_FILE.read_text().strip()) if COUNTER_FILE.exists() else 0
    new_value = current + 1
    COUNTER_FILE.write_text(f"{new_value}\n")
    return new_value


def demo() -> None:
    """ponytail check: bump() must persist and increment correctly."""
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmp:
        global COUNTER_FILE
        original = COUNTER_FILE
        COUNTER_FILE = Path(tmp) / "counter.txt"
        try:
            assert bump() == 1
            assert bump() == 2
            assert COUNTER_FILE.read_text().strip() == "2"
        finally:
            COUNTER_FILE = original
    print("demo ok")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo()
    else:
        print(bump())
