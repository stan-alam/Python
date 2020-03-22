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

 **06**

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%201.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%202.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%203.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%204.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%205.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%206.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%207.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%208.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%209.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2010.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2011.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2012.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2013A.png" width="80%" height="80%">
</a>

```Python
#cb 164.A
from dataclasses import make_dataclass
Stonk = make_dataclass("Stonk", "symbol", "current", "high", "low")
stonk = Stonk("IBM", 180.00, high = 192.31, low = 68.00)
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2013B.png" width="80%" height="80%">
</a>

```Python
#cb 165.A
class StonkRegularClass
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low

stonk_regular_class = Stonk("IBM", 189.00, high = 200.00, low = 183.00)

```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2014A.png" width="80%" height="80%">
</a>

```Python
#screenshot
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2014B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2015.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2016.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2017.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2018.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2019.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2020.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2021.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2022.png" width="80%" height="80%">
</a>

```Python
# 171.A
random_keys = { }
random_keys["astring"] = "whatever"
random_keys[5] = "an_int"
random_keys[42.0] = "floats_are_good"
random_keys[("xyz", "456")] = "groovy tuples"

class AwesomeObj:
    def __init__(self, avalue):
        self.avalue = avalue

my_obj = AwesomeObj(14)
random_keys[my_obj] = "We can store objects!"
my_obj.avalue = 13
try:
    random_keys[[1,2,3]] = "Sorry we can't store lists"
except:
    print("unable to store lists\n")

for key, value in random_keys.items():
    print ("{} has value {}".format(key, value))
```

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/src/scrncap171A.png" width="80%" height="80%">
</p>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2023.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2024.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2025.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2026.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2027.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2028.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2029.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2030.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2031.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2032A.png" width="80%" height="80%">
</a>

```Python
#cb 174.A - scrncap 174.B
from collections import defaultdict


num_items = 0

def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])

d = defaultdict(tuple_counter)

```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2032B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2033.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2034.png" width="80%" height="80%">
</a>

```Python
# 175.A
from collections import Counter

responses = [
    "bepsi",
    "stonks",
    "sheck"
]

print("they voted for {} meme_grammar".format (
Counter(responses).most_common(1)[0][0]
    )
)
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2035.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2036.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2037.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2038.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2039.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2040.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2042.png" width="80%" height="80%">
</a>

```Python
# 179.A
class Sortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return f"{self.string}:{self.number}"
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2043.png" width="80%" height="80%">
</a>

```Python
# 180.A
from functools import total_ordering

@total_ordering
class Sortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
    	return f"{self.string}:{self.number}"

def __eq__(self, object):
    return all((
    self.string == object.string,
    self.number == object.number,
    self.sort_num == object.number
    ))
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2044.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2045A.png" width="80%" height="80%">
</a>

```python
# 181.A
#181.A
from operator import itemgetter

l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 21)]
```

```text   
screencap 181.A
```

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/src/181A.png" width="80%" height="80%">
</p>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2045B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2046A.png" width="80%" height="80%">
</a>

```Python
# 181.B
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2046B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2047A.png" width="80%" height="80%">
</a>

```scrncap
182.A
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2047B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2048A.png" width="80%" height="80%">
</a>

```ScreenCap
182.b
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2048B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2049.png" width="80%" height="80%">
</a>

```Python
#183.A
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2050.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2051A.png" width="80%" height="80%">
</a>

```Python
#184.A
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2051B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2052.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2053.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2054.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2055.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2056.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2057A.png" width="80%" height="80%">
</a>

```python
#cb - 187.A - 187.B
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2057B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2058.png" width="80%" height="80%">
</a>

```html
<html>
  <body>
    <a href="contactme.html">Contact Me!</a>
    <a href="weblog.html">Checkout my cool blog</a>
    <a href="doge.html">My Doge"<a/>
    <a href="myhobbies.html">Guitar stuff</a>
    <a href="https://ghostfish.io">"Stay groovy"</a>
  <body>
</html>
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2059A.png" width="80%" height="80%">
</a>

```text
ScreenCap 189.A

```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2059B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2060.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2061.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2062A.png" width="80%" height="80%">
</a>

- [ ] Todo - Test this code!

```python
#cb 190.A
class LinkCollector:
    def __init__(self, url):
        self.url = "http://+" + "urlparse(url).netloc
        self.collected_links = set()
        self.visited_links = set()

    def collect_links(self, path="/"):
    full_url = self.url + path
    self.visited_links.add(full_url)
    page = str(urlopen(full_url).read())
    links = LINK_REGEX.findall(page)
    links = {self.normalize_url(path, link ) for link in links}
    self.collected_links = links.union(
        self.collected_links)
    unvisted_links = links.difference(
        self.visited_links)
    print(links, self.visited_links, self.collected_links, unvisited_links)

```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2062B.png" width="80%" height="80%">
</a>

```Python
# cb 192.A
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2063A.png" width="80%" height="80%">
</a>

```text
#scrncap 190.A
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2063B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2064.png" width="80%" height="80%">
</a>

- [ ] Todo - Test this code!

```python
#cb 193.A
from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys
from queue import Queue
LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

class LinkCollector:
    def __init__(self, url):
        self.url = "http://%s" % urlparse(url).netloc
        self.collected_links = { }
        self.visisted_links = set()

    def collect_links(self):
        queue = Queue()
        queue.put(self.url)
        while not queue.empty():
            url = queue.get().rstrip('/')
            self.visited_links.add(url)
            page = str(urlopen(url).read())
            links = LINK_REGEX.findall(page)
            links = {
                self.normalize_url(urlparse(url).path, link)
                for link in links
            }
            self.collected_links[url] = links
            for link in links:
                self.collected_links.setdefault(link, set())
            unvisited_links = links.difference(self.visisted_links)
            for link in unvisted_links:
                if link.startswith(self.url):
                    queue.put(link)

    def normalize_url(self, path, link):
        if link.startswith("http://"):
            return link.rstrip('/')
        elif link.startswith("/"):
            return self.url + link.rstrip('/')
        else:
            return self.url + path.rpartition('/')[0] + '/' + link.rstrip('/')

if __name__ == "__main__":
    collector = LinkCollector(sys.argv[1])
    collector.collect_links()
    for link, item in collector.collected_links.items():
        print("%s: %s" % (link, item))    
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/06/Pyth3oop6%20-%2065.png" width="80%" height="80%">
</a>

**07**

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%201.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%202.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%203.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%204.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%205A.png" width="80%" height="80%">
</a>

- [ ] Todo - Test this code!

```Python
# cb 199.A
normal_list = [1,2,3,4,5]

class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return f"x{index}"

class FunkyBackwards:
    def __reversed__(self):
        return "Backwards!"

for seq in normal_list, CustomSequence(), FunkyBackwards():
    print(f"\n{seq.__class__.__name__}: ", end="")

```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%205B.png" width="80%" height="80%">
</a>

```Python
#cb 200.A
import sys

filename = sys.argv[1]

with open(filename) as file:
    for index, line in enumerate(file):
        print(f"{index+1}: {line}", end="")
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%206.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%207.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%208.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%209.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2010.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2011.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2012.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2013.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2014.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2015.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2016.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2017.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2018.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2019.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2020.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2021.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2022.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2023.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2024.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2025.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2026.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2027.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2028.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2029.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2030.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2031.png" width="80%" height="80%">
</a>

```Python
# CB 210.A
class Options:
    default_options = {
    'port': 22,
    'host':'localhost',
    'usrname': 'Homer',
    'password': 'theSimpsons',
    'debug': True,
    }

    def __init__(self, **karwgs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2032.png" width="80%" height="80%">
</a>        

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2033.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2034.png" width="80%" height="80%">
</a>

```Python
#211.A
import os.path
import shutil

def augmented_move(target_folder, *filename, verbose=True, **specific):
    """move *.* into target_folder - to allow specific to particular files"""

    def print_verbose(message, filename):
        """print this when verbose is true"""
        if verbose:
            print(message.format(filename))

    for filename in filenames:
      target_path = os.path.join(target_folder, filename)
      if filename in specific:
          if specific[filename] == "disregard":
              print_verbose("disregarding {0}", filename)
          elif specific[filename] =="copy":
              print_verbose("copying file {0}", filename)
              shutil.copyfile(filename, target_path)
    else:
         print_verbose("moving {0}", filename)
         shutil.move(filename, target_path)
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2035.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2036.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2037.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2038.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2039A.png" width="80%" height="80%">
</a>

```Python
#213.A
def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)

some_args = range(3)
more_args = {
       "arg1": "ONE",
       "arg2": "TWO"}

print("Unpacking a sequence:", end=" ")

show_args(*some_args)
print("Unpacking a dict:", end=" ")

show_args(**more_args)

```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2039B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2040.png" width="80%" height="80%">
</a>

```Python
# 214.A - 214.B
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2041.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2042A.png" width="80%" height="80%">
</a>

```Python
# 215.A

def stan_function():
    print("Stan's function was called")

stan_function.description = "Stan's function is totally radical, dude!"

def second_function():
    print("The other function was called")

second_function.description = "This function is awesome!!!"

def yet_another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("the name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now We'll call the function that was passed to us!")
    function
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2042B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2043A.png" width="80%" height="80%">
</a>

```Python
# 216.A
import datetime
import time

class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.edndtime <= datetime.datetime.now()

class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)

        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)

```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2043B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2044.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2045.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2046.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2047.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2048.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2049.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2050.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2051.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2052A.png" width="80%" height="80%">
</a>

```Python
#220.A
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2052B.png" width="80%" height="80%">
</a>


<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2053.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2054.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2055A.png" width="80%" height="80%">
</a>

```Python
#221.A
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2055B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2056.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2057.png" width="80%" height="80%">
</a>

```text
scrncap 222A-223A
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2058.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2059.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2060.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2061.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2062.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2063.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2064.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2065.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2066.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2067.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2068.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2069.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2070.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2071.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/07/Pyth3oop7%20-%2072.png" width="80%" height="80%">
</a>
