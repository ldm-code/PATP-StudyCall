from model.usuario import Usuario
from model.instituicao import Instituicao
from model.chamado import Chamado

from PyQt5 import QtWidgets
import sys
from view.user import Ui_Dialog  

def main():

    app = QtWidgets.QApplication(sys.argv)


    janela = QtWidgets.QDialog()


    tela = Ui_Dialog()


    tela.setupUi(janela)


    janela.show()


    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


