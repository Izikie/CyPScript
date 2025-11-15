from api.pkg_manager import update, upgrade
from api.logger import *

def update_system():
    info("Updating package lists...")
    update()
    info("Upgrading system...")
    upgrade()
