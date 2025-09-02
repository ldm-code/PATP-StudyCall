from PyQt5 import QtWidgets
from view.interface_inicial import Ui_Form as UiInicial
from view.interface_user import Ui_Form as UiUser
from view.interface_instituicao import Ui_Form as UiInstituicao
class MainApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.tela_inicial = UiInicial()
        self.tela_inicial.setupUi(self)
        self.tela_inicial.usuario.clicked.connect(self.abrir_tela_usuario)
        self.tela_inicial.instituicao.clicked.connect(self.abrir_tela_facul)
    def abrir_tela_usuario(self):
        self.tela_usuario = QtWidgets.QWidget()
        self.ui_usuario = UiUser()
        self.ui_usuario.setupUi(self.tela_usuario)
        self.tela_usuario.show()
        self.close()
    def abrir_tela_facul(self):
        self.tela_instituicao=QtWidgets.QWidget()
        self.ui_instituicao=UiInstituicao()
        self.ui_instituicao.setupUi(self.tela_instituicao)
        self.tela_instituicao.show()
        self.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())

