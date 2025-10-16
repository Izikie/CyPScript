from api.ui import console
from api.utils import LOG_FILE_SEPARATOR

def error(message: str) -> None:
    console.print(f"[bold red]Error:[/bold red] {message}")
    with open("detailedLog.txt", "a", encoding="utf-8") as f:
        f.write(f"ERROR: {message}\n")
        f.write(LOG_FILE_SEPARATOR)  # separator

def info(message: str) -> None:
    console.print(f"[bold green]Info:[/bold green] {message}")
    with open("detailedLog.txt", "a", encoding="utf-8") as f:
        f.write(f"INFO: {message}\n")
        f.write(LOG_FILE_SEPARATOR)  # separator

def debug(message: str) -> None:
    console.print(f"[bold blue]Debug:[/bold blue] {message}")
    with open("detailedLog.txt", "a", encoding="utf-8") as f:
        f.write(f"DEBUG: {message}\n")
        f.write(LOG_FILE_SEPARATOR)  # separator