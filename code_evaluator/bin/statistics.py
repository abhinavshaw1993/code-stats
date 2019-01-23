"""
Python Module for Generating Various Statistics.
"""
import os
import sys
import click

import code_evaluator.definitions as definitions
import code_evaluator.utils.files_and_folders_utils as utils
import code_evaluator.utils.data_utils as data_utils
import code_evaluator.utils.print_utils as print_utils
import code_evaluator.utils.conversion_utils as conversion_utils

from collections import Counter
from pathlib import Path
from code_evaluator.utils.logging_utils import Logger

kDefaultFileExtYamlFilePath = "data/default_ext_list.yml"

def get_extension_dict(file_ext_list_file_path):
    language_dict = data_utils.read_yaml(file_ext_list_file_path)

    return language_dict

def get_file_extension_list_from_dict(extensions_dict):
    """
    Return file extension list
    """
    extension_list = []
    for e in extensions_dict.values():
        extension_list += e

    return extension_list

def get_ext_to_language_map_from_dict(extensions_dict):
    ext_to_language_map = {}
    for e in extensions_dict.keys():
        values = extensions_dict[e]
        for v in values:
            ext_to_language_map[v] = e

    return ext_to_language_map

def generate_and_print_stats(path_to_project,
                            file_ext_list_file_path=kDefaultFileExtYamlFilePath,
                            ignore_blank_lines=False):
    """
    Generates and Prints statistics as a table on the Command Line.
    """
    click.echo("\n")
    header, output= generate_stats(path_to_project,
                            file_ext_list_file_path,
                            ignore_blank_lines)
    output_table = print_utils.table(
        data=output,
        header=header)
    click.secho(output_table, fg=definitions.kOutputFontColor)

def generate_stats(path_to_project,
                   file_ext_list_file_path=kDefaultFileExtYamlFilePath,
                   ignore_blank_lines=False):
    """
    Generates statistics as a list of lists and returns the header as well.
    """
    header = ['Language']

    total_lines_of_code, lines_of_code_per_language = evaluate_lines_of_code(
        path_to_project, file_ext_list_file_path, ignore_blank_lines)
    header.append('Lines of Code')

    percentage_of_code = evaluate_percentage_of_code(
        total_lines_of_code,lines_of_code_per_language)
    header.append('Percentage')

    output = conversion_utils.convert_dicts_to_list(
        lines_of_code_per_language, percentage_of_code)

    output.append(evaluate_total(output))

    return header, output

def evaluate_total(output):
    """
    Evaluates the total of the different statistics.
    @example: if lines of code and percentage for languages are
              Language Lines Percentage
              "Python"   20     20
              "Java"     80     80
              This will return ['Total', 100, 100]
    """
    total_stats = ['Total']
    for stat_idx in range(1, len(output[0])):
        stat_total = 0
        for lang_stats in output:
            stat_total += lang_stats[stat_idx]
        total_stats.append(stat_total)

    return total_stats

def evaluate_lines_of_code(path_to_project,
                           file_ext_list_file_path,
                           ignore_blank_lines):
    """
    Count lines of code in folder.
    """
    # Variable to store total number of lines of code.
    total_lines_of_code = 0
    # Default dict storying lines of code per file ext.
    lines_of_code_per_language  = Counter()

    files = utils.get_files_in_dir(path_to_project)
    folders = utils.get_folders_in_dir(path_to_project)

    # Language map is used to map file extension to programming languages.
    ext_dict = get_extension_dict(file_ext_list_file_path)
    ext_list = get_file_extension_list_from_dict(ext_dict)
    ext_lang_map = get_ext_to_language_map_from_dict(ext_dict)
    # Loop to count lines of files.
    for file in files:
        file_name, file_ext = os.path.splitext(file)

        if file_ext in ext_list :
            Logger().verbose_print("File: ", Path(file), v_lvl=5, msg_type='info')
            line_count = utils.get_total_line_for_file(file)
            lines_of_code_per_language[ext_lang_map[file_ext]] += line_count
            total_lines_of_code += line_count

    return total_lines_of_code, lines_of_code_per_language

def evaluate_percentage_of_code(total_lines_of_code, lines_of_code_per_language):
    """
    Return Percentage of code per language.
    """
    percentage_of_code = {}
    for key in lines_of_code_per_language.keys():
        percentage_of_code[key] = lines_of_code_per_language[key] / total_lines_of_code * 100

    return percentage_of_code

def evaluate_num_files_and_folders():
    """
    Returns Count of files and folders in the project.
    """
    file_count = count(utils.get_sub_files_in_dir(path_to_project))
    folder_count = count(utils.get_sub_folders_in_dir(path_to_project))

    return file_count, folder_count
