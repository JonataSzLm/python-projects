import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input('Mensagem: ') + '\n'
        client.sendto(msg.encode(), ('192.168.43.213', 4436))
        data, sender = client.recvfrom(1024)
        print(data.decode())
        if data.decode() == 'sair\n' or msg == 'sair\n':
            break

    client.close()
except Exception as e:
    print('Erro de conexão!')
    print(e)
    client.close()