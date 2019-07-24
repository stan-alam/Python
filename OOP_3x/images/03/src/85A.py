# Code block 85.A

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.extension):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    extension = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    extension = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    extension = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))
