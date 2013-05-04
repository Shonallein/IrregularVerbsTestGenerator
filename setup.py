from distutils.core import setup
import py2exe
 
setup(
    windows=['irregularverbstestgenerator.py'],
    data_files = ['irv.xls', 'format.xls'],
    options={
        "py2exe":{
            "unbuffered": True,
            "optimize": 2,
            }
        }
    )
