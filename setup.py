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
