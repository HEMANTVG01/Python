"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import pytest

def test_file_creation_and_result():
    with open('file1.txt', 'w') as f1:
        f1.write('23')
    with open('file2.txt', 'w') as f2:
        f2.write('78')
    with open('file3.txt', 'w') as f3:
        f3.write('3')

    with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2, open('file3.txt', 'r') as f3:
        r1 = f1.read().strip()
        r2 = f2.read().strip()
        r3 = f3.read().strip()

    with open('result.txt', 'w') as final:
        final.write(f"{r1},{r2},{r3}")

    with open('result.txt', 'r') as result_file:
        result_content = result_file.read().strip()
        assert result_content == "23,78,3"
