"""
Python Module for Generating Various Statistics.
"""
import os
import utils.files_and_folders_utils as utils
import utils.data_utils as data_utils
from collections import defaultdict

kDefaultFileExtYamlFilePath = "data/default_file_ext_list.yaml"

def evaluate_lines_of_code(path_to_project,
                           ignore_blank_lines=False,
                           file_ext_list_file_path=kDefaultFileExtYamlFilePath):
    """
    Count lines of code in folder.
    """
    # Variable to store total number of lines of code.
    lines_of_code = 0
    # Default dict storying lines of code per file ext.
    lines_of_code_per_language  = defaultdict()

    # List of files and a deque of folders.
    files = utils.get_sub_files_in_dir(path_to_project)
    folders = utils.get_sub_folders_in_dir(path_to_project)

    print("files: ", files)
    print("Folders: ", folders)

    file_ext_list = data_utils.read_yaml(file_ext_list_file_path)

    # Loop to count lines of files.
    for file in files:
        file_name, file_ext = os.path.splitext(file)

        if file_ext in file_ext_list :
            line_count = calculate_total_line_for_file(file)
            lines_of_code_per_language[file_ext] += line_count
            lines_of_code += line_count

    return lines_of_code, lines_of_code_per_language

def evaluate_num_files_and_folders():
    """
    Returns Count of files and folders in the project.
    """
    file_count = count(utils.get_sub_files_in_dir(path_to_project))
    folder_count = count(utils.get_sub_folders_in_dir(path_to_project))

    return file_count, folder_count
