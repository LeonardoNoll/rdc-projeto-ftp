import socket
import os
import shutil

def menu():
    # Lista arquivos do diretório
    lista_arquivos = os.listdir(os.getcwd())
    connection.send(' '.join(lista_arquivos).encode())

    # Recebe e envia arquivos
    action = connection.recv(1024).decode()
    if action == 'receive':
        receive_file()
    elif action == 'send':
        send_file()
    elif action == 'delete_file':
        delete_file()
    elif action == 'delete_dir':
        delete_dir()
    elif action == 'enter':
        enter_dir()


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

def delete_file():
    namefile = connection.recv(1024).decode()
    os.remove(namefile)
    print('Arquivo excluído!') 

def enter_dir():
    namefile = connection.recv(1024).decode()
    os.chdir(namefile)
    print('Diretório acessado!')

def delete_dir():
    namefile = connection.recv(1024).decode()
    shutil.rmtree(namefile)
    print('Diretório excluído!')

# Define o endereço IP e a porta do servidor
hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 5000
print('IP do servidor: ', HOST)

# Cria um socket e vincula o endereço e a porta
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Escuta a porta
server.listen(1)
print('Esperando por conexão na IP: ', HOST, 'e porta: ', PORT)
connection, address = server.accept()

# Conexão estabelecida
print('Conectado a: ', address)

menu()



# Fecha a conexão
connection.close()
# input('Pressione qualquer tecla para sair...')