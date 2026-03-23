#!/usr/bin/env python3
"""
Generate a daily summary markdown file from conversation history.
Usage: python3 generate_summary.py <session_file> [output_dir]
"""

import sys
import os
from datetime import datetime
import re

def slugify(text):
    """Convert text to a filename-friendly slug."""
    return re.sub(r'[^\w\s-]', '', text).strip().replace(' ', '-').lower()

def generate_summary(content, date_str):
    """Generate a markdown summary from conversation content."""
    lines = content.strip().split('\n')
    
    # Extract key topics/themes (first 3-5 non-empty lines as hints)
    topics = []
    for line in lines[:20]:
        line = line.strip()
        if line and len(line) > 10 and not line.startswith('#'):
            topics.append(line[:80])
            if len(topics) >= 5:
                break
    
    summary = f"""# Daily Summary — {date_str}

## Key Topics
"""
    for topic in topics[:3]:
        summary += f"- {topic}...\n"
    
    summary += f"""
## Conversation Notes

{content}

---
*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    return summary

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_summary.py <content_file> [output_dir]")
        sys.exit(1)
    
    content_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "memory"
    
    if not os.path.exists(content_file):
        print(f"Error: File not found: {content_file}")
        sys.exit(1)
    
    os.makedirs(output_dir, exist_ok=True)
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    with open(content_file, 'r') as f:
        content = f.read()
    
    summary = generate_summary(content, date_str)
    
    output_file = os.path.join(output_dir, f"{date_str}.md")
    
    # If file exists, append
    if os.path.exists(output_file):
        with open(output_file, 'a') as f:
            f.write(f"\n\n---\n\n{summary}")
        print(f"Appended to: {output_file}")
    else:
        with open(output_file, 'w') as f:
            f.write(summary)
        print(f"Created: {output_file}")

if __name__ == "__main__":
    main()
