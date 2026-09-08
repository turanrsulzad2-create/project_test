import socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("google.com", 80))
client.send(b"HEAD / HTTP/1.1\r\nHOST: google.com\r\nConnection: close\r\n\n")

banner=client.recv(4000)
print(banner.decode(errors="ignore"))
client.close()
