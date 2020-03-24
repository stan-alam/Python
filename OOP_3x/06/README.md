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
