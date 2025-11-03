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
import mysql.connector

def selecionar_chamados():
    """
    Retorna os dados dos chamados junto com o nome do usuário.
    Essa função será chamada pela camada de interface (view).
    """

    try:
        # Conecta ao banco de dados
        conexao = banco()
        cursor = conexao.cursor()

        # SELECT com JOIN entre chamados e usuários
        query = """
            SELECT 
                c.id_chamado,
                c.id_adm,
                c.titulo,
                c.descricao,
                c.prioridade,
                c.status_chamado,
                c.local,
                a.nome AS nome_usuario,
                c.data_abertura,
                c.data_fechamento
            FROM chamados c
            INNER JOIN usuario a ON c.fk_usuario = a.id_usuario;
        """

        cursor.execute(query)
        resultados = cursor.fetchall()           # lista de tuplas (cada linha é um chamado)
        colunas = [desc[0] for desc in cursor.description]  # nomes das colunas

        cursor.close()
        conexao.close()

        return colunas, resultados

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar chamados: {erro}")
        return [], [] 
    #codigo abaixo para por na tela criar_chamado que o roblox vai fzr certo
        # self.prioridade_selecionada = None 
        # self.Prio1.clicked.connect(lambda: self.selecionar_prioridade("Baixa"))
        # self.prioMed.clicked.connect(lambda: self.selecionar_prioridade("Média"))
        # self.prioAlta.clicked.connect(lambda: self.selecionar_prioridade("Alta"))

#  def selecionar_prioridade(self,valor):
#          self.prioridade_selecionada = valor
#     def criar(self):
      
#         descricao = self.lineDesc.text()
#         local = self.lineChamado.text()
#         id_user = self.lineId.text()
#         data_abertura = self.lineData.text()
#         prioridade = self.prioridade_selecionada
#         if not prioridade:
#             QtWidgets.QMessageBox.warning(None,'opa','selecione uma prioridade inicial')
#             return
#         if not descricao or not local or not data_abertura or not id_user:
#              QtWidgets.QMessageBox.warning(None,'opa','um dos campos nao foi preenchido')
#              return
#         if not re.fullmatch(r'\d+', id_user):
#             QtWidgets.QMessageBox.warning(None,'ops','id de user invalido')
#             return
#         call=Chamado(descricao=descricao,titulo=)