# GitHub Workspace Sync Commands

## Push Changes to Repo

**Push documentation updates with auto-filtering:**

When you ask to "push my workspace changes" or "commit and push the OpenClaw docs," the skill will:

1. Check what files have changed in the workspace
2. Filter out `.env`, `memory/`, `journal/`, and other excluded files
3. Stage the filtered changes
4. Create a descriptive commit message
5. Push to `mdbabaylan-openclaw-setup` on GitHub

**Example prompts:**
- "Push my SOUL.md and AGENTS.md updates"
- "Commit the config changes I made to OpenClaw"
- "Push documentation of my recent skill improvements"

## Check Repo Status

**View current status:**

```bash
git -C /root/.openclaw/workspace-chat status
```

**See last 10 commits:**

```bash
git -C /root/.openclaw/workspace-chat log --oneline -10
```

**See what changed since last commit:**

```bash
git -C /root/.openclaw/workspace-chat diff --name-only
```

## List Repository Files

**See all files in your OpenClaw setup repo:**

```bash
git -C /root/.openclaw/workspace-chat ls-files
```

## Authentication

Token is stored in `~/.openclaw/workspace-chat/.github-token` (excluded from Git).

To verify the token is working:

```bash
curl -s -H "Authorization: token $(cat ~/.openclaw/workspace-chat/.github-token)" https://api.github.com/user
```

If you see your GitHub username in the response, authentication is working.
