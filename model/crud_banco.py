import mysql.connector 


def banco():

          return mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="patp"
            ) 
          