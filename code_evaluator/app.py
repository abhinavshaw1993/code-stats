import click
import os
import sys

# Adding directories to path.
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], 'utils'))

import code_evaluator.bin.statistics as statistics
from pathlib import Path
from utils.logging_utils  import Logger

# Function to generate paths.
def generate_path(path):
    # Getting relative path and path from string.
    rel_path = os.getcwd()

    if rel_path in path:
        click.echo("relative path in path, no need to append.")
        path = Path(path)
    else:
        path = Path(os.path.join(rel_path, path))

    rel_path = Path(rel_path)

    return path, rel_path

# Main function which reads the command line arguments.
@click.command()
@click.option("--path", default="", help="Path to Project.")
@click.option("--verbose", is_flag=True, help="Run in verbose mode.")
@click.option("--ignore_blank_lines", is_flag=True, help="Ignores blank lines while calculating lines of code.")
def generate_code_statistics(path, verbose, ignore_blank_lines):
    # Instantiating logging object.
    logger = Logger()
    logger.set_verbosity(verbose)
    # Path to read stored in path.
    path, rel_path = generate_path(path)

    # Check if the path is a directory. If not return warning mssage.
    if not path.exists():
        return
        logger.verbose_print("Path does not exist!")

    if not path.is_dir():
        logger.verbose_print("Path is not  directory. Please enter a valid directory!")
        return

    logger.verbose_print("Directory to read at {}".format(path))
    lines_of_code = statistics.evaluate_lines_of_code(path, ignore_blank_lines)
    click.echo("Lines of Code {}".format(lines_of_code))

    return

if __name__ == '__main__':
    generate_code_statistics()
