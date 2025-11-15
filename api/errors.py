import sys
from api.logger import LOG_FILE, LOG_SEPARATOR, error_console

# === SYSTEM ERRORS ===
ERR_NOT_LINUX = -1
ERR_UNSUPPORTED_DISTRO = -2

# === COMMAND ERRORS ===
ERR_COMMAND_FAIL = -3

# === GENERIC ERRORS ===
ERR_UNKNOWN = -99

# === Script Fatal Exit ===
ERR_UNKNOWN_OPTION = -100

def fatal_exit(message: str, code: int) -> None:
    error_console(message)

    if code != ERR_NOT_LINUX:
        with LOG_FILE.open(mode = "a", encoding = "utf-8") as f:
            f.write(f"FATAL: {message}, code={code}\n")
            f.write(LOG_SEPARATOR)

    sys.exit(code)
