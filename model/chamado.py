import mysql.connector

from model.crud_banco import banco

class Chamado:
          def __init__(self,descricao,titulo,prioridade,local,id_user,data_abertura,data_fechamento,id_adm,status='em aberto'):
                  self.descricao=descricao
                  self.titulo=titulo
                  self.prioridade=prioridade
                  self.local=local
                  self.id_user=id_user
                  self.data_abertura=data_abertura
                  self.data_fechamento=data_fechamento
                  self.id_adm=id_adm
                  self.status=status
          def pegar_id_user(self):
            try:
              conexao=banco()
              cursor=conexao.cursor()
              sql = "SELECT id_usuario FROM usuario WHERE id_usuario  = %s"
              cursor.execute(sql,(self.id_user,))
              resultado = cursor.fetchone()
              if resultado:
                  return resultado[0]
              else:
                  return None
            except mysql.connector.Error as e:
                              print(f"Erro ao buscar ID: {e}")
                              return None
            finally:
                    if cursor: 
                         cursor.close()
                    if conexao: 
                         conexao.close()
          def salvar(self):
            try:
                conexao = banco()
                cursor = conexao.cursor()
                comando = "INSERT INTO chamados(descricao,titulo,prioridade,local,fk_usuario,status_chamado,data_abertura) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                dados=(self.descricao,self.titulo,self.prioridade,self.local,self.id_user,self.status,self.data_abertura)
                cursor.execute(comando,dados)
                conexao.commit()
                

            except mysql.connector.Error as erro:
              print(f" Erro ao salvar : {erro}")
            finally:
             if cursor:
                cursor.close()
             if conexao:
                conexao.close()
class ChamadoAssumido(Chamado):
         def pegar_id_chamado(self,id):
            try:
              conexao=banco()
              cursor=conexao.cursor()
              sql = "SELECT id_chamado FROM chamado WHERE id_chamado  = %s"
              cursor.execute(sql,(id,))
              resultado = cursor.fetchone()
              if resultado:
                  return resultado[0]
              else:
                  return None
            except mysql.connector.Error as e:
                              print(f"Erro ao buscar ID: {e}")
                              return None
            finally:
                    if cursor: 
                         cursor.close()
                    if conexao: 
                         conexao.close()
                               
                  
         def pegar_id_adm(self):
            try:
              conexao=banco()
              cursor=conexao.cursor()
              sql = "SELECT id_adm FROM adm WHERE id_adm  = %s"
              cursor.execute(sql,(self.id_adm,))
              resultado = cursor.fetchone()
              if resultado:
                  return resultado[0]
              else:
                  return None
            except mysql.connector.Error as e:
                              print(f"Erro ao buscar ID: {e}")
                              return None
            finally:
                    if cursor: 
                         cursor.close()
                    if conexao: 
                         conexao.close()
