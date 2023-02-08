from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='csaf_validator',
    version='1.0.0',
    author='Omar Santos',
    description='This program validates CSAF JSON documents against the CSAF 2.0 schema.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'jsonschema'
    ]
)

setup(
    name='csaf_validator',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/santosomar/csaf_validator',
    license='MIT',
    author='Omar Santos',
    description='A package to validate CSAF JSON files against the CSAF 2.0 Schema',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'jsonschema',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'csaf_validator=csaf_validator:main'
        ]
    }
)