<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/10/images/Pyth3oop10%20-%20page%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/10/images/Pyth3oop10%20-%20page%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/10/images/Pyth3oop10%20-%20page%203.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/10/images/Pyth3oop10%20-%20page%204.png" width="80%" height="80%">
</a>

```Python
#cb 310.A
import socket

def respond(client):
    response = input("Enter a value:")
    client.send(bytes*response, "utf8"))
    client.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 3000))
    server.listen(1)
    try:
        while True:
            client, addr = server.accept()
            respond(client)
    finally:
        server.close()

```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/10/images/Pyth3oop10%20-%20page%205A.png" width="80%" height="80%">
</a>

```Python
#cb 311.A
```
<a>
  <img src="https://github.com/stan-alam/Python/blob/develop/OOP_3x/10/images/Pyth3oop10%20-%20page%205B.png" width="80%" height="80%">
</a>
