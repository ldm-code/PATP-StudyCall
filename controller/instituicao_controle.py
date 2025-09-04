
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  
from model.instituicao import instituicao


class InstituicaoController:

    @staticmethod
    def criar_instituicao(nome, cnpj, senha, email, matricula):

        # --- Validação básica ---
        if not nome.strip() or not cnpj.strip() or not senha.strip() or not email.strip():
            raise ValueError("Todos os campos devem ser preenchidos")
        try:
            matricula = int(matricula)
        except ValueError:
            raise ValueError("Matrícula deve ser um número")
        

        facul = instituicao(nome, cnpj, senha, email, matricula)

        return facul
