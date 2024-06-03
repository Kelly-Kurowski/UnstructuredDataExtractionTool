import os
import random
import shutil

# Specify the directory paths
source_directory = r"C:\Users\kelly\OneDrive\Bureaublad\Generated Fake Resumes"
destination_directory = r"C:\Users\kelly\OneDrive\Bureaublad\40 resumes for information retrieval"

# Get a list of all files in the source directory
files = os.listdir(source_directory)

# Shuffle the list of files randomly
random.shuffle(files)

selected_files = files[:40]

# Move the selected files to the destination directory
for file_name in selected_files:
    source_path = os.path.join(source_directory, file_name)
    destination_path = os.path.join(destination_directory, file_name)
    shutil.move(source_path, destination_path)
    print(f"Moved '{file_name}' to '{destination_directory}'")
