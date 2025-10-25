from api.logger import LOG_FILE, LOG_SEPARATOR, error_console, error_file, info, success
import subprocess

def run_command_args(args: list[str]) -> subprocess.CompletedProcess:
    return run_command(" ".join(args))

def run_command(command: str) -> subprocess.CompletedProcess:
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )

        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"$ {command}\n")
            if result.returncode != 0:
                f.write(f"RETURN CODE: {result.returncode}\n")
            stdout_content = result.stdout.strip() if result.stdout else ""
            stderr_content = result.stderr.strip() if result.stderr else ""

            if stdout_content:
                f.write("STDOUT:\n")
                f.write(f"\t{stdout_content}\n")

            if stderr_content:
                f.write("STDERR:\n")
                f.write(f"\t{stderr_content}\n")
            f.write(LOG_SEPARATOR)

        if result.returncode != 0:
            error_console("Command execution failed, see log for details.")

        return result
    except Exception as e:
        error_console("Command execution failed, see log for details.")
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"$ {command}\n")
            f.write(f"ERROR: {e}\n")
            f.write(LOG_SEPARATOR)
        return subprocess.CompletedProcess(
            args=command,
            returncode=1,
            stdout="",
            stderr=str(e)
        )

def set_setting(key: str, value: str, filepath: str, separator: str = '='):
    commented_pattern = f"^#\\s*{key}\\s*="
    uncommented_pattern = f"^{key}\\s*="

    # check if commented line exists
    commented_exists = subprocess.call(
        f"grep -Eq '{commented_pattern}' '{filepath}'", shell=True
    ) == 0

    # check if uncommented line exists
    uncommented_exists = subprocess.call(
        f"grep -Eq '{uncommented_pattern}' '{filepath}'", shell=True
    ) == 0

    key_value = f"{key}{separator}{value}"

    if commented_exists:
        run_command(f"sed -i 's/{commented_pattern}.*/{key_value}/' '{filepath}'")
    elif uncommented_exists:
        run_command(f"sed -i 's/{uncommented_pattern}.*/{key_value}/' '{filepath}'")
    else:
        run_command(f"echo '{key_value}' | tee -a '{filepath}' > /dev/null")

    success(f"Set {key}={value} in {filepath}")
