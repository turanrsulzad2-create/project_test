from scapy.all import *

network="192.168.193.0/24"

answered, not_answered=sr(
        IP(dst=network) / ICMP(),
        iface="ens33",
        timeout=2,
        verbose=0
    )
for sent, recieved in answered:
    print(recieved.src)
