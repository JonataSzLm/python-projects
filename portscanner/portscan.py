import socket
import sys
import random

# def port_list(first_port, last_port):
#     if first_port and last_port:
#         return range(first_port, last_port + 1)
#     else:
#         return None
#   Melhorar!!

def scan(host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((host, int(port)))

            if code == 0:
                print('[+] {} open'.format(port))
    except:
        print('Error, something is wrong')

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(',')
        else:
            ports = [21, 22, 23, 25, 80, 135, 139, 443, 445, 3306, 8080, 8443]

        scan(host, ports)
    else:
        print('Usage: python3 portscan.py <host> <ports>')