import socket
import os

def menu():
    print('Diretório do servidor:')
    lista_arquivos = connection.recv(1024).decode().split()
    for arquivo in lista_arquivos:
        print(">",arquivo)

    # Envia e recebe arquivos
    action = input('\nDigite a opção que você deseja acessar:\n 1 - Receber arquivo\n 2 - Enviar arquivo\n 3 - Excluir arquivo\n 4 - Acessar diretório\n 5 - Excluir diretório\n')

    match action:
        case '1':
            get_file()
        case '2':
            send_file()
        case '3':
            delete_file()
        case '4':
            enter_dir()
        case '5':
            delete_dir()
        case _:
            print('Opção inválida.')
            exit()


def get_file():
    connection.send('send'.encode())
    namefile = input('Digite o nome do arquivo a ser buscado: ')
    connection.send(namefile.encode())
    with open(namefile, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)
        print('Arquivo recebido.')

def send_file():
    connection.send('receive'.encode())
    namefile = input('Digite o nome do arquivo a ser enviado: ')
    connection.send(namefile.encode())
    with open(namefile, 'rb') as file:
        while True:
            # print('Enviando arquivo...')
            data = file.read(1024)
            if not data:
                break
            connection.send(data)
        print('Arquivo enviado.')

def delete_file():
    connection.send('delete'.encode())
    namefile = input('Digite o nome do arquivo a ser excluído: ')
    connection.send(namefile.encode())
    print('Arquivo excluído.')

def enter_dir():
    connection.send('enter'.encode())
    namefile = input('Digite o nome do diretório a ser acessado: ')
    connection.send(namefile.encode())
    print('Diretório acessado.')

def delete_dir():
    connection.send('delete_dir'.encode())
    namefile = input('Digite o nome do diretório a ser excluído: ')
    connection.send(namefile.encode())
    print('Diretório excluído.')

# Define o endereço IP e a porta do servidor
HOST = '192.168.1.11'
# HOST = input('Digite o IP do servidor: ')
PORT = 5000

# Cria um socket e conecta ao servidor
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))

# Conexão estabelecida
print(f'Conectado a: {HOST}\n')

menu()
menu()


# Fecha a conexão
connection.close()
# input('Pressione qualquer tecla para sair...')
