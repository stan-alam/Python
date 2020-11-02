#311.A
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3000))
print("Received: {0}".format(client.recv(3000)))
client.close()
