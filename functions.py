import os
import random
import string


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def fillWithText(fileName):
    f = open(fileName, "a")
    for i in range(100):
        f.write("\n")
        f.write(randomString(100))
    f.close()


def insertOnFirstLine(Line1, fileName):
    file1 = open(fileName, "r")
    oline = file1.readlines()
    oline.insert(0, Line1)
    file1.close()
    file1 = open(fileName, "w")
    file1.writelines(oline)
    file1.writelines("\n")
    file1.close()


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def insertLineInAllFiles(directoryPath, line):
    allFiles = getListOfFiles(directoryPath)
    for file in allFiles:
            if file.endswith(".html"):
                # Check and insert statement
                with open(file) as content_file:
                    content = content_file.read()
                    if line in content:
                        print(file + " already contains " + line)
                    else:    
                        insertOnFirstLine(line, file) 
