"""
Util functions for calculating statistics.
"""
import os
import copy
from collections import deque

from code_stats.definitions import data_units

def get_total_line_for_file(path_to_file, ignore_blank_lines=False):
    """
    Calculate the total number of line in the given file.
    """
    i = 0
    with open(path_to_file) as f:
        for line in f:
            if line == "\n" and ignore_blank_lines:
                pass
            else:
                i+=1

    return i

def get_files_and_folders_in_dir(path_to_dir):
    """
    Returns the files and folders in the diretory.
    """
    files = []
    folders = []

    for entry in os.scandir(path_to_dir):
        if entry.is_dir():
            folders.append(entry)
        else:
            files.append(entry)

    return files, folders

def get_files_in_dir(path_to_dir):
    """
    Returns the files in a directory, includes the files in sub directories.
    """
    # Intermediate variable.
    files = []
    folders = deque([path_to_dir])

    # Loop to get files in all sub directories using BFS.
    while folders:
        current_dir = folders.popleft()
        sub_files, sub_folders = get_files_and_folders_in_dir(current_dir)
        folders.extendleft(sub_folders)
        files += sub_files

    return files

def get_folders_in_dir(path_to_dir):
    """
    Returns the folders in a directory, includes the folders in sub directories.
    """
    # Intermediate variable.
    folders = deque([path_to_dir])
    persistent_folders_list = copy.deepcopy(folders)

    # Loop to get files in all sub directories using BFS.
    while folders:
        current_dir = folders.popleft()
        sub_files, sub_folders = get_files_and_folders_in_dir(current_dir)
        folders.extendleft(sub_folders)
        persistent_folders_list.extendleft(sub_folders)

    return persistent_folders_list

def get_size_for_file(file, data_unit):
    """
    Returns size for the file.
    """
    # Gets the file size in bytes.
    file_stat = os.stat(file)

    return file_stat.st_size / data_units[data_unit]
