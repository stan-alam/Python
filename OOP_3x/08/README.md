**08**

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%201.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%202.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%203.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%204.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%205.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%206.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%207.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%208.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%209.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2010.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2011.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2012.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2013.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2014.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2015A.png" width="80%" height="80%">
</a>

        #236.A
        emails = ("Tom_Hanks@castaway.com", "Grizzly_Adams@wilderness.com")
        message = {
                "subject": "Here's some mail for ya",
                "message": "640K is enough RAM",
        }

        formatted = f"""
        From: <emails[0]>
        To: <emails[1]>
        Subject: {message['subject']}"""
        {message['message']}"""
        print(formatted)

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2015B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2016A.png" width="80%" height="80%">
</a>

```Python
      #237.A
      message["emails"] = emails

      formatted = f"""
      From: <{message['emails'][0]}>
      To: <{message['emails'][1]}>
      Subject: {message['subject']}
      {message['message']}"""
      print(formatted)

      #237.B
      class Email:
        def __init__(self, from_addr, to_addr, subject, messasge):
          self.from_addr = from_addr
          self.to_addr = to_addr
          self.subject = subject
          self._message = message

        def message(self):
            return self.message

      email = Email(
        "Tom_Hanks@castaway.com",
        "Grizzly_Adams@wilderness.com",
        "You've got mail!",
        "Take this email!",
      )

      formatted = f"""
      From: <{email.from_addr}>
      To: <{email.to_addr}>
      Subject: {email.subject}

      {email.message()}"""
      print(formatted)
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2016B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2017.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2018A.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2018B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2019.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2020.png" width="80%" height="80%">
</a>

```Python
orders = [("burger", 2, 5), ("fries", 4.2, 0), ("Bepsi", 1.75, 3)]

print("Product Quantity price Subtotal")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
            f"{product:10s}{quantity: ^9d} "
            f"${price: <8.2}${subtotal: >7.2f}"
         )
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2021.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2022.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2023.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2024.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2025.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2026.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2027.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2028.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2029.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2030.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2031.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2032.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2033.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2034.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2035.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2036.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2037.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2038.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2039.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2040.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2041.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2042.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2043.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2044A.png" width="80%" height="80%">
</a>

```Python
#cb248.A
import sys
import re

pattern = sys.argv[1] #argument vector!
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
    template = "'{}' matches patern '{}'"
else:
    template = "'{}' does not match pattern '{}'"

print(template.format(search_string, pattern))
```

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/src/248B.png" width="80%" height="80%">
</p>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2044B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2045A.png" width="80%" height="80%">
</a>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/src/249A.png" width="80%" height="80%">
</p>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2045B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2046.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2047.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2048.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2049.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2050.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2051.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2052.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2053.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2054.png" width="80%" height="80%">
</a>

```Python
#cb 252.A
pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
search_string  = "Grizzly_Adams@Sasquatch.com"
match = re.match(pattern, search_string)

if match:
  domain = match.groups()[0]
  print(domain)
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2055.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2056.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2057.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2058A.png" width="80%" height="80%">
</a>

```scrncap   
#254.A
```
<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/src/254A.png" width="80%" height="80%">
</p>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2058B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2059.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2060A.png" width="80%" height="80%">
</a>

```Python
#255.A
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2060B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2061.png" width="80%" height="80%">
</a>

```Python
#256.A
import pathlib

def count_sloc(dir_path):
    sloc = 0
    for path in dir_path.iterdir():
        if path.name.startswith("."):
            continue
        if path.suffix != ".py":
            continue
        with path.open() as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    sloc += 1
    return sloc

root_path = pathlib.Path(".")

print(f"{count_sloc(root_path)} lines of code")
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2062.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2063.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2064.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2065.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2066.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2067.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2068A.png" width="80%" height="80%">
</a>

```Python
#258.A
import pickle

my_data = ["some kind of list", "containing", 5, "values including another list", ["inner", "list"]]

with open("pickled_list", 'a') as file:
    pickle.dump(my_data, file)

with open("pickled_list" 'b') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == my_data
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2068B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2069.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2070.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2071.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2072A.png" width="80%" height="80%">
</a>

```Python
#260A.py
from threading import Timer
import datetime
from urllib.request import urlopen

class UpdatedUrl:
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2072B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2073.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2074.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2075.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2076.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2077.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2078.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2079A.png" width="80%" height="80%">
</a>

```Python
#cb
```

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2079B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2080.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2081A.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2081B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2082A.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2082B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2083.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2084A.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/08/Pyth3oop8%20-%2084B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/08/images/Pyth3oop8%20-%2085A.png" width="80%" height="80%">
</a>

```Python
#268.A  
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/08/images/Pyth3oop8%20-%2085B.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/08/images/Pyth3oop8%20-%2086.png" width="80%" height="80%">
</a>

<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/08/images/Pyth3oop8%20-%2087.png" width="80%" height="80%">
</a>

```Python
#269.A  
```
<a>
   <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/08/images/Pyth3oop8%20-%2088.png" width="80%" height="80%">
</a>
