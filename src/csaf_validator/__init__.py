#!/usr/bin/env python3
# Author: Omar Santos @santosomar
# This script validates a CSAF JSON document against the Schema

import argparse
import json
import jsonschema
import importlib.resources as pkg_resources
import urllib.request


def validate_json(json_file, use_packaged_schema):
    '''
    Validate a CSAF ROLIE feed JSON file against the Schema
    '''
    # Download the Schema
    schema_url = "https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/csaf_json_schema.json"

    schema = None
    if use_packaged_schema:
        schema = pkg_resources.read_text(__package__, "csaf_strict_json_schema.json")
        schema = json.loads(schema)
    else:
        with urllib.request.urlopen(schema_url) as url:
            schema = json.loads(url.read().decode())

    with open(json_file, encoding='utf-8') as file:
        data = json.load(file)

    # Validate the JSON file against the Schema
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"{json_file} is valid against the CSAF 2.0 Schema.")
    except jsonschema.ValidationError as error:
        print(f"{json_file} is invalid against the CSAF 2.0 Schema.\n{error}")


def main():
    parser = argparse.ArgumentParser(description='Validates a CSAF JSON file against the CSAF 2.0 Schema')
    parser.add_argument('json_file', type=str, help='JSON file to be validated')
    parser.add_argument('--use-packaged-schema', action='store_true', help='Uses an internal copy of csaf_json_schema.json so that no network connection is needed. Note that this copy may be out of date!')
    args = parser.parse_args()

    validate_json(args.json_file, args.use_packaged_schema)


if __name__ == '__main__':
    main()
