import os
from random import randint


OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list):
    pass


def func2(result_file: str):
    pass


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)

#####

import os
import csv
import concurrent.futures

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def write_fibonacci_to_files(indices, folder_path):
    def write_fibonacci(index):
        fib_value = fibonacci(index)
        with open(os.path.join(folder_path, f"{index}.txt"), 'w') as f:
            f.write(str(fib_value))
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(write_fibonacci, indices)

def create_csv_from_files(folder_path, output_csv_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            index = int(filename.split('.')[0])  
            with open(os.path.join(folder_path, filename), 'r') as f:
                fib_value = int(f.read().strip())
                data.append([index, fib_value])
    data.sort()

    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    indices = [5, 1, 8, 10]
    folder_path = "fibonacci_files"  
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    write_fibonacci_to_files(indices, folder_path)

    create_csv_from_files(folder_path, "fibonacci_values.csv")
