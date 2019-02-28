from setuptools import setup, find_packages

setup(
    name='code-stats',
    version='0.1',
    description='''A command line tool to generate code statistics for a given directory.
    These statistics include\n
    1. Total Lines of Code.\n
    2. Percentage wise break up of different languages used.''',
    author='Abhinav Shaw',
    author_email='abhinav.shaw1993@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'pathlib',
    ],
    setup_requires=[
        "pytest-runner",
    ],
    test_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts' : ['codestats=code_stats.cli:generate_code_statistics']
    },
    url="https://github.com/abhinavshaw1993/code-stats",
    classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux"
                    ],
    include_package_data=True,
    zip_safe=False,
    setup_cfg=True
)
