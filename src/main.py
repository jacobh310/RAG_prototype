import typer 

app = typer.Typer()


@app.command()
def invoke():
    print('Hello')


if __name__=='__main__':
    app()