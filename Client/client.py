import socket
import os

def getUserCommand():
    command = input('\nLista de comando:\n send - Enviar arquivo\n receive - Receber arquivo\n delete_file - Excluir arquivo\n enter_dir - Acessar diretório\n delete_dir - Excluir diretório\n exit_dir - Sair do diretório\n close - Sair\n')
    
    match command:
        case 'receive':
            requestFileFromServer()
        case 'send':
            sendFileToServer()
        case 'delete_file':
            deleteServerFile()
        case 'enter_dir':
            enterServerDir()
        case 'delete_dir':
            deleteServerFile()
        case 'exit_dir':
            exitDir()
        case 'close':
            closeProgram()
        case _:
            print('Opção inválida.')
            getUserCommand()

def receiveAndShowServerDir():
    serverDir = connection.recv(1024).decode()
    serverFileList = connection.recv(1024).decode().split()
    print('Diretório do servidor:\n', serverDir)
    if(len(serverFileList) == 0):
        print('Diretório vazio.')
    else:
        for arquivo in serverFileList:
            print(">",arquivo)

def showMenu():
    receiveAndShowServerDir()
    getUserCommand()

def requestFileFromServer():
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

def sendFileToServer():
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

def deleteServerFile():
    connection.send('deleteServerFile'.encode())
    namefile = input('Digite o nome do arquivo a ser excluído: ')
    connection.send(namefile.encode())
    print('Arquivo excluído.')

def enterServerDir():
    connection.send('enter'.encode())
    namefile = input('Digite o nome do diretório a ser acessado: ')
    connection.send(namefile.encode())
    print('Diretório acessado.')
    showMenu()

def deleteServerFile():
    connection.send('deleteServerFile'.encode())
    namefile = input('Digite o nome do diretório a ser excluído: ')
    connection.send(namefile.encode())
    print('Diretório excluído.')

def exitDir():
    connection.send('leave'.encode())
    print('Saindo do diretório.')
    showMenu()

def closeProgram():
    connection.send('closeProgram'.encode())
    print('Saindo...')
    connection.close()

# Define o endereço IP e a porta do servidor
# HOST = '192.168.1.11'
HOST = input('Digite o IP do servidor: ')
PORT = 5000

# Cria um socket e conecta ao servidor
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))

# Conexão estabelecida
print(f'Conectado a: {HOST}\n')

# Navegação no servidor
showMenu()

# Fecha a conexão
connection.close()
input('Pressione qualquer tecla para sair...')
