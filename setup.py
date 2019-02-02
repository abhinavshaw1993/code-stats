from setuptools import setup, find_packages

setup(
    name='codestat',
    version='0.1',
    description='''A command line tool to generate code statistics for a given directory.
    These statistics include
    1. Total Lines of Code.
    2. Percentage wise break up of different languages used.''',
    author='Abhinav Shaw',
    author_email='abhinavshaw@umass.edu',
    packages=find_packages(),
    install_requires=[
        'click',
        'os',
        'pathlib',
        'sys'
    ],
    setup_requires=[
        "pytest-runner",
    ],
    test_requires=[
        'pytest',
    ],
    setup_requires=[
        "pytest-runner",
    ],
    test_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts' : ['codestat=code_stat.cli:generate_code_statistics']
    },
    include_package_data=True,
    zip_safe=False,
    setup_cfg=True
)
