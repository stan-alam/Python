#286.A

class File:
    def __init__(self, name):
        self.name = name

class Dir(File):
    def __init__(self, name):
        super().__init__name(name)
        self.children = []

root = Dir("")
etc = Dir("etc")
root.children.append(etc)
etc.children.append(File("password"))
etc.children.append(File("groups"))
httpd = Dir("httpd")
etc.children.append(httpd)
httpd.children.append(file("http.conf"))
var = Dir("var")
root.children.append(var)
log = Dir("log")
var.children.append(log)
log.children.append(File("messages"))
log.children.append(File("kernal"))
