import click
import requests


@click.command()
@click.option('--newphrase', prompt='New PM phrase', help='Enter a new PM phrase you want to add to the Planet Scale PM database.')
def write(newphrase: str):
    """Add a new phrase to the Planet Scale PM database."""
    url = 'https://us-central1-whatsapp-chatbot-327023.cloudfunctions.net/PMbot-write'
    headers = {'Content-Type': 'application/json'}
    data = {"Message": newphrase}
    requests.post(url, headers=headers, data=data)
    click.echo("fine fine...")


if __name__ == '__main__':
    write()
