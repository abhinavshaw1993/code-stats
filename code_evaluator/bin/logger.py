"""
Module difining logging utils - verbose_print
"""
import click

kTypeColorMap = {
'info' : 'green',
'warning' : 'red',
'error' : 'red'
}

def print_list(*args, msg_type):
	if msg_type not in kTypeColorMap.keys():
		return

	for element in args:
		click.secho(str(element), fg=kTypeColorMap[msg_type])

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
TODO(abhinav) - Iplement this.
2. log(level) - Loggs at three levels, Info, Warning and Error.
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
                self.verbose_print = lambda *a, v_lvl, msg_type : print_list(*a, msg_type=msg_type) if v_lvl <= self.verbosity_level else None
            else:
                self.verbose_print = lambda *a, v_lvl, msg_type : None
