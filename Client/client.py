import socket

# HOST = '127.0.0.1'
HOST = str(input('Digite o IP do servidor>'))
PORT = 5000



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print('Conectado em: {HOST}\n')

namefile = str(input('Buscar arquivo>'))

client.send(namefile.encode())

with open("Client/"+namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

    print('Arquivo recebido')

 