# Copilot Sandbox Reference

## Files currently in the repository

- `README.md` introduces the GitHub Skills "Introduction to GitHub" course.
- `LICENSE` contains the repository license.
- `.gitignore` defines common files Git should ignore.
- `.github/` contains exercise step instructions, GitHub Actions workflows, and image assets.

## Core Git command checklist

- [ ] `git status` — Shows changed, staged, and untracked files in the working tree.
- [ ] `git add` — Stages selected file changes for the next commit.
- [ ] `git commit` — Records the staged changes with a commit message.
- [ ] `git push` — Uploads committed branch changes to the remote repository.
- [ ] `git checkout -b` — Creates a new branch and switches to it.

## Common Pitfalls & Quick Fixes

- If `git push` is rejected because the remote has newer commits, run `git pull --rebase` and then retry `git push`.
- If you commit to the wrong branch, create or switch to the intended branch, then move the commit with `git cherry-pick <commit>` before pushing it.
