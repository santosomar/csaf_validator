#!/usr/bin/env python3
# Author: Omar Santos @santosomar
# This script validates a CSAF JSON document against the Schema

import argparse
import json
import jsonschema
import urllib.request

def validate_json(json_file):
    '''
    Validate a CSAF ROLIE feed JSON file against the Schema
    '''
    # Download the Schema
    schema_url = "https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/csaf_json_schema.json"
    
    with urllib.request.urlopen(schema_url) as url:
    # Read the Schema file and save it locally
        schema_data = url.read().decode()
        with open('csaf_json_schema.json', 'w') as schema_file:
            schema_file.write(schema_data)

    # Load the Schema
    with open('csaf_json_schema.json') as schema_file:
        schema = json.load(schema_file)

    with open(json_file) as file:
        data = json.load(file)

    # Validate the JSON file against the Schema
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"{json_file} is valid against the CSAF 2.0 Schema.")
    except jsonschema.ValidationError as error:
        print(f"{json_file} is invalid against the CSAF 2.0 Schema.\n{error}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validates a CSAF JSON file against the CSAF 2.0 Schema')
    parser.add_argument('json_file', type=str, help='JSON file to be validated')
    args = parser.parse_args()
    validate_json(args.json_file)
