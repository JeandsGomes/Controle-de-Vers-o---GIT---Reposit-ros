# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setStyleSheet("background-color: rgb(138, 5, 190);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_login_logo = QtWidgets.QLabel(self.frame)
        self.label_login_logo.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_login_logo.setText("")
        self.label_login_logo.setPixmap(QtGui.QPixmap("New_Piskel_(5).jpg"))
        self.label_login_logo.setObjectName("label_login_logo")
        self.horizontalLayout_2.addWidget(self.label_login_logo)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_login_cpf_cliente = QtWidgets.QFrame(self.frame_3)
        self.frame_login_cpf_cliente.setMinimumSize(QtCore.QSize(0, 125))
        self.frame_login_cpf_cliente.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_login_cpf_cliente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_cpf_cliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_cpf_cliente.setObjectName("frame_login_cpf_cliente")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_login_cpf_cliente)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_login_string_fazer_login = QtWidgets.QLabel(self.frame_login_cpf_cliente)
        self.label_login_string_fazer_login.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_login_string_fazer_login.setFont(font)
        self.label_login_string_fazer_login.setStyleSheet("QLabel{\n"
"color: rgb(115, 115, 115);\n"
"text-align: center;\n"
"}")
        self.label_login_string_fazer_login.setObjectName("label_login_string_fazer_login")
        self.verticalLayout_3.addWidget(self.label_login_string_fazer_login)
        self.lineEdit_login_cpf = QtWidgets.QLineEdit(self.frame_login_cpf_cliente)
        self.lineEdit_login_cpf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_login_cpf.setFont(font)
        self.lineEdit_login_cpf.setStyleSheet("\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:rgb(115,115,115);\n"
"    border-bottom: 2px solid rgb(115,115,115);\n"
"\n"
"}")
        self.lineEdit_login_cpf.setInputMask("")
        self.lineEdit_login_cpf.setText("")
        self.lineEdit_login_cpf.setObjectName("lineEdit_login_cpf")
        self.verticalLayout_3.addWidget(self.lineEdit_login_cpf)
        self.verticalLayout_2.addWidget(self.frame_login_cpf_cliente)
        self.frame_login_loggar_entrar_cadastro = QtWidgets.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.frame_login_loggar_entrar_cadastro.setFont(font)
        self.frame_login_loggar_entrar_cadastro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_loggar_entrar_cadastro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_loggar_entrar_cadastro.setObjectName("frame_login_loggar_entrar_cadastro")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_login_loggar_entrar_cadastro)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_login_login = QtWidgets.QPushButton(self.frame_login_loggar_entrar_cadastro)
        self.pushButton_login_login.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_login_login.setStyleSheet("QPushButton{\n"
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
        self.pushButton_login_login.setObjectName("pushButton_login_login")
        self.verticalLayout_4.addWidget(self.pushButton_login_login)
        self.pushButton_login_entrar_cadastrar = QtWidgets.QPushButton(self.frame_login_loggar_entrar_cadastro)
        self.pushButton_login_entrar_cadastrar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_login_entrar_cadastrar.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"    \n"
"    color: rgb(115, 115, 115);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_login_entrar_cadastrar.setObjectName("pushButton_login_entrar_cadastrar")
        self.verticalLayout_4.addWidget(self.pushButton_login_entrar_cadastrar)
        self.verticalLayout_2.addWidget(self.frame_login_loggar_entrar_cadastro)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_login_string_fazer_login.setText(_translate("MainWindow", "             Fazer Login no JUbank"))
        self.lineEdit_login_cpf.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.pushButton_login_login.setText(_translate("MainWindow", "Login"))
        self.pushButton_login_entrar_cadastrar.setText(_translate("MainWindow", "Cadastrar-se"))
#import file_r_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
