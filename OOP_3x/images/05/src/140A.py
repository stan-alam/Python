from urlib.request import urlopen

class WebApp:
    def __init__(self, url):
        self.url = url
        self._content = None
    
    @property
    def content(self):
        if not self._content:
            print("Retrieving Web Page ... ")
        self._content = urlopen(self.url).read()
        return self.content      
