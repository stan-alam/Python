message["emails"] = emails

formatted = f"""
From: <{message['emails'][0]}>
To: <{message['emails'][1]}>
Subject: {message['subject']}
{message['message']}"""
print(formatted)
