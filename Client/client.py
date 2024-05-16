import socket

# Pede para o cliente inserir o IP do servidor
# HOST = str(input('Digite o IP do servidor>'))
HOST = '192.168.1.11'
PORT = 5000

def get_file():
    # Pede para o cliente inserir o nome do arquivo a buscar
    namefile = str(input('Buscar arquivo>'))
    connection.send(namefile.encode())

    # Recebe o arquivo
    with open("Client/"+namefile, 'wb') as file:
        while 1:
            data = connection.recv(1000000)
            if not data:
                break
            file.write(data)
        print('Arquivo recebido')

def send_file():
    # Pede para o cliente inserir o nome do arquivo a enviar
    namefile = str(input('Enviar arquivo>'))
    connection.send(namefile.encode())

    # Envia o arquivo
    with open("Client/"+namefile, 'rb') as file:
        data = file.read(1024)
        while data:
            connection.send(data)
            data = file.read(1024)
        connection.send(b'')
        print('Arquivo enviado!')
        




# Cria socket e conecta ao servidor
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))

# Conexão estabelecida
print('Conectado em: {HOST}\n')

send_file()
get_file()

 