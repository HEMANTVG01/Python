"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

######
import tempfile
import os

def test_write_files_with_encodings():
    input_data = ['abc', 'def', 'xyz']

    with tempfile.TemporaryDirectory() as tmpdir:
        utf_path = os.path.join(tmpdir, 'utf.txt')
        cp_path = os.path.join(tmpdir, 'cp.txt')

        with open(utf_path, 'wb') as f1:
            for item in input_data:
                f1.write(item.encode('utf-8'))

        with open(cp_path, 'wb') as f2:
            for item in input_data:
                f2.write(item.encode('CP1252') + b',')

        with open(utf_path, 'rb') as f1:
            utf_content = f1.read()
        assert utf_content == b'abcdefxyz'

        with open(cp_path, 'rb') as f2:
            cp_content = f2.read()
        assert cp_content == b'abc,def,xyz,'
