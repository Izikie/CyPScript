from api.pkg_manager import get_package_manager
from api.logger import *


def update_system():
    info("Updating package lists...")
    get_package_manager().update()
    info("Upgrading system...")
    get_package_manager().upgrade()
