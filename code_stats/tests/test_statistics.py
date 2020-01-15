import os
import pytest
import code_stats.bin.statistics as statistics

from collections import Counter
from code_stats.bin.logger import Logger

TEST_DIR = os.path.dirname(__file__)
kTestingDataDir = os.path.join(TEST_DIR, 'testing_data')
kExtensionListPath = os.path.join(TEST_DIR, "../data/default_ext_list.yml")

@pytest.fixture
def setup_logger():
    # Instantiating logging object.
    logger = Logger()
    logger.set_verbosity(False, 0)

def test_evaluate_lines_of_code(setup_logger):
    # Dont' Ignore Blanks. ignore ".pyc".
    total_lines_1, lines_of_code_per_lang_1 = statistics.evaluate_lines_of_code(
                                      kTestingDataDir,
                                      kExtensionListPath,
                                      ignore_blank_lines=False,
                                      ignore_extensions=["pyc"])
    actual_total_lines_1 = 18
    actual_lines_of_code_per_lang_1 = Counter({"Python": 7, "JSON": 11})
    assert actual_total_lines_1 == total_lines_1
    assert actual_lines_of_code_per_lang_1 == lines_of_code_per_lang_1

    # Ignore Blanks. ignore extensions ".pyc"
    total_lines_2, lines_of_code_per_lang_2 = statistics.evaluate_lines_of_code(
                                      kTestingDataDir,
                                      kExtensionListPath,
                                      ignore_blank_lines=True,
                                      ignore_extensions=["pyc"])
    actual_total_lines_2 = 16
    actual_lines_of_code_per_lang_2 = Counter({"Python": 5, "JSON": 11})
    assert actual_total_lines_2 == total_lines_2
    assert actual_lines_of_code_per_lang_2 == lines_of_code_per_lang_2

    # Dont' Ignore Blanks. ignore extensions ".pyc, .json"
    total_lines_3, lines_of_code_per_lang_3 = statistics.evaluate_lines_of_code(
                                      kTestingDataDir,
                                      kExtensionListPath,
                                      ignore_blank_lines=False,
                                      ignore_extensions=["pyc", ".json"])
    actual_total_lines_3 = 7
    actual_lines_of_code_per_lang_3 = Counter({"Python": 7})
    assert actual_total_lines_3 == total_lines_3
    assert actual_lines_of_code_per_lang_3 == lines_of_code_per_lang_3

def test_evaluate_percentage_of_code(setup_logger):
    # Dont' Ignore Blanks. ignore ".pyc".
    total_lines_1, lines_of_code_per_lang_1 = statistics.evaluate_lines_of_code(
                                      kTestingDataDir,
                                      kExtensionListPath,
                                      ignore_blank_lines=False,
                                      ignore_extensions=["pyc"])
    percentage_of_code_1 = statistics.evaluate_percentage_of_code(total_lines_1,
                                                                lines_of_code_per_lang_1)
    actual_total_lines_1 = 18
    actual_lines_of_code_per_lang_1 = Counter({"Python": 7, "JSON": 11})
    actual_percentage_of_code_per_lang_1 = {"Python" : 7/18 *100,
                                            "JSON": 11/18 *100}

    assert actual_percentage_of_code_per_lang_1 == percentage_of_code_1

def test_evaluate_sizes(setup_logger):
    total_size, size_per_language = statistics.evaluate_sizes(kTestingDataDir,
                                                              kExtensionListPath,
                                                              data_unit="b",
                                                              ignore_extensions=["pyc"])
    actual_total_size_bytes = 405
    actual_size_per_language = {"Python" : 163.0, "JSON" : 242.0}

    assert actual_total_size_bytes == total_size
    assert actual_size_per_language == size_per_language

def test_generate_stats(setup_logger):
    actual_header = ['Language', 'Lines of Code', '% of Code', 'Size in b']
    actual_output = [['JSON', 11, 61.111111111111114, 242.0],
                    ['Python', 7, 38.88888888888889, 163.0],
                    ['Total', 18, 100.0, 405.0]]

    header, output = statistics.generate_stats(kTestingDataDir)
    print(output)

    assert all([True if row in output else False for row in actual_output])
    assert actual_header == actual_header
