import socket

hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 5000
print('IP do servidor: ', HOST)

def receive_file():
    print('Recebendo arquivo...')
    namefile = connection.recv(1024).decode()
    print('Nome do arquivo:', namefile)
    with open(namefile, 'wb') as file:
        print('Arquivo aberto...')
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)
        print('Arquivo recebido!')

def send_file():
    namefile = connection.recv(1024).decode()
    print("Server\\" + namefile)
    with open(namefile, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            connection.send(data)
        print('Arquivo enviado!')

# Cria um socket e vincula o endereço e a porta
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Escuta a porta
server.listen(1)
print('Esperando por conexão na IP: ', HOST, 'e porta: ', PORT)
connection, address = server.accept()

# Conexão estabelecida
print('Conectado a: ', address)

# Recebe e envia arquivos
action = connection.recv(1024).decode()
if action == 'receive':
    receive_file()
elif action == 'send':
    send_file()

# Fecha a conexão
connection.close()
# input('Pressione qualquer tecla para sair...')