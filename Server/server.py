import socket
import os
import shutil

def menu():
    # Lista arquivos do diretório
    print('Diretório do servidor: ', os.getcwd())
    connection.send(os.getcwd().encode()) 
    lista_arquivos = os.listdir(os.getcwd())
    connection.send(' '.join(lista_arquivos).encode())

    # Recebe e envia arquivos
    action = connection.recv(1024).decode()
    match action:
        case 'receive':
            receive_file()
        case 'send':
            send_file()
        case 'delete_file':
            delete_file()
        case 'delete_dir':
            delete_dir()
        case 'enter':
            enter_dir()
        case 'leave':
            leave_dir()
        case 'exit_program':
            exit_program()
        case 'invalid':
            print('Opção inválida.')
            menu()

def receive_file():
    print('Recebendo arquivo...')
    if (connection.recv(1024).decode() == 'Arquivo encontrado!'):
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
    else:
        print('Arquivo não encontrado!')

def send_file():
    namefile = connection.recv(1024).decode()
    print(os.getcwd() + "\\" + namefile)
    try:
        with open(namefile, 'rb') as file:
            connection.send('Arquivo encontrado!'.encode())
            while True:
                data = file.read(1024)
                if not data:
                    break
                connection.send(data)
            print('Arquivo enviado!')
    except:
        connection.send('Arquivo não encontrado!'.encode())
        print('Arquivo não encontrado!')

def delete_file():
    namefile = connection.recv(1024).decode()
    os.remove(namefile)
    print('Arquivo excluído!') 

def enter_dir():
    namefile = connection.recv(1024).decode()
    os.chdir(namefile)
    print('Diretório acessado!')
    menu()

def delete_dir():
    namefile = connection.recv(1024).decode()
    shutil.rmtree(namefile)
    print('Diretório excluído!')

def leave_dir():
    os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
    print('Saindo do diretório!')
    menu()

def exit_program():
    connection.close()
    print('Conexão encerrada.')
    exit()

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
print('Esperando por conexão na IP:', HOST, 'e porta:', PORT)
connection, address = server.accept()

# Conexão estabelecida
print('Conectado a:', address)

# Menu
menu()

# Fecha a conexão
connection.close()
# input('Pressione qualquer tecla para sair...')