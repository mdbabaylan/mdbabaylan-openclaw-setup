#!/bin/bash
# sync-to-github.sh - Push workspace changes to GitHub with auto-filtering

set -e

REPO_DIR="/root/.openclaw/workspace-chat"
GITHUB_TOKEN_FILE="${REPO_DIR}/.github-token"
REPO_NAME="mdbabaylan-openclaw-setup"
GITHUB_USER="mdbabaylan"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if token file exists
if [ ! -f "$GITHUB_TOKEN_FILE" ]; then
    echo -e "${RED}Error: GitHub token not found at $GITHUB_TOKEN_FILE${NC}"
    exit 1
fi

TOKEN=$(cat "$GITHUB_TOKEN_FILE")

# Files and patterns to exclude from commits
EXCLUDED=(
    ".env"
    "*.env"
    "memory/[0-9]*-[0-9]*-[0-9]*.md"
    "journal/"
    ".git/"
    "node_modules/"
    "dist/"
    ".github-token"
)

# Function to check if file should be excluded
should_exclude() {
    local file="$1"
    for pattern in "${EXCLUDED[@]}"; do
        if [[ "$file" == $pattern ]] || [[ "$file" =~ $pattern ]]; then
            return 0  # Should exclude
        fi
    done
    return 1  # Should not exclude
}

# Change to repo directory
cd "$REPO_DIR"

# Get list of changed files
echo -e "${YELLOW}Checking changed files...${NC}"
CHANGED_FILES=$(git diff --name-only --cached)
if [ -z "$CHANGED_FILES" ]; then
    CHANGED_FILES=$(git diff --name-only)
fi

if [ -z "$CHANGED_FILES" ]; then
    echo -e "${YELLOW}No changes to commit${NC}"
    exit 0
fi

# Filter out excluded files
echo -e "${YELLOW}Filtering excluded files...${NC}"
FILTERED_FILES=()
while IFS= read -r file; do
    if ! should_exclude "$file"; then
        FILTERED_FILES+=("$file")
        echo -e "${GREEN}✓ Including: $file${NC}"
    else
        echo -e "${YELLOW}⊘ Excluding: $file${NC}"
    fi
done <<< "$CHANGED_FILES"

if [ ${#FILTERED_FILES[@]} -eq 0 ]; then
    echo -e "${YELLOW}No files to commit after filtering${NC}"
    exit 0
fi

# Stage filtered files
echo -e "${YELLOW}Staging files...${NC}"
git add "${FILTERED_FILES[@]}"

# Create descriptive commit message
echo -e "${YELLOW}Creating commit message...${NC}"
FILE_COUNT=${#FILTERED_FILES[@]}
FILE_LIST=$(printf '%s\n' "${FILTERED_FILES[@]}" | head -3 | sed 's/^/  - /')
COMMIT_MSG="docs: Update OpenClaw workspace documentation

Changes include:
${FILE_LIST}"

if [ $FILE_COUNT -gt 3 ]; then
    COMMIT_MSG="${COMMIT_MSG}
  ... and $((FILE_COUNT - 3)) more files"
fi

# Commit
echo -e "${YELLOW}Committing changes...${NC}"
git commit -m "$COMMIT_MSG" || {
    echo -e "${RED}Commit failed${NC}"
    exit 1
}

# Push to GitHub
echo -e "${YELLOW}Pushing to GitHub...${NC}"
git push origin main || {
    echo -e "${RED}Push failed. Checking remote...${NC}"
    git remote -v
    exit 1
}

echo -e "${GREEN}✓ Successfully pushed ${FILE_COUNT} files to GitHub${NC}"
echo -e "${GREEN}Repository: https://github.com/${GITHUB_USER}/${REPO_NAME}${NC}"
