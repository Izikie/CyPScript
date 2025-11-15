from api.logger import info, out
from api.pkg_manager import install
from api.utils import run_command, set_setting

SYSCTL_CONFIG = "/etc/sysctl.conf"

RP_FILTER = "1"
ACCEPT_REDIRECTS = "0"
SEND_REDIRECTS = "0"
ACCEPT_SOURCE_ROUTE = "0"
LOG_MARTIANS = "1"
IP_FORWARD = "0"
TCP_SYNCOOKIES = "1"
DISABLE_IPV6 = "1"

def network():
    info("Installing and enabling UFW (Uncomplicated Firewall)")
    install("ufw")
    run_command("ufw --force enable")

    info("Turning on UFW logging")
    run_command("ufw logging on")

    info("Configuring sysctl network parameters")

    settings = {
        "net.ipv4.conf.default.rp_filter": RP_FILTER,
        "net.ipv4.conf.all.rp_filter": RP_FILTER,
        "net.ipv4.conf.all.accept_redirects": ACCEPT_REDIRECTS,
        "net.ipv4.conf.all.send_redirects": SEND_REDIRECTS,
        "net.ipv4.conf.all.accept_source_route": ACCEPT_SOURCE_ROUTE,
        "net.ipv4.conf.all.log_martians": LOG_MARTIANS,
        "net.ipv4.ip_forward": IP_FORWARD,
        "net.ipv4.tcp_syncookies": TCP_SYNCOOKIES,
        "net.ipv6.conf.all.disable_ipv6": DISABLE_IPV6
    }

    for key, value in settings.items():
        set_setting(key, value, SYSCTL_CONFIG)

    run_command("sysctl -p > /dev/null")

    info("Current /etc/hosts file content:")
    result = run_command("cat /etc/hosts")
    if result.returncode == 0:
        out('\n'.join('\t' + line for line in result.stdout.splitlines()))