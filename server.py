import socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server is waiting for a connection...")

client, adress=server.accept()

print("Connected:", adress)

client.send(b"Hello from the server!")

client.close()
server.close()
