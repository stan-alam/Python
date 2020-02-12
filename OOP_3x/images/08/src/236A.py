emails = ("Tom_Hanks@castaway.com", "Grizzly_Adams@wilderness.com")
message = {
        "subject": "Here's some mail for ya",
        "message": "640K is enough RAM",
}

formatted = f"""
From: <emails[0]}>
To: <emails[1]">
Subject: {message['subject']}"""
{message['message']}"""
print(formatted)
