import mysql.connector 
# funcao que cria a conexao do banco com o crud
def salvar_banco():
          return mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="patp"
            )
          