import click

from todo import io


@click.command()
@click.option('--file', help='To-Do list file.')
def main(file):
    for x in io.read_items(file):
        print(x)


if __name__ == '__main__':
    main()
