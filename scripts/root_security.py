import subprocess

from api.logger import info
from api.utils import run_command


def root_security():
    run_command("passwd -l root")
    info("Disabled Root Account")

    result = subprocess.run(
        ["grep", "-q", "NOPASSWD\\|!authenticate", "/etc/sudoers"],
        check=False
    )

    if result.returncode == 0:
        print("Instances of NOPASSWD or !authenticate found, please check /etc/sudoers")
    else:
        print("No instances of NOPASSWD or !authenticate found")

    run_command("chmod 640 /etc/shadow")
    info("Changed /etc/shadow permissions to 640")
