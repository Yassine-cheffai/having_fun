"""
return all files paths inside a given directory
a function should take a folder path and return all files paths relative to the initial path
consider a folders structures as a tree, each node can be a folder or a file, 
if it's a folder add the files and do the same to the folders
"""

from typing import Tuple, List
import os


def retreive_files(path: str) -> Tuple[List, List]:
    all_files = []
    all_directories = []
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            all_files.append(file_path)
        for name in directories:
            dir_path = os.path.join(root, name)
            all_directories.append(dir_path)

    return all_files, all_directories


print(retreive_files(os.getcwd())[0])
