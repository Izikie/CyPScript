from api.pkg_manager import detect_distro
from api.ui import *
from scripts import *
from scripts.update import update_system

console.clear()

detect_distro()

if not confirm_prompt("Did you read the README and check your forensic questions?"):
    console.print(
        "\n[bold red]⚠️ You should really read the README and check your forensic questions first.[/bold red]"
    )
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

option = select_multiple_prompt("Select what to do?", [
    "Update",
    "Software Manager",
    "File Scanner",
    "Network & Firewall",
    "Root Security",
    "Password Quality & Account Security",
    "Cron Dumper",
    "User Management",
    "Exit"])

match option:
    case "Update":
        update_system()

console.print(option)
