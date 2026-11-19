#!/usr/bin/env python3
"""Print a friendly summary of the repository's top-level contents.

Run from the repository root with:

    python3 scripts/repo_check.py

This script uses only the Python standard library.
"""

from pathlib import Path


def main() -> None:
    """Display the repository name and a sorted list of top-level entries."""
    repository_root = Path(__file__).resolve().parent.parent
    print(f"Hello! Checking repository: {repository_root.name}")
    print("Top-level files and directories:")

    entries = sorted(repository_root.iterdir(), key=lambda path: path.name)
    for entry in entries:
        # Distinguish directories from files while keeping the output concise.
        print(f"- {entry.name}/" if entry.is_dir() else f"- {entry.name}")


if __name__ == "__main__":
    main()
