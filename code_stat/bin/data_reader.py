import yaml
import os
import sys

from code_stat.definitions import ROOT_DIR

def read_yaml(file_path):
    """Util to read Yaml File."""

    # Reading from YML file.
    with open(os.path.join(ROOT_DIR, file_path), "r") as ymlfile:
        yaml_file = yaml.load(ymlfile)

    return yaml_file
