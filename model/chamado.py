class chamado:
          def __init__(self,descricao,titulo,usuario,prioridade,tempo_estimado,local,instituicao,status='em aberto'):

                  self.descricao=descricao
                  self.titulo=titulo
                  self.usuario=usuario #relacionamento de usuario
                  self.prioridade=prioridade
                  self.tempo_estimado=tempo_estimado #relacionamento de admin
                  self.local=local
                  self.status=status
          def atualizar(self,novo_status,nova_prioridade,novo_tempo):
                  stats=['resolvido','em aberto']
                  self.tempo_estimado=novo_tempo
                  if novo_status in stats:
                      self.status=novo_status
                  prioridades=[1,2,3]
                  if nova_prioridade in prioridades:
                          self.prioridade=nova_prioridade
                               
                  