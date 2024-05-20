import os
import random
import shutil

# Specify the directory paths
source_directory = r"C:\Users\kelly\OneDrive\Bureaublad\Inkoop Facturen labSC OCR Adobe"
destination_directory = r"C:\Users\kelly\OneDrive\Bureaublad\Randomly selected 200 invoices"

# Get a list of all files in the source directory
files = os.listdir(source_directory)

# Shuffle the list of files randomly
random.shuffle(files)

# Select the first 200 files (or fewer if there are fewer than 100 files)
selected_files = files[:200]

# Move the selected files to the destination directory
for file_name in selected_files:
    source_path = os.path.join(source_directory, file_name)
    destination_path = os.path.join(destination_directory, file_name)
    shutil.move(source_path, destination_path)
    print(f"Moved '{file_name}' to '{destination_directory}'")
