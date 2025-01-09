import click
import argparse

## All the commands are defined here
@click.command() 
def hello():
    click.echo('Hello world!')

@click.command()
def initdb():
    click.echo('Database initialized')
    
@click.command() 
def dropdb():
    click.echo('Database dropped')
    
@click.command() 
@click.argument('task')
def add(task):
    click.echo(f'\'{task}\' task added.')

## Click group starts here
@click.group()
def cli():
    pass 

## Commands added to cli here
cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(add)

def main():
    """
    Main driver function goes here
    """
    # Initialize ArgumentParser with custom program name
    parser = argparse.ArgumentParser(prog='LazyBoy')
    
    # Define optional arguments here
    # Flag to display name of the application
    parser.add_argument('-n', '--name', action='store_true', help='Display name of the application.')
    
    # Flag to enable verbosity
    parser.add_argument('-v', '--verbose', action='store_true', default=0)

    parser.add_argument('command', choices=['add', 'remove', 'list'], help='Add, remove or list the tasks', nargs='?')
    args, remaining_args = parser.parse_known_args()
    
    print(args)
    print(remaining_args)
    
    if args.command == 'add':
        parser.add_argument('task', nargs='+', type=str)
        args = parser.parse_args()
    else:
        args = parser.parse_known_args(remaining_args)
             
    task_list = []
    
    match args.command:
        case 'add':
            task_str = " ".join(args.task)
            task_list.append(task_str)
            
            print(f"Task {task_list.index(task_str)+1} was added.")
            
            if args.verbose:
                print(f"Task {task_list.index(task_str)+1} \'{task_str}\' was added.\n")
        
        case "list":
            if not task_list: 
                print("No task to show.")
            else:
                for t in task_list: 
                    print(f"{task_list.index(t)+1} : {t} \n")
                
if __name__ == "__main__":
    cli()