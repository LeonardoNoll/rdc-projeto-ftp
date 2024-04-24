import socket

HOST = '192.168.1.9'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', '5000'))

print('Conectado\n')

namefile = str(input('Buscar arquivo>'))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

    print('Arquivo recebido')

# s.sendall(str.encode('Ja fui e ja voltei!'))
# data = s.recv(1024)

# print('Mensagem recebida: ', data.decode())     