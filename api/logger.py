from pathlib import Path
from datetime import datetime

from rich.text import Text

from api.ui import console

SYMBOL_SUCCESS = "✔"
SYMBOL_INFO = "!"
SYMBOL_ERROR = "⛌"

LOG_FOLDER = Path(f"logs-{datetime.now().strftime('%Y%m%d-%H%M%S')}")
LOG_FILE = LOG_FOLDER / "log.txt"

# Make sure the folder exists
LOG_FOLDER.mkdir(parents=True, exist_ok=True)

LOG_SEPARATOR = "=" * 80 + "\n"

def out(message: str):
    console.print(message)

def log(message: str):
    console.print(message)

    if isinstance(message, Text):
        plain_message = message.plain
    else:
        plain_message = Text.from_markup(message).plain

    with LOG_FILE.open(mode = "a", encoding = "utf-8") as f:
        f.write(f"{plain_message}\n")

def success(message):
    console.print(f"[bold green][{SYMBOL_SUCCESS}][/bold green] {message}")

# === Info Logging ===
def info_file(message: str) -> None:
    with LOG_FILE.open(mode = "a", encoding = "utf-8") as f:
        f.write(f"INFO: {message}\n")

def info_console(message: str) -> None:
    console.print(f"[bold yellow][{SYMBOL_INFO}][/bold yellow] {message}")

def info(message: str) -> None:
    info_console(message)
    info_file(message)

# === Error Logging ===
def error_file(message: str) -> None:
    with LOG_FILE.open(mode = "a", encoding="utf-8") as f:
        f.write(f"ERROR: {message}\n")

def error_console(message: str) -> None:
    console.print(f"[bold red][❌][/bold red] {message}")

def error(message: str) -> None:
    error_console(message)
    error_file(message)