from scapy.all import *

#pacote = ARP(psrc="19.19.19.19")
#pacote = Ether()/IP()/TCP(dport=22)/"Hello"
pacote = IP(dst="google.com")/ICMP()
pacote.show()
#respondidos, nao_respondidos = sr(pacote) -> Enviar e receber resposta
#send(pacote) -> Enviar
#send(pacote, loop=1) -> Enviar em loop