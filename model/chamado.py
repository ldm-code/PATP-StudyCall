import mysql.connector

from model .crud_banco import salvar_banco

class Chamado:
          def __init__(self,descricao,titulo,prioridade,local,data_abertura,data_fechamento,status='em aberto'):
                  self.descricao=descricao
                  self.titulo=titulo
                  self.prioridade=prioridade
                  self.local=local
                  self.status=status
                  self.data_abertura=data_abertura
                  self.data_fechamento=data_fechamento
          def salvar(self):
            try:
                conexao = salvar_banco()
                cursor = conexao.cursor()

                comando = "INSERT INTO chamados(descricao,titulo,prioridade,local,status_chamado,data_abertura,data_fechamento) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                dados=(self.descricao,self.titulo,self.prioridade,self.local,self.status,self.data_abertura,self.data_fechamento)
                cursor.execute(comando,dados)
                conexao.commit()
                print("roblox achou a calcinha")

            except mysql.connector.Error as erro:
              print(f" Erro ao salvar usuário: {erro}")
            finally:
             if cursor:
                cursor.close()
             if conexao:
                conexao.close()

             

 
                               
                  