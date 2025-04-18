"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    ...

def remove_duplicated_words(a):
    n = a.split()
    u = []
    for i in n:
        if i not in u:
            u.append(i)
    return ' '.join(u)

if __name__ == "__main__":
    a = 'cat cat dog 1 dog 2'
    r = remove_duplicated_words(a)
    print(r)


print(remove_duplicated_words('cat cat dog 1 dog 2'))
print(remove_duplicated_words('cat cat cat'))
print(remove_duplicated_words('1 2 3'))
