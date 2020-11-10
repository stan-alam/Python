# 09
## Iterator Pattern!

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%203.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%204.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%205.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%206.png" width="80%" height="80%">
</a>

```Python
#275.A
class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%207A.png" width="80%" height="80%">
</a>

```text
scrncap 276.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%207B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%208.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%209.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2010.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2011.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2012.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2013.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2014A.png" width="80%" height="80%">
</a>

```Python
#279.A
import sys

filename = sys.argv[1]

with open(filename) as file:
    header = file.readline().strip().split("\t")
contacts = [
dict(
zip(header, line.stripe().split("\t"))
)]

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2014B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2015.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2016A.png" width="80%" height="80%">
</a>

```Python
#280.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2016B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2017.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2018.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2019.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2020.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2021.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2022A.png" width="80%" height="80%">
</a>

```Python
#283.A
import sys

#generator expression
inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (
            l.replace("\tWARNING", "") for l in infile if "WARNING" in l
        )
        for l in warnings:
            outfile.write(l)

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2022B.png" width="80%" height="80%">
</a>

```Python
#283.B  
with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l infile:
            if "WARNING" in l:
                outfile.write(l.replace("\tWARNING", ""))
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2022C.png" width="80%" height="80%">
</a>

```Python
#283C
class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

        def __iter__(self):
            return self

        def __next__(self):
            l = self.insequence.readline()
            while l and "WARNING" not in l:
                l = self.insequence.readline()
            if not l:
    raise StopIteration
            return l.replace("\tWARNING", "")
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2023.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2024.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2025.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2026.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2027.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2028.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2029.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2030.png" width="80%" height="80%">
</a>

https://github.com/stan-alam/science/tree/master/CS/comp-sciPyth

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2031A.png" width="80%" height="80%">
</a>

```Python
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

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2031B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2032.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2033.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2034.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2035.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2036.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2037.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2038.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2039.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2040.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2041A.png" width="80%" height="80%">
</a>

```Python
#291.A
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2041B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2042.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2043.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2044.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2045.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2046.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2047.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2048.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2049.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2050.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2051.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2052.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2053.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2054A.png" width="80%" height="80%">
</a>

```Python
#298.A
import csv

dataset_file_name = "pigments.csv"

def load_colors(filename):
  with open(filename) as dataset_file:
    lines = csv.reader(dataset_file)
    for line in lines:
      label, hex_color = line
      yield (hex_to_rgb(hex_color), label)
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2054B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2055.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2056.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2057.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2058.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2059.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2060.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2061.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%2062.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2063A.png" width="80%" height="80%">
</a>

```Python
# cb 301.A
from collections import Counter

def name_pigments(model_colors, target_colors, num_neighbors=5):
  for target, near in nearest_neighbors(
    model_colors, target_colors, num_neighbors=5
  ):
    print(target, near)
    name_guess = Counter(n[1] for n in near).most_common()[0][0]
    yield target, name_guess
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2063B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2064A.png" width="80%" height="80%">
</a>

```Python
# cb302.A

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2064B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2065A.png" width="80%" height="80%">
</a>

```Python
# cb302B
def process_colors(dataset_file_name="pigments.csv"):
  model_colors = load_colors(dataset_file_name)
  colors = name_colors(model_colors, generate_colors(), 5)
  write_results(colors)


if __name__ == "__main__":
  process_colors()
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2065B.png" width="80%" height="80%">
</a>

```Python
# cb
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2066.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/09/images/Pyth3oop9%20-%20page%2067.png" width="80%" height="80%">
</a>
