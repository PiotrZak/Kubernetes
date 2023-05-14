import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Get the current directory
current_directory = os.getcwd()

# Define the path to the models folder
models_directory = os.path.join(current_directory, "models")

# Filter the files to include only Python files
python_files = [file for file in models_directory if file.endswith(".py")]

def open_python_file(file):
    file_path = os.path.join(folder_path, file)
    subprocess.run(["python", file_path])

# Create a thread pool
with ThreadPoolExecutor() as executor:
    # Submit tasks to the thread pool for each Python file
    for file in python_files:
        executor.submit(open_python_file, file)