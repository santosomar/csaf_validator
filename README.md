![Python versions](https://img.shields.io/pypi/pyversions/danger-python)

# CSAF Validator
A Python-based program used to validate a Common Security Advisory Framework (CSAF) JSON file against the CSAF 2.0 schema.

## Requirements
- Python 3
- `jsonschema` library

```
pip install -r requirements.txt
```

## Usage:

```
usage: csaf_validator.py [-h] json_file

Validates a CSAF JSON file against the CSAF 2.0 Schema

positional arguments:
  json_file   JSON file to be validated

optional arguments:
  -h, --help  show this help message and exit
  ```
  
 Example:
 
 ```
 $ python3 csaf_validator2.py cisco-sa-iox-8whGn5dL.json
 cisco.json is valid against the CSAF 2.0 Schema.
 ```

## How the Script Works
The script performs the following steps:

- Downloads the CSAF 2.0 JSON Schema from the URL https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/csaf_json_schema.json and saves it to a local file named csaf_json_schema.json.
- Loads the CSAF 2.0 JSON Schema from the local file.
- Loads the JSON file to be validated.
- Validates the JSON file against the CSAF 2.0 JSON Schema using the jsonschema library.

If the validation is successful, the script prints a message indicating that the JSON file is valid against the CSAF 2.0 Schema. If the validation fails, the script prints an error message indicating that the JSON file is invalid against the CSAF 2.0 Schema, along with the validation error.

## Additional Information
The `jsonschema` library is used to perform the JSON schema validation. JSON schema is a standard for describing the structure of JSON data, and the jsonschema library provides an implementation of this standard for Python.

The script uses the `argparse` library to allow the JSON file to be passed as a command-line argument. This makes it easy to use the script in a variety of contexts, such as from the command line, from within another script, or from a scheduling tool. The argparse library also provides automatic documentation of the command-line arguments, making the script easier to use for others who may not be familiar with it.