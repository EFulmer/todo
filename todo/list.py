"""List To-Do items."""
import click

from todo import io


@click.command()
@click.option("-f", "--file", help="To-Do list file.", default="./todo.csv")
@click.option("-c", "--show-completed", help="Show completed items.", default=False)
def main(file, show_completed):
    if show_completed:
        for x in io.show_all(file):
            print(x)
    else:
        for x in io.show_non_complete(file):
            print(x)


if __name__ == "__main__":
    main()
