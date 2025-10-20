from model.usuario import Usuario
from model.instituicao import Instituicao
from model.chamado import Chamado

from PyQt5 import QtWidgets
import sys
from view.user import Ui_Dialog  # importa a tela do usuário

def main():
    # Cria a aplicação Qt
    app = QtWidgets.QApplication(sys.argv)

    # Cria a janela de diálogo (base da interface)
    janela = QtWidgets.QDialog()

    # Cria o objeto da tela gerada pelo Qt Designer
    tela = Ui_Dialog()

    # Configura os elementos da interface na janela
    tela.setupUi(janela)

    # Exibe a janela na tela
    janela.show()

    # Mantém o programa rodando até o usuário fechar
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


