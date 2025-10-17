import sys

from api.ui import console
from api.utils import LOG_FILE, LOG_SEPARATOR

# === SYSTEM ERRORS ===
ERR_NOT_LINUX = -1
ERR_UNSUPPORTED_DISTRO = -2

# === COMMAND ERRORS ===
ERR_COMMAND_FAIL = -3

# === GENERIC ERRORS ===
ERR_UNKNOWN = -99

def fatal_exit(message: str, code) -> None:
    console.print(f"[bold red]⚠️ {message}[/bold red]")

    if code != ERR_NOT_LINUX:
        with LOG_FILE.open(mode="a", encoding="utf-8") as f:
            f.write(f"FATAL: {message}, code={code}\n")
            f.write(LOG_SEPARATOR)

    sys.exit(code)