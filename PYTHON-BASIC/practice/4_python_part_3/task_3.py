"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    ...


"""
write tests for is_http_domain function
"""
##solution##
import re

def domain_check(link):
    if re.search("^https", link) or re.search("^http", link) or re.search("$/ ", link):
        return True
    else:
        return False

if __name__ == "__main__":
    print(domain_check('https://ru.wikipedia.org'))
    print(domain_check('https://ru.wikipedia.org/'))
    print(domain_check('griddynamics.com'))
