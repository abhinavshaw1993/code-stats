from setuptools import setup

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
    py_modules=['code_evaluator'],
    scripts=['utils.py', 'statistics.py'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        evaluate=code_evaluator:generate_code_statistics
    ''',
)
