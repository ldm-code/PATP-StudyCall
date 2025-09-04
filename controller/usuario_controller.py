import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  
from model.usuario import Usuario


class UsuarioController:
          @staticmethod
          def criar_user(nome,senha,email,tipo):
                  if not nome.strip() or not senha.strip() or not email.strip() or not tipo.strip():
                          raise ValueError('Um dos campos nao foi preenchido.')
                  tipos=['professor','aluno','Professor','Aluno']
                  if tipo not in tipos:
                          raise ValueError('esse campo so aceita professor ou aluno.')

                  User=Usuario(nome,senha,email,tipo)
                  return User