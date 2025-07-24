import click
from rich.console import Console

console = Console()


@click.command()
@click.version_option()
def main():
    """{{cookiecutter.project_short_description}}"""
    console.print("[bold green]Hello from {{cookiecutter.project_name}}![/bold green]")


if __name__ == "__main__":
    main()
