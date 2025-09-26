import mysql.connector

class Usuario:
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo   
    
    def salvar(self):          
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="patp"
            )
            cursor = conexao.cursor()
            sql = "INSERT INTO usuario (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)"
            valores = (self.nome, self.email, self.senha, self.tipo)
            cursor.execute(sql, valores)
            conexao.commit()
            print("Usuário salvo com sucesso!")
        except mysql.connector.Error as erro:
            print(f" Erro ao salvar usuário: {erro}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
