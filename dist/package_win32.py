#!/usr/bin/python
# -*- coding: utf-8 -*-

"""\
Packaging script for win32 plateform
"""

import os
import sys
import subprocess
import shutil

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

def main():
   cmd = ['C:\\Python27\\python.exe', os.path.join(SCRIPT_PATH, '../setup_win32.py'), 'py2exe']
   subprocess.call(cmd)
   cmd = ['C:\\Program Files (x86)\\Inno Setup 5\\ISCC.exe', '/dDistRoot='+os.path.join(SCRIPT_PATH, "build_win32"), '/o'+SCRIPT_PATH, os.path.join(SCRIPT_PATH,'win_installer.iss')]
   subprocess.call(cmd)
   #shutil.rmtree(os.path.join(SCRIPT_PATH, "build_win32"))

if __name__ == '__main__':
    main()
