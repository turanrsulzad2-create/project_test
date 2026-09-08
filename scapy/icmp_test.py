from scapy.all import *
packet=IP(dst="127.0.0.1") / ICMP()
response=sr1(packet, timeout=2)

if response:
    response.show()
else:
    print("No response")
