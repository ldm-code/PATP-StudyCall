class Usuario:
          def __init__(self,nome,email,senha,tipo='aluno'):
                  self.nome=nome
                  self.email=email
                  self.senha=senha
                  self.tipo=tipo   
          def atualizar(self,novo_tipo) :
                  tipos=['aluno','professor']  
                  if novo_tipo in tipos:
                          self.tipo=novo_tipo 