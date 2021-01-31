import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("Tube-Downloader.py", base=base)]

setup(
    name="Tube-Downloader",
    version="beta-0.1",
    description="Lightweight Application For Downloding YouTube Videos.",
    executables=executables,
)
