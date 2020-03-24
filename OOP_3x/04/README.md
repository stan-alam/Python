## 04

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%203A.png" width="80%" height="80%">
</a>

```text
ScreenCapture 104.A

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%203B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%204A.png" width="80%" height="80%">
</a>

```text
ScreenCapture 104.B - 104.C

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%205A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 105.A
#105.A
def call_exceptor():
    print("call_exceptor starts here...")
    no_return()
    print("an exception is raised")
    print("....so this won't print")
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%205B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%205C.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%206.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%207.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 107.A
def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is nil"
```

```text
ScreenCapture 107.B
```

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/src/107B.png" width="70%" height="70%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%208.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%209A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 108.A
#108.A
def funny_division2(divider):
    try:
        if divider == 42:
            raise ValueError("42 is a reserved number")
        return 100 / divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than 0"
```

```text
ScreenCapture 108.B
```
<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/src/108B.png" width="70%" height="70%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%209B.png" width="80%" height="80%">
</a>

```text
ScreenCapture 108.C

```

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/src/108C.png" width="75%" height="75%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%209C.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2010A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 109.A
#109.A
def funny_div3(divider):
    try:
        if divider == 42:
            print("42 is a special number in the multiverse(s)")
        return 100 / divider
    except ZeroDivisionError:
        return "C'mon don't enter 0!"
    except TypeError:
        return "Enter a number value"
    except ValueError:
        print("no, the multiverse(s) says NOT 42!")
        raise
```

```text
#screencap 109AB
```
<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/src/109AB.png" width="75%" height="75%">
</p>


<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2010B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2011.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 109.B
#109.B
try:
	raise ValueError("This arg")
except ValueError as e:
    print("the exception args were", e.args)
```

```text
#screencap 109B
```
<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/src/109B.png" width="75%" height="75%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2012A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 110.A
#110.A
import random
here_and_there_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(here_and_there_exceptions)
    print("raising...{}".format(choice))
    if choice:
       raise choice("An error has occured")
except ValueError:
    print("Just caught a value error")
except TypeError:
    print("You just caused a Type Error")
except Exception as e:
    print('Caught some "weird" error ..?: %s' % (e.__class__.__name__))
else:
    print("Hi, there were no exception...means whatever runs here will run!")
finally:
    print("This cleanup code will run no matter what... e.g. to clean up test env")
```

```text
ScreenCapture 110.B
```
<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/src/110B.png" width="75%" height="75%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2013.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2014.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2015.png" width="80%" height="80%">
</a>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/svg/Graph112A.svg" width="50%" height="50%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2016.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2017.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2018A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 113.A
#113.A
class InvalidWithDrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"account does not have sufficient funds for ${amount}")
        self.amount = amount
        self.balance = balance
    def overage(self):
        return self.amount - self.balance
```

```text
ScreenCapture 113.B
```
<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/src/113B.png" width="75%" height="75%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2018B.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 114.A
def divide_with_exception(number, divisor):
    try:
	print(f"{number} / {divisor} = {number / divisor}")
    except ZeroDivisionError:
	print("You can't divide by 0")

def divide_with_if(number, divisor):
    if divisor == 0:
	print("You can't divide by 0, duh!")
    else:
        print(f"{number} / { divisor} = { number / divisor}")
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2018C.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2019A.png" width="80%" height="80%">
</a>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/iamerror.jpg" width="50%" height="50%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2019B.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 114.A for 19B
def divide_with_exception(number, divisor):
    try:
	print(f"{number} / {divisor} = {number / divisor}")
    except ZeroDivisionError:
	print("You can't divide by 0")

def divide_with_if(number, divisor):
    if divisor == 0:
	print("You can't divide by 0, duh!")
    else:
        print(f"{number} / { divisor} = { number / divisor}")
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2020.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2021A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 116.A #1
class Inventory:
  def lock(self, item_type):
    """select a type of item. This method will lock the currently selected item as to prevent race conditions...preventing the selling of the same item to more than one person at a time"""
    pass

  def unlock(self, item_type):
    """Release the given type so other's have    access to it"""
    pass

  def purchase(self, item_type):
    """if the item is NOT locked, raise an exception. If the item_type does not exist, raise an exception. If the item is currently out of stock, raise an exception. If the item is available, subtract one item and return the number of items left."""
    pass
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2021B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2022A.png" width="80%" height="80%">
</a>

- [ ] Todo - Test this code!

```Python
# CodeBlock 116.A #2
#162A-2
item_type = "widget"
inv = Inventory()
inv.lock(item.type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("sorry, the item you requested {}".format(item_type))
except OutOfStock:
    print("not available")
else:
    print("Purchase is complete. There are {num_lef} {item_left} {item_type}s left")
finally:
    inv.unlock(item_type)
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2022B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2023.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2024.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2025.png" width="80%" height="80%">
</a>

```Python
#118.A
import hashlib


class User:
    def __init__(self, username, password):
        """Create a new user Object. The password is encrypted before being stored."""
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encypt the password with the username and return the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256       (hash_string).hexdigest()

    def check_password(self, password):
        """rerturn true if password is valid for this user, false otherwise"""
        encrypted = self.__encrypt_pw(password)
        return encrypted == self.password

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2026A.png" width="80%" height="80%">
</a>

```Python  
#119.A
class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass  
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2026B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2027A.png" width="80%" height="80%">
</a>

```Python
# code block 120.A
class Authenticator:
    def __init__(self):
    	"""construct an authenticator to manage user logins"""
    	self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 8:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)  
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2027B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2028A.png" width="80%" height="80%">
</a>

```Python
# code block 121.A
def login(self, username, password):
    try:
        user = self.users[username]
    except KeyError:
        raise InvalidUsername(username)

    if not user.check_password(password):
        raise InvalidPassword(username, user)

    user.is_logged_in = True
    return True  
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2028B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2029.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2030.png" width="80%" height="80%">
</a>

```Python
# code block 122.A

class Authorizer:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2031.png" width="80%" height="80%">
</a>

```Python
# code block 123.A
def check_permission(self, perm_name, username):
    if not self.authenticator.is_logged_in(username):
        raise NotLoggedInError(username)

    try:
        perm_set = self.permissions[perm_name]
    except KeyError:
        raise PermissionError("Permission not found")
    else:
        if username not in perm_set:
            raise NotPermittedError(username)
        else:
            return True
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/04/Pyth3oop4%20-%2032.png" width="80%" height="80%">
</a>

```text
# screencap 123B-124A
```
