"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    ...

def power_diff(arr):
    n = len(arr)
    r = []
    for i in range(n):
        if i == 0:
            r.append(arr[i]**2)
        else:
            power = arr[i] ** 2
            prev = arr[i-1] ** 2
            diff = power - (prev - arr[i-1])
            r.append(diff)
    return r

if __name__ == "__main__":
    arr = [1,2,3]
    r1 = power_diff(arr)
    print(r1)
