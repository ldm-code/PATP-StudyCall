from PyQt5 import QtCore, QtGui, QtWidgets
from model.usuario import Usuario,selecionar_ultimo_id


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 412)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-150, -160, 761, 611))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnUserOk = QtWidgets.QPushButton(self.frame)
        self.btnUserOk.setGeometry(QtCore.QRect(370, 480, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnUserOk.setFont(font)
        self.btnUserOk.setStyleSheet("background-color: rgb(35, 173, 4);\n"
"border-radius: 15px;\n"
" border: 2px solid black;")
        self.btnUserOk.setObjectName("btnUserOk")
       
        self.lineNome = QtWidgets.QLineEdit(self.frame)
        self.lineNome.setGeometry(QtCore.QRect(260, 260, 331, 22))
        self.lineNome.setText("")
        self.lineNome.setObjectName("lineNome")
        self.lineNome.setPlaceholderText('seu nome:')
        self.lineEmail = QtWidgets.QLineEdit(self.frame)
        self.lineEmail.setGeometry(QtCore.QRect(260, 310, 331, 22))
        self.lineEmail.setText("")
        self.lineEmail.setObjectName("lineEmail")
        self.lineEmail.setPlaceholderText('seu email:(xx@gmail.com):')
        self.lineSenha = QtWidgets.QLineEdit(self.frame)
        self.lineSenha.setGeometry(QtCore.QRect(260, 360, 331, 22))
        self.lineSenha.setText("")
        self.lineSenha.setObjectName("lineSenha")
        self.lineSenha.setPlaceholderText('sua senha:')
        self.rbProfessor = QtWidgets.QRadioButton("Professor", self.frame)
        self.rbProfessor.setGeometry(QtCore.QRect(260, 410, 150, 22))  
        self.rbProfessor.setStyleSheet("background-color: rgb(188, 255, 137); border-radius: 10px;")
        self.rbProfessor.setObjectName("rbProfessor")
        self.rbAluno = QtWidgets.QRadioButton("Aluno", self.frame)
        self.rbAluno.setGeometry(QtCore.QRect(410, 410, 150, 22)) 
        self.rbAluno.setStyleSheet("background-color: rgb(188, 255, 137); border-radius: 10px;")
        self.rbAluno.setObjectName("rbAluno")
        self.nomeUser = QtWidgets.QLabel(self.frame)
        self.nomeUser.setGeometry(QtCore.QRect(400, 240, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nomeUser.setFont(font)
        self.nomeUser.setObjectName("nomeUser")
        self.emailUser = QtWidgets.QLabel(self.frame)
        self.emailUser.setGeometry(QtCore.QRect(400, 290, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.emailUser.setFont(font)
        self.emailUser.setObjectName("emailUser")
        self.senhaUser = QtWidgets.QLabel(self.frame)
        self.senhaUser.setGeometry(QtCore.QRect(400, 340, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.senhaUser.setFont(font)
        self.senhaUser.setObjectName("senhaUser")
        self.tipoUser = QtWidgets.QLabel(self.frame)
        self.tipoUser.setGeometry(QtCore.QRect(400, 390, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tipoUser.setFont(font)
        self.tipoUser.setObjectName("tipoUser")
        self.verdeUserB = QtWidgets.QFrame(self.frame)
        self.verdeUserB.setGeometry(QtCore.QRect(140, 540, 771, 51))
        self.verdeUserB.setStyleSheet("background-color: rgb(25, 170, 0);")
        self.verdeUserB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verdeUserB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verdeUserB.setObjectName("verdeUserB")
        self.verdeUserC = QtWidgets.QFrame(self.frame)
        self.verdeUserC.setGeometry(QtCore.QRect(130, 160, 771, 51))
        self.verdeUserC.setStyleSheet("background-color: rgb(25, 170, 0);")
        self.verdeUserC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verdeUserC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verdeUserC.setObjectName("verdeUserC")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnUserOk.setText(_translate("Dialog", "ok"))
        self.nomeUser.setText(_translate("Dialog", "Nome:"))
        self.emailUser.setText(_translate("Dialog", "Email:"))
        self.senhaUser.setText(_translate("Dialog", "Senha:"))
        self.tipoUser.setText(_translate("Dialog", "Tipo:"))
    def model(self):
        
        nome=self.lineNome.text().strip()
        email=self.lineEmail.text().strip()
        senha=self.lineSenha.text().strip()
        if self.rbProfessor.isChecked():
             tipo = "professor"
        elif self.rbAluno.isChecked():
             tipo = "aluno"
        else:
            QtWidgets.QMessageBox.warning(None, "Tipo inválido", "Selecione se você é professor ou aluno.")
            return False
     
        if not nome or not email or not senha :

            QtWidgets.QMessageBox.warning(None, "Campos vazios", "Preencha todos os campos antes de salvar!")
           
            return False
    
        
        usuario=Usuario(nome=nome,email=email,senha=senha,tipo=tipo)
        try:
          usuario.salvar()
         
          nome_user=usuario.senha
          email_user=usuario.email
          msg=f"""
          Usuario salvo com sucesso!
          senha: {nome_user}
          email: {email_user}
          * email e senha necessario para criar cadastro
          """
          QtWidgets.QMessageBox.information(None,"bem vindo",msg)
          return True
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Erro ao salvar", f"Ocorreu um erro: {str(e)}")
            return False
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())