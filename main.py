from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("teste", "senha", r"C:\Users\Desktop\Desktop\testeServidor", "elradr")

handler = FTPHandler
handler.authorizer = authorizer

with FTPServer(("192.168.1.11", 21), handler) as server:
    server.max_cons = 5
    server.max_cons_per_ip = 2
    server.serve_forever()
