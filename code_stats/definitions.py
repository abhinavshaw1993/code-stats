import os
import pathlib

# Defining Root Directory of the project.
ROOT_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
USER_HOME = pathlib.Path.home()

# Font colors
kOutputFontColor = "yellow"
kNotificationFontColor = 'blue'

# data units.
data_units = {
"b" : 1,
"kb" : 1024,
"mb" : 1024*1024,
"gb" : 1024*1024*1024
}

kTypeColorMap = {
'info' : 'green',
'warning' : 'red',
'error' : 'red'
}
