"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    ...

def build_from_unique_words(*lines, word_number):
    result = []
    for line in lines:
        words = list(dict.fromkeys(line.split()))
        if word_number < len(words):
            result.append(words[word_number]) 
    return ' '.join(result) 

if __name__ == "__main__":
    r1 = build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    print(r1)
    r2 = build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    print(r2)
    r3 = build_from_unique_words('1 2', '1 2 3', word_number=10)
    print(r3)
    r4 = build_from_unique_words(word_number=10)
    print(r4)
