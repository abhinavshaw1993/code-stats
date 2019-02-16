import os

import code_stats.utils.conversion_utils as conversion_utils
import code_stats.utils.files_and_folders_utils as files_and_folders_utils
from code_stats.definitions import data_units
from pathlib import Path

TEST_DIR = os.path.dirname(__file__)

kTestDict1 =  {"python" : 50, "json": 100, "text" : 20}
kTestDict2 =  {"python" : .5, "json": .3, "text" : .2}
kTestList = [['python', 50], ['json', 100], ['text', 20]]
kTestListForMulDicts = [['python', 50, .5], ['json', 100, .3], ['text', 20, .2]]
kTestCSVExtensionString = "csv,json,python"
kTestExtentionList = ["csv", "json", "python"]

""" --------------------- Conversion Utils --------------------- """

def test_convert_dict_to_list():
    assert conversion_utils.convert_dict_to_list(kTestDict1) == kTestList

def test_list_to_dicts():
    assert conversion_utils.convert_dicts_to_list(kTestDict1, kTestDict2) == kTestListForMulDicts

def test_are_keys_equal():
    assert conversion_utils.are_keys_equal(kTestDict1, kTestDict2) == True

def test_convert_csv_to_list():
    """
    Accepts just a string, not new line separated files.
    """
    assert conversion_utils.convert_csv_to_list(kTestCSVExtensionString) == kTestExtentionList

""" --------------------- Files and Folder Utils --------------------- """

def test_get_total_line_for_file():
    test_file = os.path.join(TEST_DIR, 'testing_data/test_file.py')

    line_count = files_and_folders_utils.get_total_line_for_file(test_file,
                                                        ignore_blank_lines=False)
    actual_line_count = 7
    assert line_count == actual_line_count

    line_count_ignore_blanks = files_and_folders_utils.get_total_line_for_file(test_file,
                                                        ignore_blank_lines=True)
    actual_line_count_ignore_blanks = 5
    assert line_count_ignore_blanks == actual_line_count_ignore_blanks

def test_get_size_for_file():
    test_file = os.path.join(TEST_DIR, 'testing_data/test_file.py')

    file_size_bytes = files_and_folders_utils.get_size_for_file(test_file, data_unit='b')
    file_size_k_bytes = files_and_folders_utils.get_size_for_file(test_file, data_unit='kb')
    file_size_m_bytes = files_and_folders_utils.get_size_for_file(test_file, data_unit='mb')
    file_size_g_bytes = files_and_folders_utils.get_size_for_file(test_file, data_unit='gb')
    actual_size_bytes = os.path.getsize(test_file)
    assert file_size_bytes == actual_size_bytes
    assert file_size_k_bytes == actual_size_bytes / 1024 # Conversion Factor
    assert file_size_m_bytes == actual_size_bytes / (1024 * 1024)
    assert file_size_g_bytes == actual_size_bytes / (1024 * 1024 * 1024)

def test_get_files_and_folders_in_dir():
    """
    Testing the os.scanDir module.
    """
    test_dir = os.path.join(TEST_DIR, 'testing_data')
    actual_folders, actual_files = [], []

    for dir_obj in os.scandir(test_dir):
        if dir_obj.is_dir():
            actual_folders.append(dir_obj.path)
        else:
            actual_files.append(dir_obj.path)

    path_to_files = []
    path_to_folders = []

    files, folders = files_and_folders_utils.get_files_and_folders_in_dir(
                                             test_dir)

    for file_entry in files:
        path_to_files.append(file_entry.path)

    for folder_entry in folders:
        path_to_folders.append(folder_entry.path)

    assert path_to_files == actual_files
    assert path_to_folders == actual_folders
