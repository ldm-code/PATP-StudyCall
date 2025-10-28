from model.usuario import Usuario
from model.instituicao import Instituicao
from model.chamado import Chamado

from PyQt5 import QtWidgets
import sys
from view.user import Ui_Dialog as Ui_User
from view.telaInicio import Ui_DialogInit


class TelaInicio(QtWidgets.QDialog, Ui_DialogInit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
        self.btnUser.clicked.connect(self.abrir_tela_usuario)
    def abrir_tela_usuario(self):
        self.hide()
        self.tela_usuario = TelaUsuario()
        self.tela_usuario.exec_() 
class TelaUsuario(QtWidgets.QDialog, Ui_User):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
def main():
    app = QtWidgets.QApplication(sys.argv)
    janela = TelaInicio()
    janela.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
