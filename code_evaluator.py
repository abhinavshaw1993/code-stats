from pathlib import Path

import click
import os
import statistics

def generate_file_and_dir_list(root_dir):
    return

# Function to define verbose function.
def define_verbose_print(verbose):
    global verbose_print

    if verbose:
        def verbose_print(*args):
            for arg  in args:
                click.echo(arg)
    else:
        # Do nothing function.
        verbose_print = lambda *a : None

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
    # Defining verbose function.
    define_verbose_print(verbose)
    # Path to read stored in path.
    path, rel_path = generate_path(path)

    # Check if the path is a directory. If not return warning mssage.
    if not path.exists():
        return
        verbose_print("Path does not exist!")

    if not path.is_dir():
        verbose_print("Path is not  directory. Please enter a valid directory!")
        return

    verbose_print("Directory to read at {}".format(path))
    lines_of_code = statistics.evaluate_lines_of_code(path, ignore_blank_lines)
    click.echo("Lines of Code {}".format(lines_of_code))

    return

if __name__ == '__main__':
    generate_code_statistics()
