from PIL import Image

class ScaleZip(ZipProcessor):
    def process_files(self):
    '''Scale images in the dir to 640x480'''
    for fielname in self.temp_directory
