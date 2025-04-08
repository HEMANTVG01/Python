"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse


def print_name_address(args: argparse.Namespace) -> None:
    ...


"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""

import sys
import argparse
from faker import Faker

def generate_fake_data(number_of_instances, fields):
    fake = Faker()
    fake_data = []

    for _ in range(number_of_instances):
        data = {}
        for field, provider in fields.items():
            provider_func = getattr(fake, provider)
            data[field] = provider_func()
        fake_data.append(data)
    
    return fake_data

def main():
    parser = argparse.ArgumentParser(description="Generate fake data.")
    parser.add_argument("number", type=int, help="Number of instances to generate")
    
    parser.add_argument(
        "fields_and_providers", 
        nargs="+", 
        help="Fields and their respective providers (e.g., --name=name --address=address)"
    )
    
    args = parser.parse_args()

    fields = {}
    for field_and_provider in args.fields_and_providers:
        field, provider = field_and_provider.split('=')
        fields[field] = provider

    fake_data = generate_fake_data(args.number, fields)

    for entry in fake_data:
        print(entry)

if __name__ == "__main__":
    main()
