# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_cadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setStyleSheet("background-color: rgb(138, 5, 190);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_cadastro_logo = QtWidgets.QFrame(self.frame_3)
        self.frame_cadastro_logo.setGeometry(QtCore.QRect(6, 9, 281, 111))
        self.frame_cadastro_logo.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_cadastro_logo.setStyleSheet("background-image: url(:/newPrefix/New Piskel (5).png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.frame_cadastro_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cadastro_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cadastro_logo.setObjectName("frame_cadastro_logo")
        self.label_cadastro_logo = QtWidgets.QLabel(self.frame_cadastro_logo)
        self.label_cadastro_logo.setGeometry(QtCore.QRect(70, -30, 160, 122))
        self.label_cadastro_logo.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_cadastro_logo.setPixmap(QtGui.QPixmap(":/newPrefix/New_Piskel_(5).png"))
        self.label_cadastro_logo.setObjectName("label_cadastro_logo")
        self.frame_cadastro_botao_cadastrar_entrar = QtWidgets.QFrame(self.frame_3)
        self.frame_cadastro_botao_cadastrar_entrar.setGeometry(QtCore.QRect(10, 120, 278, 251))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.frame_cadastro_botao_cadastrar_entrar.setFont(font)
        self.frame_cadastro_botao_cadastrar_entrar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cadastro_botao_cadastrar_entrar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cadastro_botao_cadastrar_entrar.setObjectName("frame_cadastro_botao_cadastrar_entrar")
        self.pushButton_cadastro_cadastrar = QtWidgets.QPushButton(self.frame_cadastro_botao_cadastrar_entrar)
        self.pushButton_cadastro_cadastrar.setGeometry(QtCore.QRect(10, 150, 251, 50))
        self.pushButton_cadastro_cadastrar.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_cadastro_cadastrar.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(115, 115, 115);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(67, 67, 67);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_cadastro_cadastrar.setObjectName("pushButton_cadastro_cadastrar")
        self.pushButton_cadastro_entrar_login = QtWidgets.QPushButton(self.frame_cadastro_botao_cadastrar_entrar)
        self.pushButton_cadastro_entrar_login.setGeometry(QtCore.QRect(80, 210, 118, 16))
        self.pushButton_cadastro_entrar_login.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_cadastro_entrar_login.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"    \n"
"    color: rgb(115, 115, 115);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_cadastro_entrar_login.setObjectName("pushButton_cadastro_entrar_login")
        self.frame_cadastro_dados_cliente = QtWidgets.QFrame(self.frame_cadastro_botao_cadastrar_entrar)
        self.frame_cadastro_dados_cliente.setGeometry(QtCore.QRect(10, 0, 261, 141))
        self.frame_cadastro_dados_cliente.setMinimumSize(QtCore.QSize(0, 125))
        self.frame_cadastro_dados_cliente.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_cadastro_dados_cliente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cadastro_dados_cliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cadastro_dados_cliente.setObjectName("frame_cadastro_dados_cliente")
        self.label_cadastro_string_criar_conta = QtWidgets.QLabel(self.frame_cadastro_dados_cliente)
        self.label_cadastro_string_criar_conta.setGeometry(QtCore.QRect(10, 0, 170, 17))
        self.label_cadastro_string_criar_conta.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadastro_string_criar_conta.setFont(font)
        self.label_cadastro_string_criar_conta.setStyleSheet("QLabel{\n"
"color: rgb(115, 115, 115);\n"
"text-align: center;\n"
"}")
        self.label_cadastro_string_criar_conta.setObjectName("label_cadastro_string_criar_conta")
        self.lineEdit_cadastro_nome = QtWidgets.QLineEdit(self.frame_cadastro_dados_cliente)
        self.lineEdit_cadastro_nome.setGeometry(QtCore.QRect(10, 20, 241, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_cadastro_nome.setFont(font)
        self.lineEdit_cadastro_nome.setStyleSheet("\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:rgb(115,115,115);\n"
"    border-bottom: 2px solid rgb(115,115,115);\n"
"\n"
"}")
        self.lineEdit_cadastro_nome.setInputMask("")
        self.lineEdit_cadastro_nome.setText("")
        self.lineEdit_cadastro_nome.setObjectName("lineEdit_cadastro_nome")
        self.lineEdit_cadastro_sobrenome = QtWidgets.QLineEdit(self.frame_cadastro_dados_cliente)
        self.lineEdit_cadastro_sobrenome.setGeometry(QtCore.QRect(10, 40, 241, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_cadastro_sobrenome.setFont(font)
        self.lineEdit_cadastro_sobrenome.setStyleSheet("\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:rgb(115,115,115);\n"
"    border-bottom: 2px solid rgb(115,115,115);\n"
"\n"
"}")
        self.lineEdit_cadastro_sobrenome.setInputMask("")
        self.lineEdit_cadastro_sobrenome.setText("")
        self.lineEdit_cadastro_sobrenome.setObjectName("lineEdit_cadastro_sobrenome")
        self.lineEdit_cadastro_CPF = QtWidgets.QLineEdit(self.frame_cadastro_dados_cliente)
        self.lineEdit_cadastro_CPF.setGeometry(QtCore.QRect(10, 60, 241, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_cadastro_CPF.setFont(font)
        self.lineEdit_cadastro_CPF.setStyleSheet("\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:rgb(115,115,115);\n"
"    border-bottom: 2px solid rgb(115,115,115);\n"
"\n"
"}")
        self.lineEdit_cadastro_CPF.setInputMask("")
        self.lineEdit_cadastro_CPF.setText("")
        self.lineEdit_cadastro_CPF.setMaxLength(10)
        self.lineEdit_cadastro_CPF.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_cadastro_CPF.setObjectName("lineEdit_cadastro_CPF")
        self.lineEdit_cadastro_CPF_2 = QtWidgets.QLineEdit(self.frame_cadastro_dados_cliente)
        self.lineEdit_cadastro_CPF_2.setGeometry(QtCore.QRect(10, 80, 241, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_cadastro_CPF_2.setFont(font)
        self.lineEdit_cadastro_CPF_2.setStyleSheet("\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:rgb(115,115,115);\n"
"    border-bottom: 2px solid rgb(115,115,115);\n"
"\n"
"}")
        self.lineEdit_cadastro_CPF_2.setInputMask("")
        self.lineEdit_cadastro_CPF_2.setText("")
        self.lineEdit_cadastro_CPF_2.setObjectName("lineEdit_cadastro_CPF_2")
        self.lineEdit_cadastro_CPF_3 = QtWidgets.QLineEdit(self.frame_cadastro_dados_cliente)
        self.lineEdit_cadastro_CPF_3.setGeometry(QtCore.QRect(10, 100, 241, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_cadastro_CPF_3.setFont(font)
        self.lineEdit_cadastro_CPF_3.setStyleSheet("\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:rgb(115,115,115);\n"
"    border-bottom: 2px solid rgb(115,115,115);\n"
"\n"
"}")
        self.lineEdit_cadastro_CPF_3.setInputMask("")
        self.lineEdit_cadastro_CPF_3.setMaxLength(10)
        self.lineEdit_cadastro_CPF_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_cadastro_CPF_3.setObjectName("lineEdit_cadastro_CPF_3")
        self.lineEdit_cadastro_nome.raise_()
        self.lineEdit_cadastro_sobrenome.raise_()
        self.lineEdit_cadastro_CPF.raise_()
        self.lineEdit_cadastro_CPF_2.raise_()
        self.label_cadastro_string_criar_conta.raise_()
        self.lineEdit_cadastro_CPF_3.raise_()
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cadastro"))
        self.label_cadastro_logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/New_Piskel_(5).jpg\"/></p></body></html>"))
        self.pushButton_cadastro_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.pushButton_cadastro_entrar_login.setText(_translate("MainWindow", "Já tem cadastro ? Entrar"))
        self.label_cadastro_string_criar_conta.setText(_translate("MainWindow", "                   Criar sua conta"))
        self.lineEdit_cadastro_nome.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.lineEdit_cadastro_sobrenome.setPlaceholderText(_translate("MainWindow", "Sobreno"))
        self.lineEdit_cadastro_CPF.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.lineEdit_cadastro_CPF_2.setPlaceholderText(_translate("MainWindow", "Digite a senha"))
        self.lineEdit_cadastro_CPF_3.setText(_translate("MainWindow", "confirme a"))
        self.lineEdit_cadastro_CPF_3.setPlaceholderText(_translate("MainWindow", "Confirme a senha"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())