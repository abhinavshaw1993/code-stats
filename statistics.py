"""
Python Module for Generating Various Statistics.
"""
from utils import get_files_and_folders_from_dir, calculate_total_line_for_file
import os
import yaml
from collections import deque

def evaluate_lines_of_code(path, ignore_blank_lines=False):
    """
    Count lines of code in folder.
    """
    lines_of_code = 0
    files = []
    folders = deque([path])

    while folders:
        current_dir = folders.popleft()
        sub_files, sub_folders = get_files_and_folders_from_dir(current_dir)
        folders.extendleft( sub_folders)
        files += sub_files

    for file in files:
        file_name, file_ext = os.path.splitext(file)
        print("File_name {} and ext{} : ".format(file_name, file_ext))

        if file_ext in file_ext_list :
            lines_of_code += calculate_total_line_for_file(file)

    return lines_of_code
