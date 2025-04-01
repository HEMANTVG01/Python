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


import os

def extract_values_and_write():
    directory_path = '/Users/hhemantvg/Documents/Python/Python_task_2/files'
    values = []
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as file:
                    content = file.read().strip() 
                    if content:  
                        values.append(content)
            except Exception as e:
                print(f"Error reading file {filename}: {e}")

    with open('result.txt', 'w') as result_file:
        result_file.write(', '.join(values))
    
    return values 

extracted_values = extract_values_and_write()
print("Extracted values:", ', '.join(extracted_values))
