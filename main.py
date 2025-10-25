from api.errors import fatal_exit, ERR_UNKNOWN_OPTION
from api.logger import LOG_SEPARATOR, log
from api.pkg_manager import detect_distro
from api.ui import *
from scripts.account_security import account_security, DEFAULT_PASSWORD
from scripts.cron_dumper import cron_dumper
from scripts.file_scanner import file_scanner
from scripts.network import network
from scripts.root_security import root_security
from scripts.software import software_manager
from scripts.update import update_system
from scripts.user_managment import user_management

console.clear()
detect_distro()

if not confirm_prompt("Did you read the README and check your forensic questions?"):
    console.print("[bold red]⚠️ You should really read the README and check your forensic questions first.[/bold red]")
    console.print("[red]Skipping this can cause issues or make the VM incompletable.[/red]")
    console.print()
    console.print("[yellow]" + LOG_SEPARATOR + "[/yellow]")
    exit(-1)

option_map = {
    "Scan Files": file_scanner,
    "Dump Cron": cron_dumper,
    "Configure and Update System": update_system,
    "Manage Software": software_manager,
    "Harden Network": network,
    "Harden Root Access": root_security,
    "Account Security": account_security,
    "Manage Users": user_management,
    "Exit": exit
}

def menu():
    console.print(r""".______    __       _______  _______ .______   
|   _  \  |  |     |   ____||   ____||   _  \  
|  |_)  | |  |     |  |__   |  |__   |  |_)  | 
|   _  <  |  |     |   __|  |   __|  |   ___/  
|  |_)  | |  `----.|  |____ |  |____ |  |      
|______/  |_______||_______||_______|| _|      
""")

    console.print(
        "[bold red]WARNING:[/bold red][red] This script is designed for Cyber patriot VM aligned environments.[/red]")
    console.print("[red]Use in other environments may lead to unexpected results.[/red]\n")

    console.print(
        f"[bold green]IMPORTANT:[/bold green] The password all users will be set to is [yellow]'[/yellow][green]{DEFAULT_PASSWORD}[/green][yellow]'[/yellow]\n")

    selected_options = select_multiple_prompt("Select what to do?", list(option_map.keys()))
    console.clear()
    return selected_options

while True:
    try:
        options = menu()

        for i, opt in enumerate(options, start=1):
            func = option_map.get(opt)
            if func:
                log(f"\n[bold cyan]{'*' * 10} {opt} ({i}/{len(options)}) {'*' * 10}[/bold cyan]\n")
                func()
            else:
                fatal_exit("Unknown option selected.", ERR_UNKNOWN_OPTION)

            if i == len(options):
                pause_prompt()

        console.clear()
    except (KeyboardInterrupt, EOFError):
        console.print("\n[bold red]Operation interrupted by user.[/bold red]")
        exit(0)

