import socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

print("Connected to serrver!")

data=client.recv(1024)

print("server:", data.decode())

client.close()
