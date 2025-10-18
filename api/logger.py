from pathlib import Path
from datetime import datetime

from api.ui import console

LOG_FILE = Path(f"out-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log")
LOG_SEPARATOR = "=" * 80 + "\n"

def error(message: str) -> None:
    console.print(f"[bold red][❌][/bold red] {message}")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"ERROR: {message}\n")
        f.write(LOG_SEPARATOR)

def info(message: str) -> None:
    console.print(f"[bold yellow][!][/bold yellow] {message}")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"INFO: {message}\n")
        f.write(LOG_SEPARATOR)
