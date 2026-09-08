from scapy.all import *
packet=IP(dst="google.com") / TCP(dport=80, flags="S")

response= sr1(packet, timeout=2, verbose=0)

if response:
    response.show()
else:
    print("No response")
