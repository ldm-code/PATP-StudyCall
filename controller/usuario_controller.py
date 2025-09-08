import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  
from model.usuario import Usuario


class UsuarioController:
          @staticmethod
          def criar_user(nome,email,senha,tipo):
                  if not nome.strip() or not senha.strip() or not email.strip() or not tipo.strip():
                          raise ValueError('Um dos campos nao foi preenchido.')
                  tipo=tipo.lower()
                  tipos=['professor','aluno']
                  if tipo not in tipos:
                          raise ValueError('esse campo so aceita professor ou aluno.')
                  User=Usuario(nome,email,senha,tipo)
                  return User