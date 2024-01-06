from shutil import rmtree
from os import makedirs
from os.path import isdir


def make_new_dir(folder):
    if isdir(folder):
        rmtree(folder)
        
    makedirs(folder)
