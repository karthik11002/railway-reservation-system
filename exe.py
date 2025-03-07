import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base,icon="icon.ico")]

cx_Freeze.setup(
    name = "JDK",
    options = {"build_exe": {"packages":["tkinter","os","sys"], "include_files":['tcl86t.dll','tk86t.dll','icon.ico','photos']}},
    version = "1.00",
    description = "JDK",
    executables = executables
    )
