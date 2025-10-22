import mysql.connector 

def salvar_banco():
          return mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="patp"
            )
          