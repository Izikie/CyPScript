from pathlib import Path
from datetime import datetime

from rich.text import Text

from api.ui import console

LOG_FILE = Path(f"out-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log")
LOG_SEPARATOR = "=" * 80 + "\n"

def out(message: str):
    console.print(message)

def log(message: str):
    console.print(message)

    if isinstance(message, Text):
        plain_message = message.plain
    else:
        plain_message = Text.from_markup(message).plain

    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{plain_message}\n")

def success(message):
    console.print(f"[bold green][✔️][/bold green] {message}")

# === Info Logging ===
def info_file(message: str) -> None:
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"INFO: {message}\n")

def info_console(message: str) -> None:
    console.print(f"[bold yellow][⚠️][/bold yellow] {message}")

def info(message: str) -> None:
    info_console(message)
    info_file(message)

# === Error Logging ===
def error_file(message: str) -> None:
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"ERROR: {message}\n")

def error_console(message: str) -> None:
    console.print(f"[bold red][❌][/bold red] {message}")

def error(message: str) -> None:
    error_console(message)
    error_file(message)