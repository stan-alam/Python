Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.extension):
            raise Exception("Invalid file format")

        self.filename = filename

        
>>> 
>>> class OggFile(AudioFile):
    extension = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))

        
>>> ogg = OggFile("2pac.ogg")
>>> 
>>> ogg.play()
playing 2pac.ogg as ogg
>>> 
