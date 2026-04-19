import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from config import MAX_RETRIES
from file_manager import FileManager
from runner import CodeRunner
from fixer import AIFixer

console = Console()

def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Usage: python main.py <script_to_run.py>[/bold red]")
        sys.exit(1)

    target_file = sys.argv[1]
    
    if not os.path.exists(target_file):
        console.print(f"[bold red]Error: File '{target_file}' not found![/bold red]")
        sys.exit(1)

    try:
        fixer = AIFixer()
    except ValueError as e:
        console.print(f"[bold red]{e}[/bold red]")
        sys.exit(1)

    console.print(f"[bold blue]Step 1: Running code[/bold blue] ({target_file})")
    FileManager.create_backup(target_file)
    console.print(f"[italic dim]Backup created at {target_file}.bak[/italic dim]")

    retries = 0

    while retries < MAX_RETRIES:
        success, stdout, stderr = CodeRunner.run_script(target_file)

        if success:
            console.print("\n[bold green]Code executed successfully.[/bold green]")
            if stdout:
                console.print(Panel(stdout, title="Output", border_style="green"))
            sys.exit(0)
            
        # Error occurred
        console.print(f"\n[bold red]Step 2: Error detected (Attempt {retries + 1}/{MAX_RETRIES})[/bold red]")
        console.print(Panel(stderr, title="Error Traceback", border_style="red"))
        
        console.print("[bold yellow]Step 3: Sending error to AI...[/bold yellow]")
        
        current_code = FileManager.read_file(target_file)
        
        try:
            suggested_fix = fixer.get_fix(current_code, stderr)
        except Exception as e:
            console.print(f"[bold red]AI Fixer Error: {e}[/bold red]")
            sys.exit(1)

        console.print("[bold magenta]Step 4: AI suggested fix[/bold magenta]")
        syntax = Syntax(suggested_fix, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title="Suggested Code", border_style="magenta"))

        console.print("[bold cyan]Step 5: Applying fix...[/bold cyan]")
        FileManager.write_file(target_file, suggested_fix)

        console.print("[bold blue]Step 6: Retrying execution...[/bold blue]\n")
        retries += 1

    console.print(f"[bold red]Max retries ({MAX_RETRIES}) reached. The agent could not fix the code.[/bold red]")
    sys.exit(1)

if __name__ == "__main__":
    main()
