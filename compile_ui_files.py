#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import sys
import os

FILE_LIST=["irregularverbstestgenerator.ui"]

def _compile_ui_file(f):
    file_name = os.path.splitext(os.path.split(f)[1])[0]
    file_path = os.path.split(f)[0]
    subprocess.call(["pyside-uic", "-o", 
                     os.path.join(file_path, "ui_{0}.py".format(file_name)), f])

if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    for f in FILE_LIST:
        _compile_ui_file(os.path.join(root_dir, f))
