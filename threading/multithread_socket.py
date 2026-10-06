import socket
import threading
import json

host="127.0.0.1"
open_ports=[]

def check_port(port):
    print(f"Port {port} yoxlanilir")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    result = client.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} OPEN")
        open_ports.append(port)

    client.close()


threads=[]

for port in range(1, 1025):
    t = threading.Thread(target=check_port, args=(port,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All is over")

with open("scan_result.json", "w") as file:
    json.dump({
        "host": host,
        "open_ports": open_ports
     }, file, indent=4)
