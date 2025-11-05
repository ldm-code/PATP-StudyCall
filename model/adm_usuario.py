import mysql.connector

from model.crud_banco import banco

class Adm:
          def __init__(self,nome,senha,instituicao,matricula,email):
                  self.nome=nome
                  self.senha=senha
                  self.instituicao=instituicao
                  self.matricula=matricula
                  self.email=email
          def pegar_id_instituicao(self):
               try:

                    conexao = banco()
                    cursor = conexao.cursor()
                    sql = "SELECT id_instituicao FROM instituicao WHERE id_instituicao = %s"
                    cursor.execute(sql, (self.instituicao,))
                    resultado = cursor.fetchone()
                    if resultado:
                      return resultado[0]  
                    else:
                         
                         return None
               except mysql.connector.Error as e:
                              print(f"Erro ao buscar ID da instituição: {e}")
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
                 comando = "INSERT INTO adm(nome,senha,instituicao,matricula,email) VALUES(%s,%s,%s,%s,%s)"
                 dados=(self.nome,self.senha,self.instituicao,self.matricula,self.email)
                 cursor.execute(comando,dados)
                 conexao.commit()
                 return cursor.lastrowid

           except mysql.connector.Error as erro:
                print(f" Erro ao salvar usuário: {erro}")
           finally:
             if cursor:
                cursor.close()
             if conexao:
                conexao.close()
def selecionar_ultimo_id_adm():
    try:
        conexao = banco()
      

        cursor = conexao.cursor()
        cursor.execute("SELECT id_adm FROM adm ORDER BY id_adm DESC LIMIT 1;")
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            return None

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar último ID: {erro}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexao:
           conexao.close()
                   

