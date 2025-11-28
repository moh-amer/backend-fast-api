#!/usr/bin/env bash

set -euo pipefail

# --- FUNCTIONS --------------------------------------------------------------

error() {
    echo "❌ Error: $1"
    exit 1
}

# --- READ TOKEN -------------------------------------------------------------

GITHUB_TOKEN="${1:-}"

if [[ -z "$GITHUB_TOKEN" ]]; then
    read -rsp "Enter your GitHub Personal Access Token: " GITHUB_TOKEN
    echo
fi

if [[ -z "$GITHUB_TOKEN" ]]; then
    error "GitHub token cannot be empty"
fi

# --- SYSTEM UPDATE ----------------------------------------------------------

echo "🔄 Updating system..."
sudo apt update -y

# --- INSTALL GH -------------------------------------------------------------

echo "📦 Installing GitHub CLI (gh)..."
type -p curl >/dev/null || sudo apt install curl -y

if ! command -v gh >/dev/null 2>&1; then
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg

    sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
https://cli.github.com/packages stable main" \
        | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

    sudo apt update -y
    sudo apt install gh -y
else
    echo "✅ gh already installed"
fi

# --- GH AUTH ---------------------------------------------------------------

echo "🔐 Authenticating GitHub CLI..."
echo "$GITHUB_TOKEN" | gh auth login --with-token

# --- GIT CONFIG ------------------------------------------------------------

echo "⚙️ Updating ~/.gitconfig to use gh as credential helper..."

git config --global credential.helper ""
git config --global credential.helper "!gh auth git-credential"

# --- CREATE REPO ------------------------------------------------------------
echo "📁 Creating Dev repository..."
mkdir -p ~/dev && cd ~/dev
git clone https://github.com/moh-amer/backend-fast-api.git && cd backend-fast-api

echo "🎉 Configuration complete."
echo "You can now use git and gh without entering your token again."

# --- START CLAUDE ------------------------------------------------------------
echo "Starting Claude..."
claude

