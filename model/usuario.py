import mysql.connector


from model.crud_banco import banco
class Usuario:
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo   

    def salvar(self): 
         
        try:
            
            conexao = banco()
           
            cursor = conexao.cursor()
           
            sql = "INSERT INTO usuario (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)"
            valores = (self.nome, self.email, self.senha, self.tipo)
          

            cursor.execute(sql, valores)
            

            conexao.commit()
           

            return cursor.lastrowid
        except mysql.connector.Error as erro:
            print(f" Erro ao salvar usuário: {erro}")
        finally:
            if cursor:
                
                cursor.close()
               
            if conexao:
          
                conexao.close()
                     
