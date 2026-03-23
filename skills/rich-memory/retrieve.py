#!/usr/bin/env python3
"""
Rich Memory Retrieval
Simple keyword-based retrieval for now.
Future: add embedding-based semantic search.
"""

import os
import glob
import yaml
from pathlib import Path

# Load config
CONFIG_PATH = Path(__file__).parent / "config.yaml"
with open(CONFIG_PATH) as f:
    CONFIG = yaml.safe_load(f)

def get_memory_files(category=None):
    """Get all memory files for a category or all categories."""
    files = []
    base = Path(".")
    
    if category and category in CONFIG["memory_paths"]:
        path = CONFIG["memory_paths"][category]
        pattern = f"{path}/*.md"
        files.extend(glob.glob(pattern))
    else:
        for path in CONFIG["memory_paths"].values():
            if path == "memory/":
                pattern = f"{path}????-??-??.md"  # Daily files
            else:
                pattern = f"{path}/*.md"
            files.extend(glob.glob(pattern))
    
    return sorted(files)

def search_files(query, files, case_sensitive=False):
    """Simple keyword search across files."""
    results = []
    query = query if case_sensitive else query.lower()
    
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                content_check = content if case_sensitive else content.lower()
                
                if query in content_check:
                    # Extract snippet around match
                    idx = content_check.find(query)
                    start = max(0, idx - 200)
                    end = min(len(content), idx + 500)
                    snippet = content[start:end]
                    
                    results.append({
                        "file": filepath,
                        "snippet": snippet,
                        "full": content
                    })
        except Exception as e:
            continue
    
    return results

def retrieve(query, mode="exact", category=None, top_k=None):
    """
    Retrieve relevant memory.
    
    Args:
        query: What to search for
        mode: "exact", "semantic" (fallback to exact for now), "recent"
        category: "people", "projects", "preferences", or None for all
        top_k: Max results to return
    """
    top_k = top_k or CONFIG["retrieval"]["top_k"]
    files = get_memory_files(category)
    
    if mode == "recent":
        # Sort by mtime, return newest
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        results = [{"file": f, "full": open(f).read()} for f in files[:top_k]]
    else:
        # exact or semantic (both keyword for now)
        results = search_files(query, files)
        results = results[:top_k]
    
    return results

def format_for_context(results):
    """Format retrieval results for insertion into context."""
    if not results:
        return ""
    
    output = ["## Relevant Memory"]
    for r in results:
        filename = os.path.basename(r["file"])
        output.append(f"\n### {filename}")
        output.append(r.get("full", r.get("snippet", "")))
    
    return "\n".join(output)

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "test"
    results = retrieve(query)
    print(format_for_context(results))
