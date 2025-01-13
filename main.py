import click
from queryset import QuerySet

## Initializing query object
query = QuerySet()

## All the commands are defined here
@click.command() 
def hello():
    click.echo('Hello world!')

@click.command()
def start():
    query.create_table()
    click.echo('Database initialized.')
    
@click.command() 
def close():
    query.close_db()
    click.echo('Database closed')

@click.command() 
@click.argument('task')
def add(task):
    query.add_task(task)
    click.echo(f'\'{task}\' task added.')

@click.command()
def list():
    tasks = query.fetch_all()
    
    if tasks:
        print("ID  Tasks")
        print("-------------------")
        
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}   {task[1]}")
            
        print("\n")
    else:
        print("No tasks to show.")
    
## Click group starts here
@click.group()
def cli():
    pass 

## Commands added to cli here
cli.add_command(start)
cli.add_command(add)
cli.add_command(list)
                
if __name__ == "__main__":
    cli()