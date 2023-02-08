from setuptools import setup, find_packages

setup(
    name='Common Security Advisory Framework (CSAF) Validator',
    version='0.1',
    author='Omar Santos',
    description='This program validates CSAF JSON documents against the CSAF 2.0 schema.',
    packages=find_packages(),
    install_requires=[
        'jsonschema'
    ]
)
