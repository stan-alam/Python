#310A
import socket

def respond(client):
    response = input("Enter a value:")
    client.send(bytes*response, "utf8"))
    client.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bing(("localhost", 3000))
    server.listen(1)
    try:
        while True:
            client, addr = server.accept()
            respond(client)
    finally:
        server.close()
