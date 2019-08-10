class FlacFile:
  def __init__(self, filename):
    if not filename.endswith(".flac"):
      raise Exception("Invalid File Frmt")

    self.filename = filename

   def play(self):
       print("Playing {} as flac".format(self.filename))
