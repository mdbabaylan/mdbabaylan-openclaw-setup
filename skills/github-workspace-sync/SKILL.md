---
name: github-workspace-sync
description: "Sync your OpenClaw workspace to GitHub, commit and push documentation changes, view repo status, and manage your public portfolio. Use when you want to: (1) commit and push workspace changes (config files, SOUL.md, AGENTS.md, markdown docs), (2) view repo status and recent commits, (3) list files changed since last commit, (4) automatically exclude API keys and daily journals from commits. Automatically filters .env files, memory/YYYY-MM-DD.md, and other sensitive files."
---

# GitHub Workspace Sync

Manage your OpenClaw workspace documentation in GitHub without leaving your chat. This skill handles commits, pushes, and repo management while automatically protecting sensitive files.

## Quick Start

**Push documentation changes:**
```
Push my OpenClaw workspace docs with a clear commit message
```

**Check repo status:**
```
Show me the status of my mdbabaylan-openclaw-setup repo
```

**List recent commits:**
```
What's been committed to my OpenClaw repo recently?
```

## How It Works

1. **Automatic Filtering**: Excludes `.env`, daily journals (`memory/YYYY-MM-DD.md`), and API keys before committing
2. **Clear Commits**: Generates descriptive commit messages based on what changed
3. **Session Persistence**: Your GitHub token is stored securely; persists across session resets
4. **Public Portfolio**: Committed files are visible in your OpenClaw setup repo for job opportunities

## Files and Usage

See `references/commands.md` for detailed API commands and options.

## What Gets Committed

✅ **Included:**
- `SOUL.md`, `AGENTS.md`, `IDENTITY.md`, `USER.md`
- `HEARTBEAT.md`
- Configuration and setup docs
- Skill improvements and references

❌ **Excluded (automatic):**
- `.env` and API keys
- `memory/` directory (daily journals)
- `journal/` directory (raw logs)
- `.git/`, `node_modules/`, `dist/`
- Other generated artifacts

## Setting Up

Your GitHub token is already stored securely. The skill uses it to:
- Authenticate with GitHub API
- Push to your `mdbabaylan-openclaw-setup` repo
- List files and check status

If you need to reset the token, ask to update the GitHub credentials.
