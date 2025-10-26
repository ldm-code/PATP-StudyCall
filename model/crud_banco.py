import mysql.connector 
print("Importando crud_banco.py")

def banco():

          return mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="patp"
            ) 
          