from enum import Enum, auto
from pathlib import Path

from ui import console
import subprocess
import distro

LOG_FILE = Path("detailedLog.txt")
LOG_FILE_SEPARATOR = "=" * 80 + "\n"

def run_command(command: str) -> subprocess.CompletedProcess:
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"$ {command}\n")
            if result.stdout:
                f.write(f"STDOUT:\n{result.stdout}\n")
            if result.stderr:
                f.write(f"STDERR:\n{result.stderr}\n")
            f.write(LOG_FILE_SEPARATOR)

        return result
    except Exception as e:
        console.print(f"[bold red]Command failed:[/bold red] {e}")
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"$ {command}\n")
            f.write(f"EXCEPTION: {e}\n")
            f.write(LOG_FILE_SEPARATOR)
        return subprocess.CompletedProcess(command, 1, "", str(e))

class DistroType(Enum):
    DEBIAN = auto()
    UBUNTU = auto()
    MINT = auto()
    FEDORA = auto()

def detect_distro() -> DistroType:
    name = distro.id().lower()
    if "linuxmint" in name:
        return DistroType.MINT
    elif name == "ubuntu":
        return DistroType.UBUNTU
    elif name == "debian":
        return DistroType.DEBIAN
    elif name == "fedora":
        return DistroType.FEDORA
    else:
        raise RuntimeError(f"Unsupported OS: {name}")
