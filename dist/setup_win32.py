from distutils.core import setup
import py2exe
import os
import sys
import shutil

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(SCRIPT_PATH, "build_win32")
if not os.path.exists(path):
    os.makedirs(path)

setup(
    windows=[os.path.join(SCRIPT_PATH, '../irregularverbstestgenerator.py')],
    data_files = [os.path.join(SCRIPT_PATH, '../irv.xls'), os.path.join(SCRIPT_PATH, '../format.xls')],
    options={'build': {'build_base': os.path.join(SCRIPT_PATH, 'build')},
        "py2exe":{
            "unbuffered": True,
            "optimize": 2,
            "dist_dir": path  
            }
        }
    )

shutil.rmtree(os.path.join(SCRIPT_PATH, "build"))
