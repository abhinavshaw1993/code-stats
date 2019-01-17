"""
Module difining logging utils - verbose_print
"""

def print_list(*args):
	for element in args:
		print(element)
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

    def __init__(self):
        Borg.__init__(self)

    def set_verbosity(self, verbose):
        if self.verbosity is None:
            self.verbosity = verbose
            if verbose:
                print("Verbosity set correctly")
                self.verbose_print = lambda *a : print_list(*a)
            else:
                self.verbose_print = lambda *a : None

    def get_verbose_print():
        if verbosity is not None:
            return self.verbose_print

        return
