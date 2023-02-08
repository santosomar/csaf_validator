# CSAF Validator
A Python-based program used to validate a Common Security Advisory Framework (CSAF) JSON file against the CSAF 2.0 schema.

## How to Use It:

```
usage: csaf_validator2.py [-h] json_file

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
