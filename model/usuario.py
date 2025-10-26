import mysql.connector
print("Importando usuario.py")

from model.crud_banco import banco
class Usuario:
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo   

    def salvar(self): 
         
        try:
            print("1️⃣ Chamando salvar_banco()")
            conexao = banco()
            print("nao qubera aqui")
            cursor = conexao.cursor()
            print("cursor e conexao criadas")
            sql = "INSERT INTO usuario (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)"
            valores = (self.nome, self.email, self.senha, self.tipo)
            print("dados recebidos")

            cursor.execute(sql, valores)
            print("quarry feita")

            conexao.commit()
            print("deu commit")

            return cursor.lastrowid
        except mysql.connector.Error as erro:
            print(f" Erro ao salvar usuário: {erro}")
        finally:
            if cursor:
                print("fechando cursor")
                cursor.close()
                print("fechou o cursor")
            if conexao:
                print("iniciando encerramento")
                conexao.close()
                print("fechou a conexao")       
