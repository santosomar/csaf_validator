# CSAF Validator
A Python-based program used to validate a Common Security Advisory Framework (CSAF) JSON file against the CSAF 2.0 schema.

## Requirements
- Python 3
- `jsonschema` library

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
