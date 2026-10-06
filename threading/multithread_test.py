import threading
import time

def check_port(port):
    print(f"Port {port} yoxlanilir")
    time.sleep(2)
    print(f"Port {port} checking is over")
    
threads=[]

for port in range(1, 6):
    t=threading.Thread(target=chech_port, args=(port,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All is over")
