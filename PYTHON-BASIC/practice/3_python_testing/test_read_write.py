"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""


import pytest
import tempfile
import os
from p2task4 import extract_values_and_write 


@pytest.fixture
def temp_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        filenames = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
        file_contents = {
            'file1.txt': 'content1',
            'file2.txt': 'content2',
            'file3.txt': '',  
            'file4.txt': 'content4'
        }
        for filename, content in file_contents.items():
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write(content)
        yield temp_dir, filenames


def test_extract_values_and_write(temp_files):
    temp_dir, filenames = temp_files
    extracted_values = extract_values_and_write(directory_path=temp_dir)
    expected_values = ['content1', 'content2', 'content4']
    assert extracted_values == expected_values, f"Expected {expected_values}, but got {extracted_values}"
    result_file_path = os.path.join(temp_dir, 'result.txt')
    assert os.path.exists(result_file_path), "result.txt was not created."

    with open(result_file_path, 'r') as result_file:
        result_content = result_file.read().strip()
        expected_result_content = ', '.join(expected_values)
        assert result_content == expected_result_content, f"Expected result content {expected_result_content}, but got {result_content}"


def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        extracted_values = extract_values_and_write(directory_path=temp_dir)
    assert extracted_values == [], "Expected no values to be extracted from an empty directory."


def test_directory_with_only_empty_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        filenames = ['empty1.txt', 'empty2.txt', 'empty3.txt']
        for filename in filenames:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('')

        extracted_values = extract_values_and_write(directory_path=temp_dir)
    assert extracted_values == [], "Expected no values to be extracted from empty files."


def test_write_to_custom_output_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        filenames = ['file1.txt', 'file2.txt']
        file_contents = {
            'file1.txt': 'content1',
            'file2.txt': 'content2'
        }
        for filename, content in file_contents.items():
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write(content)
        custom_output_file = os.path.join(temp_dir, 'custom_result.txt')
        extracted_values = extract_values_and_write(directory_path=temp_dir, output_file=custom_output_file)
        expected_values = ['content1', 'content2']
        assert extracted_values == expected_values, f"Expected {expected_values}, but got {extracted_values}"
        assert os.path.exists(custom_output_file), "Custom output file was not created."

        with open(custom_output_file, 'r') as result_file:
            result_content = result_file.read().strip()
            expected_result_content = ', '.join(expected_values)
            assert result_content == expected_result_content, f"Expected result content {expected_result_content}, but got {result_content}"

