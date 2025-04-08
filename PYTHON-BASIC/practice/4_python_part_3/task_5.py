"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple


def make_request(url: str) -> Tuple[int, str]:
    ...


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
import urllib.request

def make_request(url):
    with urllib.request.urlopen(url) as response:
        status_code = response.getcode()
        data = response.read().decode('utf-8')
        return status_code, data

url = "https://example.com"
status_code, data = make_request(url)
print(f"Status Code: {status_code}")
print(f"Response Data: {data[:200]}...")  # Print first 200 characters of the response
