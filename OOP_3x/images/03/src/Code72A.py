Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ContactList(list):
  def search(self, name):
    """Return all contacts that contain the search value within their name"""
    matching_contacts = []
    for contact in self:
      if name in contact.name:
        matching_contacts.append(contact)
    return matching_contacts

>>> class Contact:
  all_contacts = ContactList()

  def __init__(self, name, email):
    self.name = name
    self.email = email 
    Contact.all_contacts.append(self)

    
>>> c1 = Contact("Tom Hanks", "hanks@castaway.com")
>>> c2 = Contact("Wilson", "wilson@castaway.com")
>>> c3 = Contact("Grizzly Adams", "benTheBear@wilderness.com")
>>> [c.name for c in Contact.all_contacts.search('Tom')]
['Tom Hanks']
>>> 
