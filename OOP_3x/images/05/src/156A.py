def home(self):
    while self.document.characters[
            self.position-1].character != '\n':
         self.position -= 1
         if self.position == 0:
         # go to begin of file before  /n
             break

def end(self):
    while self.position < len (
            self.document.characters) and \
            self.document.characters[
                    self.position
                    ].character != '\n':
            self.position += 1
