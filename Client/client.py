import socket

# Pede para o cliente inserir o IP do servidor
HOST = str(input('Digite o IP do servidor>'))
PORT = 5000

# Cria socket e conecta ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Conexão estabelecida
print('Conectado em: {HOST}\n')

# Pede para o cliente inserir o nome do arquivo a buscar
namefile = str(input('Buscar arquivo>'))
client.send(namefile.encode())

# Recebe o arquivo
with open("Client/"+namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)
    print('Arquivo recebido')

 