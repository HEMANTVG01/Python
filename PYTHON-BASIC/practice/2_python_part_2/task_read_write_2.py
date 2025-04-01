"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

############
import random
import string

def generate_words(num_words=5, word_length=3):
    words = []
    for _ in range(num_words):
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.append(word)
    return words

def write_words_to_files(words):
    with open('file1.txt', 'w', encoding='utf-8') as file1:
        file1.write('\n'.join(words))
    with open('file2.txt', 'w', encoding='cp1252') as file2:
        file2.write(','.join(reversed(words)))

words = generate_words()
write_words_to_files(words)
print("Files written: file1.txt (UTF-8), file2.txt (CP1252)")


########
#file1.txt = knv
byb
vqg
dud
hdd

#file2.txt
hdd,dud,vqg,byb,knv
