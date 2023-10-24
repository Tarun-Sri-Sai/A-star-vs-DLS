import shutil
import os


def make_new_dir(folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
