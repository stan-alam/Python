# CodeBlock 72.A 2 of 2

class Contact:
  all_contacts = ContactList()

  def __init__(self, name, email):
    self.name = name
    self.email = email
    Contact.all_contacts.append(self)
