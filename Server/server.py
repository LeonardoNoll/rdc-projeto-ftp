import socket

PORT = 5000

# Busca e mostra o IP do servidor
hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
print(f"IP Address: {HOST}")

# Cria socket e vincula o endereço e a porta
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Escuta a porta
server.listen(1)
print ('Esperando o cliente no servidor: ', HOST,'e porta: ', PORT)
connection, adress = server.accept()

# Conexão estabelecida
# Mostra o endereço do cliente
print ('Conectado em: ', adress)

namefile = connection.recv(1024).decode()

# Envia o arquivo
with open("Server/"+namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)
    print('Arquivo enviado!')


