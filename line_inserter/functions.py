import os
import random
import string


def insertOnFirstLine(insert_line, file_name):
    with open(file_name, "r") as f:
        flines = f.readlines()
        flines.insert(0, insert_line)
        with open(file_name, "w") as f:
            f.writelines(flines)
            f.writelines("\n")


def getListOfFiles(directory_name):
    # create a list of file and sub directories 
    # names in the given directory 
    list_of_file = os.listdir(directory_name)
    all_files = []
    # Iterate over all the entries
    for entry in list_of_file:
        # Create full path
        full_path = os.path.join(directory_name, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(full_path):
            all_files = all_files + getListOfFiles(full_path)
        else:
            all_files.append(full_path)
                
    return all_files


def insertLineInAllFiles(directory_path, line):
    all_files = getListOfFiles(directory_path)
    for file in all_files:
        if file.endswith(".html"):
            # Check and insert statement
            with open(file) as content_file:
                content = content_file.read()
                if line in content:
                    print(f"{file} already contains {line}")
                else:    
                    insertOnFirstLine(line, file) 
