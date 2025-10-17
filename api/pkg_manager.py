import sys
from abc import ABC, abstractmethod
from enum import Enum, auto

from distro import distro

from api.errors import fatal_exit, ERR_NOT_LINUX, ERR_UNSUPPORTED_DISTRO
from api.utils import *

class DistroType(Enum):
    DEBIAN = auto()
    UBUNTU = auto()
    MINT = auto()
    FEDORA = auto()
    UNKNOWN = auto()

DISTRO_TYPE = DistroType.UNKNOWN

class PackageManager(ABC):
    @abstractmethod
    def install(self, package_name: str) -> None:
        pass

    @abstractmethod
    def uninstall(self, package_name: str) -> None:
        pass

    @abstractmethod
    def update(self: str) -> None:
        """Refresh the package list"""
        pass

    @abstractmethod
    def upgrade(self) -> None:
        """Upgrade installed packages"""
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Remove orphaned/unneeded packages"""
        pass

class AptPackageManager(PackageManager):
    def install(self, package_name: str) -> None:
        run_command(f"apt-get install -y {package_name}")

    def uninstall(self, package_name: str) -> None:
        run_command(f"apt-get remove -y {package_name}")

    def update(self: str) -> None:
        run_command("apt-get update -y")

    def upgrade(self: str) -> None:
        run_command("apt-get upgrade -y")

    def cleanup(self) -> None:
        run_command("apt-get autoremove -y")

class RpmPackageManager(PackageManager):
    def install(self, package_name: str) -> None:
        pass

    def uninstall(self, package_name: str) -> None:
        pass

    def update(self) -> None:
        pass

    def upgrade(self) -> None:
        pass

    def cleanup(self) -> None:
        pass

def detect_distro():
    global DISTRO_TYPE
    if not sys.platform.startswith("linux"):
        fatal_exit("Only Linux is supported", ERR_NOT_LINUX)

    match distro.id().lower():
        case "linuxmint":
            DISTRO_TYPE = DistroType.MINT
        case "ubuntu":
            DISTRO_TYPE = DistroType.UBUNTU
        case "debian":
            DISTRO_TYPE = DistroType.DEBIAN
        case "fedora":
            DISTRO_TYPE = DistroType.FEDORA
        case _:
            fatal_exit("Unsupported Linux distribution", ERR_UNSUPPORTED_DISTRO)

def get_package_manager() -> PackageManager | None:
    match DISTRO_TYPE:
        case DistroType.DEBIAN | DistroType.UBUNTU | DistroType.MINT:
            return AptPackageManager()
        case DistroType.FEDORA:
            return RpmPackageManager()
    return None