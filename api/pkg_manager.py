import sys

from distro import distro

from api.errors import fatal_exit, ERR_NOT_LINUX, ERR_UNSUPPORTED_DISTRO
from api.utils import *

def install(package_name: str) -> None:
    run_command(f"apt-get install -yqq {package_name}")

def uninstall(package_name: str) -> None:
    run_command(f"apt-get remove -yqq {package_name}")

def update() -> None:
    run_command("apt-get update -yqq")

def upgrade() -> None:
    run_command("apt-get upgrade -yqq")

def cleanup() -> None:
    run_command("apt-get autoremove -yqq")

def ensure_compatibility():
    if not sys.platform.startswith("linux"):
        fatal_exit("Only Linux is supported", ERR_NOT_LINUX)

    if "debian" not in distro.id().lower() and "debian" not in distro.like().lower().split():
        fatal_exit("Unsupported Linux distribution, only Debian-based distros are supported", ERR_UNSUPPORTED_DISTRO)