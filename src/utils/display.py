# display.py
# src/utils/display.py

from rich.console import Console

console = Console()

def print_info(msg: str):
    console.print(f"[bold cyan][INFO][/bold cyan] {msg}")

def print_error(msg: str):
    console.print(f"[bold red][ERROR][/bold red] {msg}")

def print_success(msg: str):
    console.print(f"[bold green][SUCCESS][/bold green] {msg}")
