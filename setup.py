from setuptools import setup, find_packages

setup(
    name='code_evaluator',
    version='0.1',
    description='''A command line tool to generate code statistics for a given directory.
    These statistics include
    1. Total Lines of Code.
    2. Percentage wise break up of different languages used.''',
    author='Abhinav Shaw',
    author_email='abhinavshaw@umass.edu',
    packages = find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
    'console_scripts' : ['evaluate=code_evaluator.cli:generate_code_statistics']
    },
    include_package_data = True,
    zip_safe = False
)
