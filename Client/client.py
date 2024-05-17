import socket

# Define o endereço IP e a porta do servidor
# HOST = '192.168.1.11'
HOST = input('Digite o IP do servidor: ')
PORT = 5000

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
            data = file.read(1024)
            if not data:
                break
            connection.send(data)
        print('Arquivo enviado.')

# Cria um socket e conecta ao servidor
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))

# Conexão estabelecida
print(f'Conectado a: {HOST}\n')

# Envia e recebe arquivos
action = input('Digite "get" para baixar um arquivo ou "send" para enviar um arquivo: ')

if action == 'get':
    get_file()
elif action == 'send':
    send_file()

# Fecha a conexão
connection.close()
input('Pressione qualquer tecla para sair...')
