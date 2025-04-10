"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
############

f1 = open('file1.txt', 'w')
f1.write('23')
f1.close()

f2 = open('file2.txt', 'w')
f2.write('78')
f2.close()

f3 = open('file3.txt', 'w')
f3.write('3')
f3.close()

with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2, open('file3.txt', 'r') as f3:
    r1 = f1.read().strip()
    r2 = f2.read().strip()
    r3 = f3.read().strip()

with open('result.txt', 'w') as final:
    final.write(f"{f1},{f2},{f3}")
