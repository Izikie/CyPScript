from pathlib import Path

from api.logger import info, info_console
from api.utils import run_command_args

media_types = ('mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv',
               'mp3', 'wav', 'flac', 'aac', 'ogg',
               'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff')
executable_types = ('sh', 'bin', 'py')
document_types = ('pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'rtf')

all_types = media_types + executable_types + document_types

SCAN_LOG_FILE = Path("file_scan.log")

def scan_dir(home:bool):
    files_found = 0
    base_path = "/home" if home else "/"

    with SCAN_LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"== {"HOME" if home else "SYSTEM"} ==\n")

        for ext in all_types:
            cmd = ["find", base_path]
            if not home:
                prune_paths = ["/home", "/run"]
                for p in prune_paths:
                    cmd += ["-path", p, "-prune", "-o"]
            cmd += ["-type", "f", "-iname", f"*.{ext}", "-print"]

            result = run_command_args(cmd)
            if not result.stdout:
                continue

            for line in result.stdout.splitlines():
                line = line.strip()
                if line:
                    files_found += 1
                    f.write(f"{line}\n")
                    info_console(line)

        return files_found

def file_scanner():
    SCAN_LOG_FILE.write_text("")
    info("Scanning files...")

    system_files = scan_dir(home=False)
    home_files = scan_dir(home=True)

    total_files = system_files + home_files

    info(f"Scan complete.")

    info(f"System files: {system_files}")
    info(f"Home files: {home_files}")
    info(f"Total files: {total_files}")
