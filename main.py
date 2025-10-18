from api.pkg_manager import detect_distro
from api.ui import *
from scripts.account_security import account_security
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
    console.print("\n[bold red]⚠️ You should really read the README and check your forensic questions first.[/bold red]")
    console.print("[red]Skipping this can cause issues or make the VM incompletable.[/red]")
    console.print()
    console.print("[yellow]" + ('=' * 80) + "[/yellow]")
    exit(-1)

console.print(r""" .______    __       _______  _______ .______   
 |   _  \  |  |     |   ____||   ____||   _  \  
 |  |_)  | |  |     |  |__   |  |__   |  |_)  | 
 |   _  <  |  |     |   __|  |   __|  |   ___/  
 |  |_)  | |  `----.|  |____ |  |____ |  |      
 |______/  |_______||_______||_______|| _|      
""")

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

options = select_multiple_prompt("Select what to do?", list(option_map.keys()))
console.clear()

for opt in options:
    func = option_map.get(opt)
    if func:
        func()
    else:
        console.print(f"[red]Unknown option: {opt}[/red]")