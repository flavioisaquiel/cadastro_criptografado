
import mysql.connector
import secrets
import getpass
import hashlib
from hashlib import sha256
from string import digits


numeros = digits

# gerando Id aleatório
registro = ''.join(secrets.choice(numeros) for _ in range(6))
Id = registro

Nome = input('Digite seu Nome : ')
Senha = getpass.getpass('Digite Uma Senha : ') # digitando senha sem aparecer os caracteres

hashed_password = hashlib.sha256(Senha.encode()).hexdigest() # criptografando a senha
# armazenando no mySql
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='xxxxxxx',
    database='dados',
)
cursor = conexao.cursor()

comando = f'INSERT INTO cadastros ( Nome,Id,Senha) VALUES (%s,%s,%s)'
valores = (Nome, Id, hashed_password,)

#executando o comando
cursor.execute(comando, valores)
conexao.commit()
# fechando cursor e conexão com bando de dados
cursor.close()
conexao.close()


