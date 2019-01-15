"""
Util functions for calculating statistics.
"""
import os
from collections import deque

def get_total_line_for_file(path_to_file):
    """
    Calculate the total number of line in the given file.
    """
    with open(path_to_file) as f:
        for i, l in enumerate(f):
            pass

    return i + 1

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

def get_sub_files_in_dir(path_to_dir):
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
        folders.extendleft( sub_folders)
        files += sub_files

    return files

def get_sub_folders_in_dir(path_to_dir):
    """
    Returns the folders in a directory, includes the folders in sub directories.
    """
    # Intermediate variable.
    folders = deque([path_to_dir])
    persistent_folders_list = folders

    # Loop to get files in all sub directories using BFS.
    while folders:
        current_dir = folders.popleft()
        sub_files, sub_folders = get_files_and_folders_in_dir(current_dir)
        folders.extendleft(sub_folders)
        persistent_folders_list.extendleft(sub_folders)

    return persistent_folders_list
