from ui import console
import subprocess

def run_command(command: str) -> subprocess.CompletedProcess:
    """Run a shell command safely and return the process result."""
    try:
        return subprocess.run(command, shell=True, text=True, capture_output=True)
    except Exception as e:
        console.print(f"[bold red]Command failed:[/bold red] {e}")
        return subprocess.CompletedProcess(command, 1, "", str(e))