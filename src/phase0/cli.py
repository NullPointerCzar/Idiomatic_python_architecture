import typer
from phase0.exceptions import ApplicationError
from phase0.logger import setup_logging
from phase0.services import UserApiClient, UserBatchIterator

app = typer.Typer(help="Phase0 CLI tool for interacting with the Phase0 API")

@app.command()
def process(
url: str = typer.Option(
"https://jsonplaceholder.typicode.com/users",
"--url", "-u"
),batch_size: int = typer.Option(  # ← ADD THIS
        2,  # Default value
        "--batch-size", "-b",  # Command-line options
        help="Number of users per batch"  # Help text
),
) -> None:
    setup_logging()
    try:
        client = UserApiClient(base_url = url)
        users = client.fetch_users()
        iterator = UserBatchIterator(users, batch_size=batch_size)
        
        for idx, batch in enumerate(iterator, start=1):
            typer.echo(f"--- Batch {idx} ---")
            for user in batch:
                typer.echo(f" [{user.id}] {user.name} <{user.email}>")
                
    except ApplicationError as err:
        logging.getLogger(__name__).error(
            f"Execution failed: {err}"
        )
        raise typer.Exit(code=1) from err
    
if __name__ == "__main__":
    app()