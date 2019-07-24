# Code block 85.A

class AudioFile:
  def __init__(self, filename):
    if not filename.endswith(self.extension):
      raise Exception("invalid file format")

      self.filename = filename

class Mp3File(AudioFile):
  extension ="mp3"

  def play(self):
    print("play { } as mp3".format(self.filename))

class WavFile(AudioFile):
  extension = "wav"

  def play(self):
    print("play { } as wav".format(self.filename))

class OggFile(AudioFile):
  extension = "oog"

  def play(self):
    print("play { } as ogg".format(self.filename))
