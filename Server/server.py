import socket

hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 5000
print('IP do servidor: ', HOST)

def receive_file():
    print('Recebendo arquivo...')
    namefile = connection.recv(1024).decode()
    print(namefile)
    with open("Server/"+namefile, 'wb') as file:
        print('Arquivo aberto...')
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)
        print('Arquivo recebido!')

def send_file():
    namefile = connection.recv(1024).decode()
    with open("Server/"+namefile, 'rb') as file:
        data = file.read(1024)
        while data:
            connection.send(data)
            data = file.read(1024)
        print('Arquivo enviado!')



# Busca e mostra o IP do servidor

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

# namefile = connection.recv(1024).decode()

# Envia o arquivo
receive_file()
send_file()


