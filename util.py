# util.py - some utility functions for the main program

import os
from pathlib import Path
from sys import platform
import get_logger from logger

log = get_logger('util.py')

def delete_file(file_path):
    file_path_object = Path(file_path)

    if not file_path_object.exists():
        return
    
    if not file_path_object.is_file():
        return

    # attempt to delete
    try:
        file_path_object.unlink()
    except FileNotFound as e:
        pass
    except:
        log.error(f'Failed to delete file at path {file_path} with error: {sys.exc_info()[0]}')
        