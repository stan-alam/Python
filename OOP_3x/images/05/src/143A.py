import sys
import shutil
import zipfile
from pathlib import Path

class ZipReplace:
    def __init__(self, filename, search_strng, replace_strng):
        self.filename = filename
        self.search_strng = search_strng
        self.replace_strng = replace_strng
        self.temp_directory = Path(f"unzipped-{filename}")
