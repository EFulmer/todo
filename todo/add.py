"""Add an item to the To-Do List."""
from pathlib import Path

import click

from todo import io


@click.command()
@click.option("-t", "--task", type=str)
@click.option("-f", "--file", help="To-Do list file.", default="./todo.csv")
def main(task, file):
    if not Path(file).exists():
        raise FileNotFoundError(f"To-Do List does not exist as file {file}.")
    io.add_item(file_name=file, task=task)


if __name__ == "__main__":
    main()
