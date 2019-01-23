import click
import os
import sys

# Adding directories to path.
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], 'utils'))

import code_evaluator.bin.statistics as statistics
from pathlib import Path
from code_evaluator.bin.logger  import Logger
from code_evaluator.definitions import USER_HOME

# Function to generate paths.
def generate_path(path):
    # Resolvin `~`.
    if '~' in path:
        return Path(path.replace('~', str(USER_HOME)))

    # Getting relative path and path from string.
    rel_path = os.getcwd()
    if rel_path in path:
        click.echo("relative path in path, no need to append.")
        path = Path(path)
    else:
        path = Path(os.path.join(rel_path, path))

    return path

# Main function which reads the command line arguments.
@click.command()
@click.option("--path", default="", help="Path to Project, accepts both Pure and Relative")
@click.option("--verbose", is_flag=True, help="Run in verbose mode.")
@click.option("--v_lvl", default=0, help="Verbosity level, everythin lesser and equal to is print. Needs --verose flag to be true.")
@click.option("--ignore_blank_lines", is_flag=True, help="Ignores blank lines while calculating lines of code.")
def generate_code_statistics(path, verbose, v_lvl, ignore_blank_lines):
    # Instantiating logging object.
    logger = Logger()
    logger.set_verbosity(verbose, v_lvl)

    # Print Results.
    click.secho("############## Code Evaluator Output ################", bg='white', fg="black", bold=True)
    # Path to read stored in path.
    path = generate_path(path)
    Logger().verbose_print("Path: {} \n".format(path), v_lvl=1, msg_type='warning')

    # Check if the path is a directory. If not return warning mssage.
    if not path.exists():
        click.echo("Path does not exist!")
        return

    if not path.is_dir():
        click.echo("Path is not  directory. Please enter a valid directory!")
        return

    logger.verbose_print("Directory to read at {}".format(path), v_lvl=0, msg_type='info')
    statistics.generate_and_print_stats(path, ignore_blank_lines=ignore_blank_lines)

    click.echo()
    click.secho("################### End Output ######################", bg='white', fg="black", bold=True)
    return

if __name__ == '__main__':
    generate_code_statistics()
