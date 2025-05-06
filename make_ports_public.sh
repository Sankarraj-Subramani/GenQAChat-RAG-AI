#!/bin/bash

# Check if GitHub Codespace environment
if [ -z "$CODESPACE_NAME" ]; then
  echo "❌ Not running inside a GitHub Codespace. Skipping port visibility update."
  exit 1
fi

echo "🔄 Making ports 3000 and 8000 public on Codespace: $CODESPACE_NAME"

# Update ports to public using GitHub CLI
gh codespace ports visibility 3000:public 8000:public --codespace "$CODESPACE_NAME"
