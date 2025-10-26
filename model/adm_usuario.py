import mysql.connector

from model .crud_banco import banco

class Adm:
          def __init__(self,nome,senha,instituicao,email,matricula):
                  self.nome=nome
                  self.senha=senha
                  self.instituicao=instituicao
                  self.matricula=matricula
                  self.email=email
           
          def salvar(self):
           try:
                 conexao = banco()
                 cursor = conexao.cursor()

                 comando = "INSERT INTO adm_usuario(nome,senha,instituicao,matricula,email) VALUES(%s,%s,%s,%s,%s)"
                 dados=(self.nome,self.senha,self.instituicao,self.matricula,self.email)
                 cursor.execute(comando,dados)
                 conexao.commit()
                 print("moderador tira o mlk desse gp agr!!!!!!!!")

           except mysql.connector.Error as erro:
                print(f" Erro ao salvar usuário: {erro}")
           finally:
             if cursor:
                cursor.close()
             if conexao:
                conexao.close()

             