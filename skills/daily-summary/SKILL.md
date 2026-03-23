---
name: daily-summary
description: Create a daily summary markdown file of conversations. Use when the user wants to archive, save, or summarize the day's chat history before ending a session, running /new, or when they explicitly ask to "summarize today" or "save our conversation." Creates dated markdown files in memory/YYYY-MM-DD.md format.
---

# Daily Summary Skill

Create a markdown file summarizing the day's conversation topics and key points.

## When to Use

- User runs /new or mentions clearing the session soon
- User explicitly asks to "summarize today," "save our conversation," or "create a summary"
- End of day wrap-up when the conversation had meaningful content

## Output Format

Files are saved to `memory/YYYY-MM-DD.md` with this structure:

```markdown
# Daily Summary — 2026-03-06

## Key Topics
- Topic 1...
- Topic 2...
- Topic 3...

## Conversation Notes

[Brief summary of key discussions]

---
*Generated: 2026-03-06 14:30:00*
```

## Process

1. Review the conversation history for the session
2. Identify 3-5 key topics or themes discussed
3. Write a brief narrative summary (3-7 bullet points or short paragraphs)
4. Include any decisions made, insights shared, or action items
5. Save to `memory/YYYY-MM-DD.md`

## Script (Optional)

For automation, the helper script is available:
```bash
python3 scripts/generate_summary.py <content_file> [output_dir]
```

But manual creation via write-file tool is preferred for quality summaries.

## Notes

- If a file for today's date already exists, append to it with a separator
- Keep summaries concise but meaningful—future you will thank you
- Include emotional context if relevant (anxiety, wins, mood shifts)
- Don't include raw tool outputs unless they're meaningful results
