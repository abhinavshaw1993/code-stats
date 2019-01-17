from setuptools import setup, find_packages

setup(
    name='code_evaluator',
    version='0.1',
    description='''A command line tool to generate code statistics for a given directory.
    These statistics include
    1. Total Lines of Code.
    2. Total number of files.
    3. Percentage wise break up of different languages used.''',
    author='Abhinav Shaw',
    author_email='abhinavshaw@umass.edu',
    packages = find_packages(exclude=("tests")),
    install_requires=[
        'click',
    ],
    entry_points={
    'console_scripts' : ['evaluate=code_evaluator.app:generate_code_statistics']
    },
    package_data = {
    'app' : ['default_file_ext_list.yaml']
    },
    zip_safe = False
)
