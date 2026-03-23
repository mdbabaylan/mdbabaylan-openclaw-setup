# Obsidian Vault Integration Skill

Integrate OpenClaw with your Obsidian vault for journaling, todos, and auto-linked knowledge graphs.

## Prerequisites

```bash
# Install obsidian-cli (requires Node.js)
npm install -g obsidian-cli

# Or use obsidian-export if you prefer:
pip install obsidian-exporter
```

## Configuration

Set your vault path in environment or config:

```bash
export OBSIDIAN_VAULT_PATH="/home/user/Documents/ObsidianVault"
```

Or in OpenClaw config:
```yaml
skills:
  obsidian:
    vault_path: "/home/user/Documents/ObsidianVault"
    daily_notes_folder: "00 - Daily"
    todos_folder: "01 - Todos"
    projects_folder: "02 - Projects"
    auto_tag: true
    auto_link: true
```

## Tools

### 1. journal_entry

Create a timestamped journal entry in daily notes.

```yaml
name: journal_entry
description: Add an entry to today's daily note
tool_type: exec
command: |
  cd "{{vault_path}}" && \
  echo "- {{timestamp}} — {{content}}" >> "{{daily_folder}}/{{date}}.md"
parameters:
  vault_path:
    type: string
    default: "{{OBSIDIAN_VAULT_PATH}}"
  content:
    type: string
    required: true
  date:
    type: string
    default: "$(date +%Y-%m-%d)"
  timestamp:
    type: string
    default: "$(date +%H:%M)"
  daily_folder:
    type: string
    default: "00 - Daily"
```

### 2. add_todo

Create a new todo item.

```yaml
name: add_todo
description: Create a todo item in the todos folder
tool_type: exec
command: |
  cd "{{vault_path}}" && \
  cat >> "{{todos_folder}}/Inbox.md" << 'EOF'
  
  - [ ] {{content}} #todo {{tags}}
  EOF
parameters:
  content:
    type: string
    required: true
  tags:
    type: string
    default: ""
  vault_path:
    type: string
    default: "{{OBSIDIAN_VAULT_PATH}}"
  todos_folder:
    type: string
    default: "01 - Todos"
```

### 3. create_note

Create a new note with optional frontmatter.

```yaml
name: create_note
description: Create a new note in the vault
tool_type: exec
command: |
  cd "{{vault_path}}" && \
  mkdir -p "$(dirname '{{path}}')" && \
  cat > "{{path}}" << 'EOF'
  ---
  created: {{date}}
  tags: {{tags}}
  ---
  
  # {{title}}
  
  {{content}}
  EOF
parameters:
  title:
    type: string
    required: true
  path:
    type: string
    required: true
  content:
    type: string
    required: true
  tags:
    type: string
    default: "[]"
  date:
    type: string
    default: "$(date +%Y-%m-%d)"
  vault_path:
    type: string
    default: "{{OBSIDIAN_VAULT_PATH}}"
```

### 4. link_notes

Create a link between two notes (adds to both).

```yaml
name: link_notes
description: Create bidirectional links between notes
tool_type: exec
command: |
  cd "{{vault_path}}" && \
  echo "" >> "{{source}}" && \
  echo "→ Related: [[{{target_name}}]]" >> "{{source}}" && \
  echo "" >> "{{target}}" && \
  echo "→ Related: [[{{source_name}}]]" >> "{{target}}"
parameters:
  source:
    type: string
    required: true
  target:
    type: string
    required: true
  source_name:
    type: string
    required: true
  target_name:
    type: string
    required: true
  vault_path:
    type: string
    default: "{{OBSIDIAN_VAULT_PATH}}"
```

### 5. extract_entities

Extract key entities from text and suggest links.

```yaml
name: extract_entities
description: Identify entities that could be linked notes
tool_type: llm
prompt: |
  Extract key entities (people, projects, concepts, technologies) from this text.
  Return as a JSON array of objects with "entity" and "type" fields.
  
  Types: person, project, concept, technology, company, book, paper
  
  Text: {{text}}
  
  Output JSON only.
parameters:
  text:
    type: string
    required: true
```

### 6. vault_search

Search the vault for existing notes.

```yaml
name: vault_search
description: Search vault for existing notes
tool_type: exec
command: |
  cd "{{vault_path}}" && \
  find . -name "*.md" -type f | xargs grep -l "{{query}}" 2>/dev/null | head -10
parameters:
  query:
    type: string
    required: true
  vault_path:
    type: string
    default: "{{OBSIDIAN_VAULT_PATH}}"
```

## Usage Examples

### Daily Journaling
```
User: Log this — spent 2 hours debugging QLoRA rank settings, rank 64 stable, 128 unstable

→ Calls: journal_entry(content="Debugged QLoRA — rank 64 stable, rank 128 unstable without extended warmup")
→ Auto-extracts: [[QLoRA]], [[Fine-tuning]]
→ Creates stubs if they don't exist
```

### Project Notes
```
User: Create a project note for "OpenClaw Local Setup"

→ Calls: create_note(
    title="OpenClaw Local Setup",
    path="02 - Projects/OpenClaw Local Setup.md",
    content="Setup guide for running OpenClaw with Ollama...",
    tags="[openclaw, ollama, ai, self-hosted]"
  )
```

### Todo Management
```
User: Add todo — finish Obsidian skill documentation

→ Calls: add_todo(content="Finish Obsidian skill documentation", tags="#openclaw #docs")
```

### Auto-Linking
```
User: Link my QLoRA note to the Fine-tuning note

→ Calls: link_notes(
    source="03 - Concepts/QLoRA.md",
    target="03 - Concepts/Fine-tuning.md",
    source_name="QLoRA",
    target_name="Fine-tuning"
  )
```

## System Prompt Integration

Add to your agent's system prompt:

```markdown
You have access to an Obsidian vault for knowledge management.

When conversations contain:
- Action items → use add_todo
- Learnings/insights → use journal_entry  
- New projects/topics → use create_note
- References to existing notes → use link_notes

Auto-extract entities using extract_entities and suggest connections.
Always ask before creating new notes unless explicitly instructed.
```

## Workflow: Conversation → Graph

1. **Capture** → Journal entries from daily conversations
2. **Extract** → Pull out entities, projects, concepts
3. **Create** → Stub notes for new entities
4. **Link** → Connect related ideas automatically
5. **Review** → Weekly graph view to spot clusters and gaps

## Tips

- Use daily notes as a "firehose" — everything goes there
- Promote daily entries to project notes when they grow
- Tag aggressively for filtering in graph view
- Weekly review: look for orphan notes (no links) and connect them
- Use templates for recurring note types

## Dependencies

- obsidian-cli OR direct filesystem access
- Node.js (for obsidian-cli)
- jq (for JSON processing, optional)
