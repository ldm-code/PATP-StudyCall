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
         def __init__(self, descricao, titulo, prioridade, local, id_user, data_abertura, data_fechamento, id_adm, status='em aberto'):
               super().__init__(descricao, titulo, prioridade, local, id_user, data_abertura, data_fechamento, id_adm, status)
         def pegar_id_chamado(self,id):
            try:
              conexao=banco()
              cursor=conexao.cursor()
              sql = "SELECT id_chamado FROM chamados WHERE id_chamado  = %s"
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
         def atualizar_chamado(self, id):
          try:
            conexao = banco()
            cursor = conexao.cursor()

            sql = """
            UPDATE chamados
            SET 
                prioridade = COALESCE(%s, prioridade),
                data_fechamento = COALESCE(%s, data_fechamento),
                id_adm = COALESCE(%s, id_adm),
                status_chamado = COALESCE(%s, status_chamado)
            WHERE id_chamado = %s
            """

            valores = (
                self.prioridade,
                self.data_fechamento,
                self.id_adm,
                self.status,
                id
              
            )

            cursor.execute(sql, valores)
            conexao.commit()

          except mysql.connector.Error as e:
            print(f"Erro ao atualizar chamado: {e}")
          finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


def selecionar_chamados():
   

    try:
       
        conexao = banco()
        cursor = conexao.cursor()

        query = """
            SELECT 
                c.id_chamado,
                adm.nome AS nome_adm,
                c.titulo,
                c.descricao,
                c.prioridade,
                c.status_chamado,
                c.local,
                a.nome AS nome_usuario,
                c.data_abertura,
                c.data_fechamento
            FROM chamados c
            INNER JOIN usuario a ON c.fk_usuario = a.id_usuario
            LEFT JOIN adm ON c.id_adm = adm.id_adm;;
        """

        cursor.execute(query)
        resultados = cursor.fetchall()           
        colunas = [desc[0] for desc in cursor.description]  

        cursor.close()
        conexao.close()

        return colunas, resultados

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar chamados: {erro}")
        return [], [] 
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
         def __init__(self, descricao, titulo, prioridade, local, id_user, data_abertura, data_fechamento, id_adm, status='em aberto'):
               super().__init__(descricao, titulo, prioridade, local, id_user, data_abertura, data_fechamento, id_adm, status)
         def pegar_id_chamado(self,id):
            try:
              conexao=banco()
              cursor=conexao.cursor()
              sql = "SELECT id_chamado FROM chamados WHERE id_chamado  = %s"
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
         def atualizar_chamado(self, id):
          try:
            conexao = banco()
            cursor = conexao.cursor()

            sql = """
            UPDATE chamados
            SET 
                prioridade = COALESCE(%s, prioridade),
                data_fechamento = COALESCE(%s, data_fechamento),
                id_adm = COALESCE(%s, id_adm),
                status_chamado = COALESCE(%s, status_chamado)
            WHERE id_chamado = %s
            """

            valores = (
                self.prioridade,
                self.data_fechamento,
                self.id_adm,
                self.status,
                id
              
            )

            cursor.execute(sql, valores)
            conexao.commit()

          except mysql.connector.Error as e:
            print(f"Erro ao atualizar chamado: {e}")
          finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
def selecionar_chamados():
   

    try:
       
        conexao = banco()
        cursor = conexao.cursor()

        query = """
            SELECT 
                c.id_chamado,
                adm.nome AS nome_adm,
                c.titulo,
                c.descricao,
                c.prioridade,
                c.status_chamado,
                c.local,
                a.nome AS nome_usuario,
                c.data_abertura,
                c.data_fechamento
            FROM chamados c
            INNER JOIN usuario a ON c.fk_usuario = a.id_usuario
            LEFT JOIN adm ON c.id_adm = adm.id_adm;;
        """

        cursor.execute(query)
        resultados = cursor.fetchall()           
        colunas = [desc[0] for desc in cursor.description]  

        cursor.close()
        conexao.close()

        return colunas, resultados

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar chamados: {erro}")
        return [], [] 

