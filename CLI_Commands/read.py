import click
import requests


@click.command()
def read():
    """Pull a golden phrase from our favorite PM Bot"""
    r = requests.get(
        'https://us-central1-whatsapp-chatbot-327023.cloudfunctions.net/whatsapp-chatbot')
    response = r.json()['text']
    click.echo(response)


if __name__ == '__main__':
    read()
