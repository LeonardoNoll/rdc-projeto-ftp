import socket

HOST = '192.168.1.9'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', PORT))
server.listen(1)

print ('Esperando o cliente no servidor: ', HOST,'e porta: ', PORT)
connection, adress = server.accept()

print ('Conectado em: ', adress)

namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)
    
    print('Arquivo enviado!')

# while True:
#     data = conn.recv(1024)
#     if not data:
#         print ('Fechando a conexao')
#         conn.close()
#         break
#     conn.sendall(data)