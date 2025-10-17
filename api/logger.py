from api.ui import console
from api.utils import LOG_FILE, LOG_SEPARATOR

def error(message: str) -> None:
    console.print(f"[bold red]Error:[/bold red] {message}")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"ERROR: {message}\n")
        f.write(LOG_SEPARATOR)

def info(message: str) -> None:
    console.print(f"[bold yellow]Info:[/bold yellow] {message}")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"INFO: {message}\n")
        f.write(LOG_SEPARATOR)

def debug(message: str) -> None:
    console.print(f"[bold blue]Debug:[/bold blue] {message}")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"DEBUG: {message}\n")
        f.write(LOG_SEPARATOR)