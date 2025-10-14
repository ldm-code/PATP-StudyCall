import mysql.connector
from model.crud_banco import salvar_banco #chamando a funcao no codigo
class Instituicao:
          def __init__(self,nome,senha,matricula,cnpj,email):
                  self.nome=nome
                  self.cnpj=cnpj
                  self.senha=senha
                  self.email=email
                  self.matricula=matricula
          def salvar(self): # modulo que salva no banco
              try: # try e exept para tratar erros do banco,nada diretamente ligado ao curd
                  conexao=salvar_banco() #criando a conexao com a funcao que criamos
                  cursor=conexao.cursor() #criando o cursor para executar o comanco
                  comando="INSERT INTO instituicao(nome,senha,matricula,CNPJ,email) VALUES(%s,%s,%s,%s,%s)"
                  # variavel comando para executar a querry (comando mysql)
                  dados=( self.nome ,self.senha,self.matricula,self.cnpj,self.email) # passando os dados da classe
                  cursor.execute(comando,dados) #executando a querry para enviar dados ao banco
                  conexao.commit()# comando que finaliza a querry
                  print("salvou os dados com sucesso")
              except mysql.connector.Error as e:#tratamento de erros
                     print(f"erro !,{e}")
              finally:# fechamento do cursor e da conexao
                     if cursor:
                            cursor.close()
                     if conexao:
                            conexao.close()

                     
