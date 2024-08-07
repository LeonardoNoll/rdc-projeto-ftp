import socket
import os
import shutil

def receiveClientCommand():
    command = connection.recv(1024).decode()
    match command:
        case 'receive':
            receiveFileFromClient()
        case 'send':
            sendFileToClient()
        case 'deleteFile':
            deleteFile()
        case 'deleteDir':
            deleteDir()
        case 'enter':
            enterDir()
        case 'leave':
            exitDir()
        case 'closeProgram':
            closeProgram()
        case 'invalid':
            print('Opção inválida.')
            showMenu()

def sendDirectory():
    dirPath = os.getcwd()
    fileList = '()'.join(os.listdir(dirPath))
    if len(fileList) == 0:
        fileList = 'Diretório vazio.'

    connection.send(dirPath.encode()) 
    print('Diretório atual:\n', dirPath)
    connection.send(fileList.encode())
    print('Arquivos no diretório:', fileList)

def showMenu():
    sendDirectory()
    receiveClientCommand()

def receiveFileFromClient():
    print('Recebendo arquivo...')
    if (connection.recv(1024).decode() == 'Arquivo encontrado!'):
        nameFile = connection.recv(1024).decode()
        print('Nome do arquivo:', nameFile)
        with open(nameFile, 'wb') as file:
            print('Arquivo aberto...')
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                file.write(data)
            print('Arquivo recebido!')
    else:
        input('Arquivo não encontrado!')

def sendFileToClient():
    nameFile = connection.recv(1024).decode()
    print(os.getcwd() + "\\" + nameFile)
    try:
        with open(nameFile, 'rb') as file:
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

def deleteFile():
    nameFile = connection.recv(1024).decode()
    os.remove(nameFile)
    print('Arquivo excluído!') 

def enterDir():
    nameFile = connection.recv(1024).decode()
    os.chdir(nameFile)
    print('Diretório acessado!')
    showMenu()

def deleteDir():
    nameFile = connection.recv(1024).decode()
    shutil.rmtree(nameFile)
    print('Diretório excluído!')

def exitDir():
    os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
    print('Saindo do diretório!')
    showMenu()

def closeProgram():
    connection.close()
    print('Conexão encerrada.')
    exit()

#               MAIN                #
# Define o endereço IP e a porta do servidor
match input('Deseja usar o IP padrão? (s/n)'):
    case 's':
        HOST = socket.gethostbyname(socket.gethostname())
    case 'n':
        HOST = input('Digite o IP do servidor: ')
    case _:
        print('Opção inválida. Usando IP padrão.')
        HOST = socket.gethostbyname(socket.gethostname())

PORT = 5444

# Cria um socket e vincula o endereço e a porta
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Escuta a porta
# print('IP do servidor: ', HOST)
print('Esperando por conexão na IP:', HOST, 'e porta:', PORT)
server.listen(1)
connection, address = server.accept()

# Conexão estabelecida
print('Conectado a:', address)
# Menu
showMenu()
# input('Pressione qualquer tecla para sair...')