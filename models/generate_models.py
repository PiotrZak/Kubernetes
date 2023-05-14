import os
import subprocess
import concurrent.futures

# Get the current directory
current_directory = os.getcwd()

print(current_directory)

# Filter the files to include only Python files
python_files = [file for file in os.listdir(current_directory) if file.endswith(".py") and file != "generate_models.py"]

print ("ML Models:", python_files)

def open_python_file(file):
    file_path = os.path.join(current_directory, file)
    result = subprocess.run(["python3", file_path], capture_output=True, text=True)

# Create a thread pool
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit tasks to the thread pool for each Python file
    futures = []
    for file in python_files:
        print('Generating', file, 'model')
        future = executor.submit(open_python_file, file)
        futures.append(future)

    # Retrieve results from the futures
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            print(result)
            # Process the result as needed
        except Exception as e:
            # Handle exceptions raised by the task
            print(f"An exception occurred: {type(e).__name__}: {e}")