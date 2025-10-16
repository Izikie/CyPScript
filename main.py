from api import ui
import os

ui.console.clear()

if os.geteuid() != 0:
    ui.console.print("[bold red]⚠️ Please execute this with sudo.[/bold red]")
    exit(-1)

if not ui.confirm_prompt("Did you read the README and check your forensic questions?"):
    ui.console.print(
        "\n[bold red]⚠️ You should really read the README and check your forensic questions first.[/bold red]"
    )
    ui.console.print("[red]Skipping this can cause issues or make the VM incompletable.[/red]")
    ui.console.print()
    ui.console.print("[yellow]" + ('=' * 80) + "[/yellow]")
    exit(-1)

ui.console.print(r""" .______    __       _______  _______ .______   
 |   _  \  |  |     |   ____||   ____||   _  \  
 |  |_)  | |  |     |  |__   |  |__   |  |_)  | 
 |   _  <  |  |     |   __|  |   __|  |   ___/  
 |  |_)  | |  `----.|  |____ |  |____ |  |      
 |______/  |_______||_______||_______|| _|      
""")

option = ui.select_multiple_prompt("Select what to do?", ["Update", "Exit"])
ui.console.print(option)
