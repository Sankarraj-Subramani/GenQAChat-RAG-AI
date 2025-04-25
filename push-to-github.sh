#!/bin/bash

# Initialize git repository
git init

# Create .gitignore
echo "
# Ignore build artifacts
frontend/.next/
backend/app/__pycache__/
vectorstore.pkl
models/
" > .gitignore

# Add important project files
git add backend/ frontend/ knowledge_base/ LICENSE README.md backend/requirements.txt frontend/package.json frontend/package-lock.json .gitignore

# Commit with a message
git commit -m "Initial commit: GenQAChat-RAG-AI backend, frontend, knowledge base, license, and documentation"

# Set branch to main
git branch -M main

# Add remote origin (CHANGE THIS URL TO YOUR GITHUB REPO!)
git remote add origin https://github.com/Sankarraj-Subramani/GenQAChat-RAG-AI.git

# Push code to GitHub
git push -u origin main
