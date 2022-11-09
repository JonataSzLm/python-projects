import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

try:
    client.connect(('192.168.43.213', 4436))
    client.send(b'Oi Tudo bem?\n')
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except Exception as e:
    print('Um erro ocorreu! :(')
    print(e)