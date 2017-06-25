import click

@click.command()
@click.option('--count', prompt='count',default=1,help='Number of greetings.')
@click.option('--name',prompt='Your name',help='The person to greet.')
def hello(count,name):
    for x in range(count):
        click.echo("hello %s" % name)


if __name__ == '__main__':
    hello()