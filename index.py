import mysql.connector

#cria conexao entre banco de dados e python
conexao = mysql.connector.connect (
    host = 'localhost', 
    user = 'root',
    password = '28736ahjsbdnbzxc129-03',
    database = 'bdyoutube',
)

cursor = conexao.cursor()#cria o cursor da conexao

#CREATE
def create(nome_produto, valor):    
    comando = f'INSERT INTO vendas(Nome_produto, Valor) VALUES("{nome_produto}",{valor})'
    cursor.execute(comando)
    conexao.commit()#edita o banco de dados

#READ
def read(comando):    
    cursor.execute(comando)
    resultado = cursor.fetchall()#ler o banco de dados
    print(resultado)

#UPDATE
def update(comando):
   cursor.execute(comando)
   conexao.commit()#edita o banco de dados

#DELETE
def delete(comando):
    cursor.execute(comando)
    conexao.commit()



cursor.close()#encerra cursor
conexao.close()#encerra conexao