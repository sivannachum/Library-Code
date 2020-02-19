import os
from pathlib import Path
import time
import csv
from datetime import datetime

# Hard drive directory
start_path = Path(r'D:')
#start_path = Path(r'C:\Users\specialcollections\Desktop\Working_folder_specasst\HD')

# Open the CSV file where we will save the data
with open('test.csv','a', encoding='utf-8', newline = '') as f:
    # Create a writer object from csv module
    writer = csv.DictWriter(f, fieldnames=["File Path", "Name", "Last Modified", "Created"])
    # Write the header of the CSV file
    writer.writeheader()

    # Walk through all the paths, directories, and files in the start_path
    for path, dirs, files in os.walk(start_path):
        # Skip hidden paths
        dirs[:] = [d for d in dirs if not d[0] == '.']
        # For each directory, get its path, name, last modified date, and created date
        for dir in dirs:
            # File path
            directory_name = path
            # Folder name
            folder_name = dir
            # Last modified, m = modified
            last_modified = time.ctime(os.path.getmtime(os.path.join(path, dir)))
            # Date created, c = created
            # Avoid OS errors
            try:
                created = time.ctime(os.path.getctime(os.path.join(path, dir)))
            except OSError:
                created = "N/A"
            # Add the information for this directory as the last row in the csv file
            writer.writerow({"File Path": directory_name, "Name": folder_name, "Last Modified": last_modified, "Created": created})
# Let us know that we've finished
print("Done")