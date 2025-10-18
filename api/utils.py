from api.logger import LOG_FILE, LOG_SEPARATOR
from api.ui import console
import subprocess

def run_command(command: str) -> subprocess.CompletedProcess:
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"$ {command}\n")
            if result.stdout:
                f.write(f"STDOUT:\n{result.stdout}\n")
            if result.stderr:
                f.write(f"STDERR:\n{result.stderr}\n")
            f.write(LOG_SEPARATOR)

        return result
    except Exception as e:
        console.print(f"[bold red]Command failed:[/bold red] {e}")
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"$ {command}\n")
            f.write(f"EXCEPTION: {e}\n")
            f.write(LOG_SEPARATOR)
        return subprocess.CompletedProcess(args=command, returncode=1, stdout="", stderr=str(e))