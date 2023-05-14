import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Get the current directory
folder_path = os.getcwd()

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter the files to include only Python files
python_files = [file for file in files if file.endswith(".py")]

def open_python_file(file):
    file_path = os.path.join(folder_path, file)
    subprocess.run(["python", file_path])

# Create a thread pool
with ThreadPoolExecutor() as executor:
    # Submit tasks to the thread pool for each Python file
    for file in python_files:
        executor.submit(open_python_file, file)