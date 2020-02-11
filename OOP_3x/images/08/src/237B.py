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
