from api.pkg_manager import get_package_manager
from api.utils import set_setting, run_command_args, run_command

DEFAULT_PASSWORD = "Cyb3rPatr!0t$" # NEVER DO THIS A REAL SYSTEM, ONLY FOR SPEED DURING COMPETITION !!!!

LOGIN_CONFIG = "/etc/login.defs"
FAILLOCK_CONFIG = "/etc/security/faillock.conf"

PAM_PWQUALITY = "/usr/share/pam-configs/pwquality"
PAM_UNIX = "/usr/share/pam-configs/unix"


# Remove nullok this time from common-auth
def account_security():
    get_package_manager().install("libpam-pwquality")

    # /etc/login.defs
    login_settings = {
        "SYSLOG_SU_ENAB": "yes",
        "SYSLOG_SG_ENAB": "yes",
        "PASS_MAX_DAYS": "90",
        "PASS_MIN_DAYS": "10",
        "PASS_WARN_AGE": "14"
    }

    for key, value in login_settings.items():
        set_setting(key, value, LOGIN_CONFIG, separator='\t\t')

    # /etc/security/faillock.conf
    set_setting("unlock_time", "1800", FAILLOCK_CONFIG)
    set_setting("deny", "5", FAILLOCK_CONFIG)

    # PAM_PWQUALITY settings
    # PAM_UNIX settings

    # common-auth: remove nullok

    # Apply updated PAM settings
    run_command("sudo pam-auth-update --package --force")

