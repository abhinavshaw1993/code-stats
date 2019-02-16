"""
Module difining logging utils - verbose_print
"""
import click
import code_stats.definitions as definitions

import code_stats.utils.validation_utils as validations

def print_message(*args, msg_type):
	validations.validate_message_input(msg_type)

	for element in args:
		click.secho(str(element), fg=definitions.kTypeColorMap[msg_type])

"""
Implements singleton of logger.
"""
class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

"""
Logger class with bunch of logging functions.
1. verbose_print() - Print when verbosity set to True, which is only set
in the begining of the app.
"""
class Logger(Borg):

    verbose_print = None
    verbosity = None
    verbosity_level = 0

    def __init__(self):
        Borg.__init__(self)

    def set_verbosity(self, verbose, verbosity_level):
        if self.verbosity is None:
            self.verbosity = verbose
            self.verbosity_level = verbosity_level
            if verbose:
                self.verbose_print = lambda *a, v_lvl, msg_type : print_message(*a, msg_type=msg_type) if v_lvl <= self.verbosity_level else None
            else:
                self.verbose_print = lambda *a, v_lvl, msg_type : None
