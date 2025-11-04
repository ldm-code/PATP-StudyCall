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
from view.chamado_user import Ui_DialogCall
from view.abrir_chamado import Ui_DialogCreate as Ui_create
from view.chamado_adm import Ui_DialogSelect  


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
        self.btnUserOk.clicked.connect(self.abrir_tela_chamado) 
    def abrir_tela_chamado(self):
        self.hide()
        self.tela_chamado = ChamadoUser() 
        self.tela_chamado.exec_()

class TelaAdm(QtWidgets.QDialog,Ui_Adm):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
        self.admOk.clicked.connect(self.abrir_tela_call)
     def abrir_tela_call(self):
         self.hide()
         self.tela_Call=TelaChamadoAdm()
         self.tela_Call.exec_()
class TelaFacul(QtWidgets.QDialog,Ui_Facul):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")
        self.btnOkFacul.clicked.connect(self.abrir_tela_inicial)
     def abrir_tela_inicial(self):
         self.hide()
         self.tela_inicio=TelaInicio()
         self.tela_inicio.exec_()
class ChamadoUser(QtWidgets.QDialog,Ui_DialogCall):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogCall()
        self.ui.setupUi(self)
        self.setWindowTitle("StudyCall - Usuario")

        self.ui.btnCreateCall.clicked.connect(self.abrir_tela_criar)
        self.mostrar_chamados()

    def mostrar_chamados(self):
        colunas, resultados = selecionar_chamados()

        self.ui.tableWidget.setRowCount(len(resultados))
        self.ui.tableWidget.setColumnCount(len(colunas))
        self.ui.tableWidget.setHorizontalHeaderLabels(colunas)

        for linha_idx, linha_dados in enumerate(resultados):
            for coluna_idx, valor in enumerate(linha_dados):
                self.ui.tableWidget.setItem(linha_idx, coluna_idx, QtWidgets.QTableWidgetItem(str(valor)))

        self.ui.tableWidget.resizeColumnsToContents()
    def abrir_tela_criar(self):

        self.tela_criar = TelaChamadoCriar()
        self.tela_criar.exec_()

class TelaChamadoCriar(QtWidgets.QDialog,Ui_create):
      def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("StudyCall")




class TelaChamadoAdm(QtWidgets.QDialog,Ui_DialogSelect):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogSelect()
        self.ui.setupUi(self)
        self.setWindowTitle("StudyCall - Administrador")


        self.carregar_chamados()


    def carregar_chamados(self):
     
        try:
            colunas, resultados = selecionar_chamados()  
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar chamados:\n{e}")
            return

        tabela = self.ui.banco_adm
        tabela.setRowCount(len(resultados))
        tabela.setColumnCount(len(colunas))
        tabela.setHorizontalHeaderLabels(colunas)

        for i, linha in enumerate(resultados):
            for j, valor in enumerate(linha):
                tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor)))

        tabela.resizeColumnsToContents()

    def assumir_chamado(self):
        linha = self.ui.banco_adm.currentRow()
        if linha < 0:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um chamado para assumir.")
            return
        id_chamado = self.ui.banco_adm.item(linha, 0).text()
        QtWidgets.QMessageBox.information(self, "Chamado", f"Chamado {id_chamado} assumido!")

def main():
    app = QtWidgets.QApplication(sys.argv)
    janela = TelaInicio()
    janela.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
