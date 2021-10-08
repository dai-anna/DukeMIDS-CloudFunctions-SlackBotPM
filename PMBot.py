import click
from CLI_Commands import read
from CLI_Commands import write


@click.group(help="CLI tool to read from and write to my Planet Scale PM Bot database")
def cli():
    pass


cli.add_command(read.read)
cli.add_command(write.write)

if __name__ == '__main__':
    cli()
