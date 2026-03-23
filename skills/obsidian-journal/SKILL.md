# obsidian-journal

Daily journaling skill with Obsidian CLI integration, proper frontmatter, and graph-view optimized tagging.

## Commands

| Command | Description |
|---------|-------------|
| `journal daily "<entry>" [--category <cat>] [--mood <mood>]` | Create daily note with entry |
| `journal search <query>` | Search journal entries |
| `journal tags` | List all tags with counts |
| `journal week` | Show last 7 days summary |

## Daily Note Format

```markdown
---
date: 2026-03-12T14:30:00
category: work
mood: focused
---

# 2026-03-12

Entry text here...

#journal #daily #work #mood-focused
```

## File Structure

```
vault/
├── journal/
│   ├── daily/
│   │   ├── 2026-03-12.md
│   │   └── 2026-03-11.md
│   └── weekly/
│       └── 2026-W11.md
```

## Tagging Strategy

- `#journal` - All journal entries (for graph view)
- `#daily` - Daily notes
- `#<category>` - Work, personal, health, etc.
- `#mood-<mood>` - Track emotional patterns

## Usage Examples

```bash
# Quick entry
journal daily "Shipped the feature, feeling good"

# With metadata
journal daily "Code review marathon" --category work --mood tired

# Search entries
journal search "feature"

# View tag stats
journal tags
```

## Graph View Tips

- Use `#journal` as central node filter
- Category tags create topic clusters
- Mood tags show emotional patterns over time
- Link related entries: `[[2026-03-11]]`

## Setup

Ensure Obsidian CLI is installed and vault path is set in `TOOLS.md`:
```markdown
### Obsidian
- Vault: ~/Documents/Obsidian
- CLI: obsidian-cli
```
