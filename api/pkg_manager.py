from abc import ABC, abstractmethod
from api.utils import *

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

def get_package_manager() -> PackageManager:
    distro_type = detect_distro()
    if distro_type in (DistroType.DEBIAN, DistroType.UBUNTU, DistroType.MINT):
        return AptPackageManager()
    elif distro_type == DistroType.FEDORA:
        return RpmPackageManager()
    else:
        raise RuntimeError(f"No package manager for distro: {distro_type}")