import socket
import os

def menu():
    diretorio_server = connection.recv(1024).decode()
    print('Diretório do servidor:')
    print(diretorio_server)
    lista_arquivos = connection.recv(1024).decode().split()
    for arquivo in lista_arquivos:
        print(">",arquivo)

    # Envia e recebe arquivos
    action = input('\nDigite a opção que você deseja acessar:\n 1 - Receber arquivo\n 2 - Enviar arquivo\n 3 - Excluir arquivo\n 4 - Acessar diretório\n 5 - Excluir diretório\n 6 - Sair do diretório\n 7 - Sair\n')

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
        case '6':
            leave_dir()
        case '7':
            exit_program()
        case _:
            print('Opção inválida.')
            connection.send('invalid'.encode())
            menu()

def get_file():
    connection.send('send'.encode())
    namefile = input('Digite o nome do arquivo a ser buscado: ')
    connection.send(namefile.encode())
    if connection.recv(1024).decode() == 'Arquivo encontrado!':
        with open(namefile, 'wb') as file:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                file.write(data)
            print('Arquivo recebido.')
    else:
        print('Arquivo não encontrado.')

def send_file():
    connection.send('receive'.encode())
    namefile = input('Digite o nome do arquivo a ser enviado: ')
    try:
        with open(namefile, 'rb') as file:
            connection.send('Arquivo encontrado!'.encode())
            connection.send(namefile.encode())
            while True:
                data = file.read(1024)
                if not data:
                    break
                connection.send(data)
            print('Arquivo enviado.')
    except:
        print('Arquivo não encontrado.')

def delete_file():
    connection.send('delete_file'.encode())
    namefile = input('Digite o nome do arquivo a ser excluído: ')
    connection.send(namefile.encode())
    print('Arquivo excluído.')

def enter_dir():
    connection.send('enter'.encode())
    namefile = input('Digite o nome do diretório a ser acessado: ')
    connection.send(namefile.encode())
    print('Diretório acessado.')
    menu()

def delete_dir():
    connection.send('delete_dir'.encode())
    namefile = input('Digite o nome do diretório a ser excluído: ')
    connection.send(namefile.encode())
    print('Diretório excluído.')

def leave_dir():
    connection.send('leave'.encode())
    print('Saindo do diretório.')
    menu()

def exit_program():
    connection.send('exit_program'.encode())
    print('Saindo...')
    connection.close()

# Define o endereço IP e a porta do servidor
HOST = '192.168.1.11'
# HOST = input('Digite o IP do servidor: ')
PORT = 5000

# Cria um socket e conecta ao servidor
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))

# Conexão estabelecida
print(f'Conectado a: {HOST}\n')

# Navegação no servidor
menu()

# Fecha a conexão
connection.close()
# input('Pressione qualquer tecla para sair...')
