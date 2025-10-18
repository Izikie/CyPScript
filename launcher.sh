#!/usr/bin/env bash
set -eo pipefail

# Colors
GREEN="\033[1;32m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
RESET="\033[0m"

# Elevate privileges
echo -e "${CYAN}🚀 Elevating privileges...${RESET}"
sudo -v
while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

# Detect distro
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo -e "${RED}❌ Cannot detect Linux distribution!${RESET}"
    exit 1
fi
echo -e "${GREEN}✅ Detected distro: ${DISTRO}${RESET}"

# Install system packages
echo -e "${YELLOW}⚡ Installing system packages...${RESET}"
case "$DISTRO" in
    debian|ubuntu|linuxmint)
        sudo DEBIAN_FRONTEND=noninteractive apt install -yqq python3 python3-venv python3-pip >/dev/null 2>&1
        ;;
    fedora)
        sudo dnf install -yqq python3 python3-venv python3-pip >/dev/null 2>&1
        ;;
    *)
        echo -e "${RED}❌ Unsupported distro: $DISTRO${RESET}"
        exit 1
        ;;
esac
echo -e "${GREEN}✔ System packages ready${RESET}"

# Setup virtual environment
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}🛠 Setting up virtual environment...${RESET}"
    python3 -m venv .venv
else
    echo -e "${CYAN}✔ Virtual environment exists, skipping...${RESET}"
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
echo -e "${YELLOW}⬆ Upgrading pip...${RESET}"
python3 -m pip install -qq --upgrade pip
echo -e "${GREEN}✔ pip is ready${RESET}"

# Install required Python packages
echo -e "${YELLOW}📦 Installing required Python packages...${RESET}"
python3 -m pip install -qq --upgrade distro beaupy
echo -e "${GREEN}✔ Python dependencies ready${RESET}"

# Run main.py
if [ -f "./main.py" ]; then
    echo -e "${GREEN}▶ Running script inside virtual environment...${RESET}"
    .venv/bin/python main.py
else
    echo -e "${RED}⚠️ script not found in current directory!${RESET}"
fi
