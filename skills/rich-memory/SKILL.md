# rich-memory

Retrieve contextual, quirky, long-term memory about people, projects, and preferences.

## When to Use

- User mentions a name → fetch their people file
- Context feels thin → retrieve relevant memories
- Making a recommendation → check preferences first
- User refers to past events → search daily logs

## Memory Layout

```
memory/
├── people/           # Individuals: traits, stories, emotional beats
│   ├── alice.md
│   └── bob.md
├── projects/         # Active work: decisions, blockers, code choices
│   └── website-v2.md
└── preferences/      # How the user likes things done
    └── user.md
```

## Retrieval Modes

| Mode | Use When | Speed |
|------|----------|-------|
| `exact` | You have a name/topic | Fast |
| `semantic` | Conceptually related | Medium |
| `recent` | Looking for fresh context | Fast |

## Usage

```python
from rich_memory import retrieve

# Get everything about a person
context = retrieve("alice", mode="exact")

# Find semantically similar memories
context = retrieve("frustrated with code", mode="semantic", top_k=3)
```

## Writing Good Memory

**People files:** Store patterns, not just facts.

❌ "Alice likes coffee"
✅ "Alice claims to hate pineapple pizza, but always eats it when stressed"

**Project files:** Capture *decisions made* and *why*.

❌ "Using React"
✅ "Chose React over Vue because team knows it; revisit if performance issues arise"

**Preferences:** Note the *edge cases*.

❌ "Prefers short answers"
✅ "Wants brevity by default, but detail when learning something new"
