# 03

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%200.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%203.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%204A.png" width="80%" height="80%">
</a>

```Python
# code block 71.A
class Supplier(Contact):
    def order(self, order):
        print(
            "If this were a prod system you would  send " f"'{order}' order to '{self.name}'"
        )
```

```text

# ScreenCapture 71.B

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%204B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%205A.png" width="80%" height="80%">
</a>

```Python

# CodeBlock 72.A 1 of 2

class ContactList(list):
  def search(self, name):
    """Return all contacts that contain the search value within their name"""
    matching_contacts = []
    for contact in self:
      if name in contact.name:
        matching_contacts.append(contact)
    return matching_contacts

```

```Python
# CodeBlock 72.A 2 of 2

class Contact:
  all_contacts = ContactList()

  def __init__(self, name, email):
    self.name = name
    self.email = email
    Contact.all_contacts.append(self)

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%205B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%206A.png" width="80%" height="80%">
</a>

**ScreenCapture 72.B**

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/src/72BscreenCap.png" width="80%" height="80%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%206B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%207A.png" width="80%" height="80%">
</a>

```Python

#Code Block 73.A,

class LongNameDict(dict):
  def longest_key(self):
    longest = None
    for key in self:
      if not longest or len(key) > len(longest):
        longest = key
    return longest

```

**73.B ScreenCapture**

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/src/73Bscreencap.png" width="80%" height="80%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%207B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%208.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%209.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2010.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2011.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2012A.png" width="80%" height="80%">
</a>

```python
# code for 75.A

class MailSender:
  def send_mail(self, message):
    print("sending mail to " + self.email)
    # add some logic

```


```text
# ScreenCapture 75.A
```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2012B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2013.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2014.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2015.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2016.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2017A.png" width="80%" height="80%">
</a>

```text
# graph 78.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2017B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2018.png" width="80%" height="80%">
</a>

```Python
# 79.A
class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on BaseClass")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Call method on left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2019A.png" width="80%" height="80%">
</a>

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/src/79AScreenCap.png" width="80%" height="80%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2019B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2020A.png" width="80%" height="80%">
</a>

```Python
# Code Block 80.A
def call_me(self):
    LeftSubclass.call_me(self)
    RightSubclass.call_me(self)
    print("Calling method on subclass")
    self.num_sub_calls +=  1

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2020B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2021.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2022.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2023.png" width="80%" height="80%">
</a>

```python
# CodeBlock 83.A

class Contact:
  all_contacts = []

  def __init__(self, name="", email="", **kwargs):
    super().__init__(**kwargs)
    self.name = name
    self.email = email
    self.all_contacts.append(self)


class AddressHolder:
  def __init__(self, street="", city="", state="", code="", **kwargs):
    super().__init__(**kwargs)
    self.street = street
    self.city = city
    self.state = state
    self.zip = zip


class Friend(Contact, AddressHolder):
  def __init__(self, phone="", **kwargs):
    super().__init__(**kwargs)
    self.phone = phone

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2024.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2025.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2026.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2027.png" width="80%" height="80%">
</a>

```Python

# Code block 85.A

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.extension):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    extension = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    extension = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    extension = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2028.png" width="80%" height="80%">
</a>


**85.A ScreenCapture**

<p align="center">
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/src/85A_scncap1of3.png" width="80%" height="80%">
</p>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2029A.png" width="80%" height="80%">
</a>

```Python

# Code block 87.A
class FlacFile:
  def __init__(self, filename):
    if not filename.endswith(".flac"):
      raise Exception("Invalid File Frmt")

    self.filename = filename

   def play(self):
       print("Playing {} as flac".format(self.filename))
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2029B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2030.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2031.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2032.png" width="80%" height="80%">
</a>

```text
ScreenCapture 88.A - 88.B

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2033.png" width="80%" height="80%">
</a>

```text

ScreenCapture 89.A

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2035A.png" width="80%" height="80%">
</a>

```Python

# Code block 90.A
import abc

class MediaLoader(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def play(self):
	pass

  @abc.abstractproperty
  def ext(self):
	pass

  @classmethod
  def __subclasshook__(cls, C):
	if cls is MediaLoader:
	  attrs = set(dir(C))
	  if set(cls.__abstractmethods__) <== attrs:
		return True
	return NotImplemented

```

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2035B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2036A.png" width="80%" height="80%">
</a>

```text
ScreenShot 91.A

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2036B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2037.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2038.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2039.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2040.png" width="80%" height="80%">
</a>

```text
# screencapture 93.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2041.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2042A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 93.A
class IntroToPython:
    def lesson(self):
	    return f """
	        Hi {self.student}. define two vars, an int named with a value of 1 & a string named b with a value of 'hi'

"""

    def check(self, code):
        return code == "a = 1\nb = 'hi!'"	return code == "a = 1\nb = 'hi!'"
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2042B.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 94.A
class Assignment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, student):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2042C.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2043A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 94.A_2
class Stats(Assignment):
    def less(self):
        return (
            "Good work, "
            + self.student
            + ". Now calculate the avg of the numbers "
            + " 3, 8, 10, -5 and assign to a var named 'avg'"
        )

    def check(self, code):
        import stats

        code = "import stats\n" + code

        local_vars = { }
        global_vars = { }
        exec(code, global_vars, local_vars)

        return local_vars.get("avg") == stats.mean([3, 8, 10, -5])
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2043B.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 95.A
class AssignmentGrader:
    def __init(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1

            return result
    def lesson(self):
        return self.assignment.lesson()
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2043C.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2044A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 96.A
import uuid
# needs refactoring
class Grader:
    def __init__(self):
        self.student_graders = {}
        self.assignments_classes = {}

    def register(self, assignment_classes):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the appropriate method(s)"
            )

        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2044B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2045.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2046.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 97.A
def get_lesson(self, student):
  assignment = self.student_graders[student]
  return assignment.lesson()

def check_assignment(self, student, code):
  assignment = self.student_graders[student]
  return assignment.check(code)

# CodeBlock 97.B
def assignment_summary(self, student):
  grader = self.student_graders[student]
  return f"""
  {student}'s attempts at {grader.assignment.__class__.__name__}:

  attempts: {grader.attempts}
  correct: {grader.correct_attempts}
  passed: {grader.correct_attempts > 0}
  """
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2047A.png" width="80%" height="80%">
</a>

```Python
# CodeBlock 98.A
grader = Grader()
itp_id = grader.register(IntroToPython) #not blackmagic
stat_id = grader.register(Stats)

grader.start_assignment("Grizzly_Adams", itp_id)
print("Grizzly_Adams's Lesson:", grader.get_lesson("Grizzly_Adams"))
print(
    "Grizzly_Adams check:",
    grader.check_assignment("Grizzly_Adams", a = 1 ; b = 'hola'"),
)
print(
    "Grizzly_Adams's other check:",
    grader.check_assignment("Grizzly_Adams", "a = 1/nb = 'hola'"),
)

print(grader.assignment_summary("Grizzly_Adams"))

grader.start_assignment("Grizzly_Adams"m stat_id)
print("Grizzly_Adams's Lesson:", grader.get.lesson("Grizzly_Adams"))
print("Grizzly_Adams:", grader.check_assignment("Grizzly_Adams", "avg=6.66"))
print(
    "Grizzly_Adams' other check:",
    grader.check_assignment(
        "Grizzly_Adams", "avg = stats.mean([23, 6, 66])"
    ),
)

print(grader.assignment_summary("Grizzly_Adams"))

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2047B.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/images/03/pyth3oop3%20-%2048.png" width="80%" height="80%">
</a>
