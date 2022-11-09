from scapy.all import *

def print_pacote(pkt):
    data_pkt = raw(pkt[TCP].payload).decode('latin-1')
    if data_pkt.startswith('POST') and "pass" in data_pkt:
        print(data_pkt)

sniff(filter="port 80", prn=print_pacote, store=0)
