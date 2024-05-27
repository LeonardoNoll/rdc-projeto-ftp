import os
import shutil

# os.mkdir('teste')
# os.rmdir('teste')
# shutil.rmtree('teste')
print(os.getcwd())
lista_arquivos = os.listdir(os.getcwd())
for arquivo in lista_arquivos:
    print(">",arquivo)

diretorio = input('Digite o nome do diretório a ser acessado: ')
print(os.getcwd() +"\\" + diretorio)
os.chdir(os.getcwd() +"\\" + diretorio)
print(os.getcwd())
