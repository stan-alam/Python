**01**
Variables, functions and functional programming, closures, decorators, modules and packages.


This is the first part of a series of courses designed to dive into the internal mechanics and more advanced aspects of Python 3.

This is not a course for beginners - if you've been programming in Python for a week or a couple of months, you should probably continue writing Python for a little while longer before starting this series.

On the other hand, if you now start asking yourself questions like:

I wonder how it works?
Is there another way to do this?
What kind of closure is this? Is it the same as lambda?
I know how to use a decorator someone else wrote, but how does it work? Can I write my own?
Why doesn't this logical expression return a logical value?
What does import actually do and why do I get side effects?
and similar types of questions...
then this course is for you.

In this course series, I'll give you a more fundamental and in-depth understanding of the Python language and standard library.

For obvious reasons, Python is called "battery-powered" - there is a ton of functionality in core Python that remains to be explored.

So this course is not about explaining my favorite third-party libraries, but about Python as a language and its standard library.

It's about helping you learn Python and answering the questions you ask yourself as you develop more and more knowledge of the language.

In Python 3: Deep Dive (Part 1), we'll take a closer look at:

Variables are, in particular, simply symbols that point to objects in memory.
Namespaces and Scope
Python Numeric Types
Python's boolean type is more than just a statement than you might think!
Runtime vs. compile time and how this affects function defaults, decorators, module imports, etc.
Functions in general (including lambdas)
Functional programming techniques (such as mapping, reducing, filtering, archiving, etc.)
Closures
Decorators
Imports, modules and packages
Tuples as data structures
Named Tuples 

**02**

Sequences, iterations, iterators, generators, context managers, and generator-based coroutines.


Part 2 of this Python 3: Deep Dive series covers:

sequences
iterables
iterators
generators
comprehension
context managers
generator-based coroutines
I'll show you exactly how iteration works in Python - from the sequence protocol to the iterable and iterator protocols, and how we can write our own sequence and iterable data types.

We'll go into some detail to explain sequence slices and their relationship to ranges.

We'll also take a closer look at comprehensions, and I'll show you how list comprehensions are actually closures and have their own scope, as well as the reason why sometimes subtle bugs creep in to list comprehensions that we might not expect.

We'll take a deep dive into the itertools module and look at all the features available there and how useful (but missed!) they can be.

We will also look at generator functions, their relationship to iterators, and their comprehension counterparts (generator expressions).

Context managers, an often-overlooked construct in Python, are also covered in detail. We'll learn how to create and use our own context managers and understand the relationship between context managers and generator functions.

Finally, we'll look at how we can use generators to create coroutines.

Each section is followed by a project designed to put into practice what you learn throughout the course.

This course series focuses on the Python language and standard library. The standard CPython distribution has a huge amount of functionality and things to understand, so I don't cover third-party libraries. This is a deep dive into Python, not an exploration of the many very useful third-party libraries that have grown up around Python. These are often large enough to warrant a full course! Indeed, many of them already exist!

***** Prerequisites *****

Please note that this is a relatively advanced Python course and requires in-depth knowledge of some Python topics.

In particular, you should already have a deep understanding of the following topics:

functions and function arguments
packing and unpacking iterations and how this is used with function arguments (i.e. using *)
closures
decorators
Boolean truth values ​​and how any object has an associated truth value
named tuples 
lambdas
import modules and packages
You should also have basic knowledge of the following topics:

various data types (numeric, string, list, tuple, dictionaries, sets, etc.)
for loop, while loop, break, continue, if else
if statements
try...except...else...finally...
basic knowledge of how to create and use classes (methods, properties) - no need for advanced topics like inheritance or meta-classes
understand how certain special methods are used in classes (e.g. __init__, __eq__, __lt__, etc.)

**03**
Dictionaries, Sets, and Related Data Structures. This course is an in-depth look at Python dictionaries. Dictionaries are ubiquitous in Python. Classes are dictionaries, modules are dictionaries, namespaces are dictionaries, sets are dictionaries, and much more.


In this course we will cover in detail:

Associative Arrays and How They Can Be Implemented Using Hash Maps
hash functions and how we can use them for our own custom classes
Python Dictionaries and Sets and the Various Operations We Can Perform on Them
specialized dictionary structures like OrderedDict and how they relate to the built-in Python3.6+ dict
Python's implementation of multiple sets, the Counter class
ChainMap class
How to create custom dictionaries by inheriting from the UserDict class
How to serialize and deserialize dictionaries to JSON
Using schemas in custom JSON deserialization
A brief introduction to some useful libraries such as JSONSchema, Marshmallow, PyYaml, and Serpy