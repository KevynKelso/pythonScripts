#!/usr/local/bin/python3
import sys
from functions import insertLineInAllFiles


def start(directory_path):
    span_line_1 = "<span class=\"remove-page-title\"></span>"
    insertLineInAllFiles(directory_path, span_line_1)


if __name__ == "__main__":
    directory_path = sys.argv[1] 
    start(directory_path)
    
