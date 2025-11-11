from model.usuario import Usuario
from model.instituicao import Instituicao
from model.chamado import Chamado
import sys
import os
from model.chamado import selecionar_chamados


from PyQt5 import QtWidgets

from view.user import Ui_Dialog as Ui_User
from view.telaInicio import Ui_DialogInit
from view.facul import Ui_DialogFacul as Ui_Facul
from view.admin import Ui_DialogAdm as Ui_Adm
from view.chamado_user import ChamadoUser as ChamadoUserView
from view.abrir_chamado import Ui_DialogCreate as Ui_create
from view.chamado_adm import TelaChamadoAdm as ChamadoAdmView


class TelaInicio(QtWidgets.QDialog, Ui_DialogInit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
        self.btnUser.clicked.connect(self.abrir_tela_usuario)
        self.btnAdmin.clicked.connect(self.abrir_tela_adm)
        self.btnInst.clicked.connect(self.abrir_tela_facul)
    def abrir_tela_usuario(self):
        self.hide()
        self.tela_usuario = TelaUsuario()
        self.tela_usuario.exec_() 
    def abrir_tela_facul(self):
        self.hide()
        self.tela_facul=TelaFacul()
        self.tela_facul.exec_()
    def abrir_tela_adm(self):
        self.hide()
        self.tela_adm=TelaAdm()
        self.tela_adm.exec_()
class TelaUsuario(QtWidgets.QDialog, Ui_User):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
        self.btnUserOk.clicked.connect(self.validar_acesso) 
    def validar_acesso(self):
        if self.model():
            self.abrir_tela_chamado()
    def abrir_tela_chamado(self):
    
        self.hide()
        self.tela_chamado = ChamadoUserView() 
        self.tela_chamado.exec_()
class TelaAdm(QtWidgets.QDialog,Ui_Adm):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
        self.admOk.clicked.connect(self.validar_acesso_Tadm)
     def validar_acesso_Tadm(self):
        if self.alt():
            self.abrir_tela_call()
     def abrir_tela_call(self):
         self.hide()
         self.tela_Call=ChamadoAdmView()
         self.tela_Call.exec_()
class TelaFacul(QtWidgets.QDialog,Ui_Facul):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
        self.btnOkFacul.clicked.connect(self.validar_tela)
     def validar_tela(self):
         if self.criar():
             self.abrir_tela_inicial()
     def abrir_tela_inicial(self):
         self.hide()
         self.tela_inicio=TelaInicio()
         self.tela_inicio.exec_()







def main():
    app = QtWidgets.QApplication(sys.argv)
    janela =TelaInicio()
    janela.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()