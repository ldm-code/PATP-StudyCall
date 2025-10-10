import mysql.connector
from model.crud_banco import salvar_banco
class Instituicao:
          def __init__(self,nome,senha,matricula,cnpj,email):
                  self.nome=nome
                  self.cnpj=cnpj
                  self.senha=senha
                  self.email=email
                  self.matricula=matricula
          def salvar(self):
              try:
                  conexao=salvar_banco()
                  cursor=conexao.cursor()
                  comando="INSERT INTO instituicao(nome,senha,matricula,CNPJ,email) VALUES(%s,%s,%s,%s,%s)"
                  dados=( self.nome ,self.senha,self.matricula,self.cnpj,self.email)
                  cursor.execute(comando,dados)
                  conexao.commit()
                  print("salvou os dados com sucesso")
              except mysql.connector.Error as e:
                     print(f"erro !,{e}")
              finally:
                     if cursor:
                            cursor.close()
                     if conexao:
                            conexao.close()

                     
