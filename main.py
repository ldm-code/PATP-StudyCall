from model.usuario import Usuario
from model.instituicao import Instituicao
nome=input("seu nome:")
email=input("seu email:")
senha=input('sua senha:')
professor=input("seu tipo:")
user=Usuario(nome,email,senha,professor)
user.salvar()
facul=Instituicao("ideau","1234","69696969","000-0000-000","ideau@gmail.com")
facul.salvar()
