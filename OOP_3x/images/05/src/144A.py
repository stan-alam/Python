# 144.A
def unzip_files(self):
    self.temp_directory.mkdir()
    with zipfile.ZipFile(self.filename) as zip:
        zip.extractall(self.temp_directory)

def find_replace(self):
    for fielname in self.temp_directory.iterdir():
        with filename.open() as file:
            contents = file.read()
        contents = contents.replace(self.search_string, self.replace_string)
        with filename.open("w") as filename:
            filename.write(contents)

def zip_files(self):
    with zipfile.ZipFile(self.filename, "w") as file:
        for filename in self.temp_directory.iterdir():
            file.write(filename, filename.name)
    shutil.rmtree(self.temp_directory)

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()
