#!/usr/bin/env python3
"""Print a friendly summary of the repository's top-level contents.

Usage:

    python3 scripts/repo_check.py
    python3 scripts/repo_check.py --json

This script uses only the Python standard library.
"""

import argparse
import json
from pathlib import Path


def find_repository_root(start: Path) -> Path:
    """Find the nearest repository root from a starting path."""
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate

    script_root = Path(__file__).resolve().parent.parent
    if (script_root / ".git").exists():
        return script_root
    raise RuntimeError("Could not find the repository root.")


def build_summary(repository_root: Path) -> dict[str, object]:
    """Build a structured summary of the repository."""
    entries = sorted(repository_root.iterdir(), key=lambda path: path.name)
    return {
        "repository": repository_root.name,
        "root": str(repository_root),
        "entries": [
            {"name": entry.name, "type": "directory" if entry.is_dir() else "file"}
            for entry in entries
        ],
    }


def main() -> None:
    """Display the repository summary in text or JSON format."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        action="store_true",
        help="print the summary as JSON instead of human-readable text",
    )
    args = parser.parse_args()

    repository_root = find_repository_root(Path.cwd().resolve())
    summary = build_summary(repository_root)

    if args.json:
        print(json.dumps(summary, indent=2))
        return

    print(f"Hello! Checking repository: {repository_root.name}")
    print("Top-level files and directories:")
    for entry in summary["entries"]:
        suffix = "/" if entry["type"] == "directory" else ""
        print(f"- {entry['name']}{suffix}")


if __name__ == "__main__":
    main()
