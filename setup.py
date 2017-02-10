import sys
from cx_Freeze import setup, Executable

setup(
    name = "Stardust",
    version = "2.7",
    description = "Stardust pygame",
    executables = [Executable("stardust.py", base = "Win32GUI")])