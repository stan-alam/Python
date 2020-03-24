# 05

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%202A.png" width="80%" height="80%">
</a>

```Python
# codeblock 130.A
import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%202B.png" width="80%" height="80%">
</a>

```Python
# codeblock 131.A
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

class Polygon:
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%202C.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%203A.png" width="80%" height="80%">
</a>

```text
#scrncap 131.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%203B.png" width="80%" height="80%">
</a>

```text
#scrncap 131.B
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%203B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%204.png" width="80%" height="80%">
</a>

```Python
# codeblock 132.A
def __init__(self, points=None):
    points = points if points else []
    self.vertices = []
    for point in points:
        if isinstance(point, tuple):
            point = Point(*point)
        self.vertices.append(point)
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%205.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%206.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%207.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%208A.png" width="80%" height="80%">
</a>

```Python
# codeblock 134.A
class Color:
    def __init__(self, rgb_val, name):
        self.rgb_val = rbg_val
        self.name = name

    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%208B.png" width="80%" height="80%">
</a>

```Python
# codeblock 134.B
#134.B

 c = Color("#ff0000", "bright Red")
 c.get_name()
 c.set_name("red")
 c.get_name()

#>>> 'red'

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%208C.png" width="80%" height="80%">
</a>

```Python
# codeblock 134.C
class Color:
    def __init__(self, rgb_val, name):
        self.rgb_val = rgb_val
        self.name = name

c = Color("#ff0000", "bright red")
print(c.name)
c.name = "red"
print(c.name)

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%208D.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%209.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2010A.png" width="80%" height="80%">
</a>

```Python
# codeblock 135.B
class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid name")

    def _get_name(self):
        return self.name

    name = property(_get_name, _set_name)

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2010B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2011A.png" width="80%" height="80%">
</a>

```Python
# codeblock 136.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2011B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2012.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2013A.png" width="80%" height="80%">
</a>

```Python
# codeblock 137.A
class TomFoolery:
    def _get_tomfoolery(self):
        print("You have engaged in tom foolery")
        return self._tomfoolery

    def _set_tomfoolery(self, value):
        print("Why are you making tom foolery {}".format(value))
        self._silly = value

    def _del_tomfoolery(self):
        print("bye, tom foolery")
        del self._tomfoolery

    tomfoolery = property(_get_tomfoolery, _set_tomfoolery, _del_tomfoolery, "this is a tomfoolery property")
```

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/master/OOP_3x/images/05/Screenshot%20from%202019-09-10%2017-26-26.png" width="50%" height="50%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2013B.png" width="80%" height="80%">
</a>

```Python
# codeblock 137.C
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2014.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2015.png" width="80%" height="80%">
</a>

```Python
# codeblock 138.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2016.png" width="80%" height="80%">
</a>

```Python
# codeblock 139.A
class TomFoolery:
    @property
    def tomfoolery(self):
        "this is a tomfoolery property"
        print("What in Tomfoolery is going on here!?")
        return self.tomfoolery

    @tomfoolery.setter
    def tomfoolery(self, value):
       print ("You are tomfooling yourself {}".format(value))
       self._tomfoolery = value

    @tomfoolery.deleter
    def tomfoolery(self):
       print("You killed tomfoolery")
       del self._tomfoolery

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2017.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2018.png" width="80%" height="80%">
</a>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/lisaPresentation.jpg" width="50%" height="50%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2019.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2020A.png" width="80%" height="80%">
</a>

```Python
# codeblock 140.A
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
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2020B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2021.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2022.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2023.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2024A.png" width="80%" height="80%">
</a>

```Python
#cb 143.A
import sys
import shutil
import zipfile
from pathlib import Path

class ZipReplace:
    def __init__(self, filename, search_strng, replace_strng):
        self.filename = filename
        self.search_strng = search_strng
        self.replace_strng = replace_strng
        self.temp_directory = Path(f"unzipped-{filename}")
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2024B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2025.png" width="80%" height="80%">
</a>

- [ ] Todo - Test this code!

```Python
# cb 144.A
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
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2026.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2027.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2028.png" width="80%" height="80%">
</a>

```Python
# cb 147.A
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

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2029.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2030A.png" width="80%" height="80%">
</a>

```Python
# cb 148.A
class ZipReplace(ZipProssr):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """perform a search & replace all files in the temp dir"""
        for filename in self.temp_dir.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2030B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2031A.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2031B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2032.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2033A.png" width="80%" height="80%">
</a>

```Python
#cb 150.A
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2033B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2034A.png" width="80%" height="80%">
</a>

```Python
#cb 152A
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2034B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2035.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2036.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2037.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2038A.png" width="80%" height="80%">
</a>

```Python
# cb 154
class Character:
    def __init__(self, character,
            bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

def __str__(self):
    bold = "*" if self.bold else ''
    italic = "/" if self.italic else ''
    underline = "_" if self.underline else ''
    return bold + italic + underline + self.character
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2039.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2040.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2041A.png" width="80%" height="80%">
</a>

```Python
#cb 156A
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
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/05/Pyth3oop5%20-%2041B.png" width="80%" height="80%">
</a>
