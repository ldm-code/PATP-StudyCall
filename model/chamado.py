import mysql.connector

from model .crud_banco import banco

class Chamado:
          def __init__(self,descricao,titulo,prioridade,local,id_user,data_abertura,data_fechamento,status='em aberto'):
                  self.descricao=descricao
                  self.titulo=titulo
                  self.prioridade=prioridade
                  self.local=local
                  self.id_user=id_user
                  self.status=status
                  self.data_abertura=data_abertura
                  self.data_fechamento=data_fechamento
          def salvar(self):
            try:
                conexao = banco()
                cursor = conexao.cursor()
                print("Tipo de fk_usuario:", type(self.id_user))
                print("Valor de fk_usuario:", self.id_user)
                comando = "INSERT INTO chamados(descricao,titulo,prioridade,local,fk_usuario,status_chamado,data_abertura,data_fechamento) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                dados=(self.descricao,self.titulo,self.prioridade,self.local,self.id_user,self.status,self.data_abertura,self.data_fechamento)
                cursor.execute(comando,dados)
                conexao.commit()
                print("funcionou")

            except mysql.connector.Error as erro:
              print(f" Erro ao salvar : {erro}")
            finally:
             if cursor:
                cursor.close()
             if conexao:
                conexao.close()

             

 
                               
                  