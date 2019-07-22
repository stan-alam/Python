Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class LongNameDict(dict):
  def longest_key(self):
    longest = None
    for key in self:
      if not longest or len(key) > len(longest):
        longest = key
    return longest

 
>>> longkeys = LongNameDict()
>>> longkeys['hola'] = 1
>>> longkeys['longest yet'] = 5
>>> longkeys['hola2'] = 'multiverse'
>>> longkeys.longest_key()
'longest yet'
>>> 
