from distutils.core import setup
import py2exe
import os
import sys
import shutil

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
def abs_path(path):
    abspath = os.path.normpath(os.path.join(SCRIPT_PATH, path))
    print(abspath)
    return abspath

path = abs_path("dist/build_win32")
if not os.path.exists(path):
    os.makedirs(path)

setup(
    windows=[abs_path('irregularverbstestgenerator.py')],
    data_files = [abs_path('irv.xls'), abs_path('format.xls')],
    options={'build': {'build_base': abs_path('dist/build')},
        "py2exe":{
            "unbuffered": True,
            "optimize": 2,
            "dist_dir": path  
            }
        }
    )

shutil.rmtree(abs_path("dist/build"))
