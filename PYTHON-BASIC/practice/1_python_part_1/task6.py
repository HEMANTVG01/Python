"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    ...

def get_min_max(filename):
    min_val = float('inf') 
    max_val = float('-inf')
    with open(filename) as opened_file:
        for line in opened_file:
            num = int(line.strip())
            min_val = min(min_val, num)
            max_val = max(max_val, num)
    return (min_val, max_val)

print(get_min_max('/Users/hhemantvg/Documents/Python_Module1_Tasks/Python_part_1/file.txt'))
