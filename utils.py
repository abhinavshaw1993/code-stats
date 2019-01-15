"""
Util functions for calculating statistics.
"""
import os
import yaml

def calculate_total_line_for_file(path_to_file):
    """
    Calculate the total number of line in the given file.
    """
    with open(path_to_file) as f:
        for i, l in enumerate(f):
            pass

    return i + 1

def get_files_and_folders_from_dir(path):
    files = []
    folders = []

    for entry in os.scandir(path):
        if entry.is_dir():
            folders.append(entry)
        else:
            files.append(entry)

    return files, folders

def read_yaml(path):
    # Reading from YML file.
    with open(file_name, "r") as ymlfile:
        yaml_file = yaml.load(ymlfile)

    return yaml_file
