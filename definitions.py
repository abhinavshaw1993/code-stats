import os

# Defining Root Directory of the project.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# verbose print function.
verbose_print

# Function to define verbose function.
def define_verbose_print(verbose):
    # global verbose_print

    if verbose:
        def verbose_print(*args):
            for arg  in args:
                click.echo(arg)
    else:
        # Do nothing function.
        verbose_print = lambda *a : None
