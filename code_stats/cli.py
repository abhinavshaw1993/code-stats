import click
import os
import sys

# Adding directories to path.
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], 'utils'))

import code_stats.bin.statistics as statistics
import code_stats.utils.conversion_utils as conversion_utils
from pathlib import Path
from code_stats.definitions import data_units
from code_stats.bin.logger  import Logger
from code_stats.definitions import USER_HOME

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
@click.option("--du", default="b", help="Data Unit to calculate File Sizes.\n\
                                    Accepted values-\n\
                                    1. b - Bytes \n\
                                    2. kb - Kilo Bytes \n\
                                    3. mb - Mega Bytes \n 4. gb - Giga Bytes")
@click.option("--ignore_blank_lines", is_flag=True, help="Ignore blank lines while calculating lines of code.")
@click.option("--ignore_extensions", default="", help="Comma separated string of extensions that needs to be ignored.")
@click.option("--verbose", is_flag=True, help="Run in verbose mode.")
@click.option("--v_lvl", default=0, help="Verbosity level, verbosity set lesser or equal this number to will be printed. Needs --verose flag to be true.")
def generate_code_statistics(path, du, ignore_blank_lines, ignore_extensions, verbose, v_lvl):
    click.secho("############## CodeStat Output ################", bg='white', fg="black", bold=True)
    # Instantiating logging object.
    logger = Logger()
    logger.set_verbosity(verbose, v_lvl)

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

    if du not in data_units.keys():
        click.echo("Invalid Data Unit, please enter valid Data Unit.")

    ignore_extensions = conversion_utils.convert_csv_to_list(ignore_extensions)

    Logger().verbose_print("Directory to read is at {}".format(path),
                            v_lvl=0, msg_type='info')
    statistics.generate_and_print_stats(path_to_project=path,
                                        ignore_blank_lines=ignore_blank_lines,
                                        data_unit=du,
                                        ignore_extensions=ignore_extensions)
    click.echo()
    click.secho("################### End Output ######################", bg='white', fg="black", bold=True)

if __name__ == '__main__':
    generate_code_statistics()
