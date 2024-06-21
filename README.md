# Implementação de protocolo de Transferência de Arquivos (FTP) em Python

## Descrição
Implementação de um protocolo de transferência de arquivos (FTP) em Python, utilizando sockets TCP. Dividido em duas partes: cliente e servidor.

## Funcionalidades
- Listar arquivos no servidor
- Enviar arquivos do cliente para o servidor
- Baixar arquivos do servidor para o cliente
- Deletar arquivos no servidor
- Deletar diretórios no servidor
- Navegar entre diretórios no servidor

## Métodos de execução
### 1. Uso de arquivos .py por terminal
Em uma máquina denominada servidor, execute o arquivo `server.py`:
```bash 
python server.py
```
Com o servidor aberto, em uma maquina cliente na mesma rede,execute o arquivo `client.py`:
```bash
python client.py
```
### 2. Uso de executáveis
Em uma máquina denominada servidor, execute o arquivo `server.exe`:


Com o servidor aberto, em uma maquina cliente na mesma rede,execute o arquivo `client.exe`:

## Precauções de uso
- Certifique-se de que o servidor está na mesma rede que o cliente
- Para o uso de `.py`, é necessário que o Python esteja instalado na máquina
- Utilizando o método de `.py`, a navegação de diretório começara no diretório atual do **terminal**, e não necessariamente no diretório do arquivo `.py`. Isto vale tanto para o servidor quanto para o cliente.
- Utilizando o método de `.exe`, a navegação de diretório começara no diretório do arquivo `.exe`. Isto vale tanto para o servidor quanto para o cliente.