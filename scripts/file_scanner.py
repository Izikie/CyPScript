from pathlib import Path

from api.logger import info, info_console
from api.utils import run_command

media_types = ('mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv',
               'mp3', 'wav', 'flac', 'aac', 'ogg',
               'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff')
executable_types = ('sh', 'bin', 'py', 'jar')
document_types = ('pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'rtf')

all_types = media_types + executable_types + document_types

LOG_FILE_PATH = Path("file_scan.log")

def file_scanner():
    info("Scanning Files...")

    def scan_dir(home: bool, label: str):
        """Scan either system (excluding /home) or /home itself."""
        files_found = 0
        path = "/home" if home else "/"

        with LOG_FILE_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(f"== {label} ==\n")

            for ext in all_types:
                cmd = f'find {path} '

                # Only prune /home if scanning system
                if not home:
                    cmd += "-path /home -prune -o "

                cmd += f'-iname "*.{ext}" -type f -print'

                result = run_command(cmd)
                if result.stdout:
                    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
                    files_found += len(lines)
                    for line in lines:
                        log_file.write(f"{line}\n")
                        if home:  # Only print /home files to console
                            info_console(line)

            log_file.write(f"Total {label} files: {files_found}\n\n")

        return files_found

    # Clear previous log
    LOG_FILE_PATH.write_text("")

    # System scan excluding /home
    info("Scanning system (excluding /home)...")
    sys_count = scan_dir(False, "SYS")

    # /home scan
    info("Scanning /home...")
    home_count = scan_dir(True, "HOME")

    total_files = sys_count + home_count

    with LOG_FILE_PATH.open("a", encoding="utf-8") as f:
        f.write(f"== TOTAL ==\nTotal files: {total_files}\n")

    # Console output
    info_console(f"Total SYS files: {sys_count}")
    info_console(f"Total HOME files: {home_count}")
    info_console(f"Total files: {total_files}")

    info(f"Scan complete. Total files found: {total_files}")

