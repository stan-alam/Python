# CodeBlock 72.A 1 of 2

class ContactList(list):
  def search(self, name):
    """Return all contacts that contain the search value within their name"""
    matching_contacts = []
    for contact in self:
      if name in contact.name:
        matching_contacts.append(contact)
    return matching_contacts
