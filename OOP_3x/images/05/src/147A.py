import sys
import shutil
import zipfile
from pathlib import Path

class ZipProcssr:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_dir = Path(f"unzipped-{zipname[:-4]}")
        
     def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()
     
     def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(self.temp_dir)
     
     def zip_files(self):
        with zipfile.ZipFile(self.zipname, "w") as file:
            for filename in self.temp_dir.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_dir)
