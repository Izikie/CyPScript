#!/usr/bin/env bash
set -e  # exit on any error

# Colors
GREEN="\033[1;32m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
RESET="\033[0m"

echo -e "${CYAN}🚀 Elevating privileges...${RESET}"
sudo -v  # ask for sudo password upfront

# Keep sudo alive until script finishes
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

# Install system packages only if missing
install_python() {
    case "$DISTRO" in
        debian|ubuntu|linuxmint)
            PKGS=("python3" "python3-venv" "python3-pip")
            for pkg in "${PKGS[@]}"; do
                if ! dpkg -s "$pkg" &>/dev/null; then
                    echo -e "${YELLOW}⚡ Installing $pkg...${RESET}"
                    sudo apt install -y "$pkg"
                else
                    echo -e "${CYAN}✔ $pkg already installed, skipping...${RESET}"
                fi
            done
            ;;
        fedora)
            PKGS=("python3" "python3-venv" "python3-pip")
            for pkg in "${PKGS[@]}"; do
                if ! rpm -q "$pkg" &>/dev/null; then
                    echo -e "${YELLOW}⚡ Installing $pkg...${RESET}"
                    sudo dnf install -y "$pkg"
                else
                    echo -e "${CYAN}✔ $pkg already installed, skipping...${RESET}"
                fi
            done
            ;;
        *)
            echo -e "${RED}❌ Unsupported distro: $DISTRO${RESET}"
            exit 1
            ;;
    esac
}

install_python

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}🛠 Setting up virtual environment...${RESET}"
    python3 -m venv .venv
else
    echo -e "${CYAN}✔ Virtual environment already exists, skipping...${RESET}"
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip itself
echo -e "${YELLOW}🔼 Upgrading pip...${RESET}"
UPGRADE_OUTPUT=$(pip install --upgrade pip 2>&1)
if echo "$UPGRADE_OUTPUT" | grep -q "Requirement already satisfied"; then
    echo -e "${CYAN}✔ pip is already up-to-date${RESET}"
else
    echo "$UPGRADE_OUTPUT"
fi

# Install dependencies if missing
install_if_missing() {
    PACKAGE=$1
    if ! pip show "$PACKAGE" &>/dev/null; then
        echo -e "${YELLOW}⚡ Installing $PACKAGE...${RESET}"
        pip install "$PACKAGE"
    else
        echo -e "${CYAN}✔ $PACKAGE already installed, skipping...${RESET}"
    fi
}

install_if_missing distro
install_if_missing beaupy

# Upgrade all outdated packages in the venv
echo -e "${YELLOW}🔄 Upgrading all outdated Python packages...${RESET}"
for pkg in $(pip list --outdated --format=columns | tail -n +3 | awk '{print $1}'); do
    echo -e "${YELLOW}⬆ Upgrading $pkg...${RESET}"
    pip install -U "$pkg"
done

# Run main.py using venv's Python
if [ -f "./main.py" ]; then
    echo -e "${GREEN}▶ Running main.py inside virtual environment...${RESET}"
    .venv/bin/python main.py
else
    echo -e "${RED}⚠️ main.py not found in current directory!${RESET}"
fi