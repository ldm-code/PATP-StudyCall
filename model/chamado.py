import _mysql_connector

from model .crud_banco import salvar_banco

class chamado:
          def __init__(self,descricao,titulo,usuario,prioridade,local,instituicao,status='em aberto'):

                  self.descricao=descricao
                  self.titulo=titulo
                  self.usuario=usuario 
                  self.prioridade=prioridade
                  self.local=local
                  self.status=status
          def atualizar(self,novo_status,nova_prioridade,novo_tempo):
                  stats=['resolvido','em aberto','em andamento']
                  self.tempo_estimado=novo_tempo
                  if novo_status in stats:
                      self.status=novo_status
                  prioridades=['baixa','média','alta']
                  if nova_prioridade in prioridades:
                          self.prioridade=nova_prioridade
          def salvar(self):
                conexao = salvar_banco()
                cursor = conexao.cursor()


 
                               
                  