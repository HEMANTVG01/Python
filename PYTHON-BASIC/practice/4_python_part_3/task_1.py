"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime


def calculate_days(from_date: str) -> int:
    ...


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""

import datetime

class WrongFormatException(Exception):
    pass

def calculate_days(date_str):
    try:
        custom_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.date.today()
        delta = custom_date - current_date
        return delta.days
    
    except ValueError:
        raise WrongFormatException(f"Date format must be 'YYYY-MM-DD'")

print(calculate_days('2021-10-07'))  
print(calculate_days('2021-10-05'))  
print(calculate_days('10-07-2021'))  
