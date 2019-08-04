Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class SecretString:
    """None secure - string storage"""

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """show the string if the pass_phrase is correct."""
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""

        
>>> secret_string = SecretString("WACME", "hamster")
>>> print(secret_string.decrypt("hamster"))
WACME
>>> print(secret_string.__plain_string)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(secret_string.__plain_string)
AttributeError: 'SecretString' object has no attribute '__plain_string'
>>> 
