from model.usuario import Usuario
nome=input("seu nome:")
email=input("seu email:")
senha=input('sua senha:')
professor=input("seu tipo:")
user=Usuario(nome,email,senha,professor)
user.salvar()
