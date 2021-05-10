import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_deposito import Tela_deposito
from tela_login import Tela_login
from tela_menu import Tela_menu
from tela_saque import Tela_saque
from tela_transfere2 import Tela_transfere
from tela_cadastro import Tela_cadastro
from tela_historico import Tela_historico

from cadastro import Cadastro
from Banco import Banco,Cliente

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self,Main):
        Main.setObjectName('Main')
        Main.resize(640,480)#tamnaho da tela

        self.QtStack=QtWidgets.QStackedLayout()#cria pilha

        #qts de telas
        self.stack0=QtWidgets.QMainWindow()
        self.stack1=QtWidgets.QMainWindow()
        self.stack2=QtWidgets.QMainWindow()
        self.stack3=QtWidgets.QMainWindow()
        self.stack4=QtWidgets.QMainWindow()
        self.stack5=QtWidgets.QMainWindow()
        self.stack6=QtWidgets.QMainWindow()

        #cria objetos para as telas
        self.tela_login=Tela_login()
        self.tela_login.setupUi(self.stack0)

        self.tela_menu=Tela_menu()
        self.tela_menu.setupUi(self.stack1)

        self.tela_cadastro=Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack2)
        
        self.tela_deposito=Tela_deposito()
        self.tela_deposito.setupUi(self.stack3)

        self.tela_transfere=Tela_transfere()
        self.tela_transfere.setupUi(self.stack4)

        self.tela_saque=Tela_saque()
        self.tela_saque.setupUi(self.stack5)

        self.tela_historico=Tela_historico()
        self.tela_historico.setupUi(self.stack6)        

        #add ao QtStack
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        '''
        '''

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        #cria um objeto
        self.cad=Cadastro()
        self.contaLogada=None
        self.contaTransfere=None
        self.n_conta=0
        #funçoes dos botoes da tela,
        self.tela_login.pushButton_login_login.clicked.connect(self.botaoLogin)
        self.tela_login.pushButton_login_entrar_cadastrar.clicked.connect(self.abrirCadastro)

        self.tela_menu.pushButton_menu_entra_deposito.clicked.connect(self.abrirDeposito)
        self.tela_menu.pushButton_menu_entra_saque.clicked.connect(self.abrirSaque)
        self.tela_menu.pushButton_menu_entra_transferencia.clicked.connect(self.abrirTransfere)
        self.tela_menu.pushButton_voltar_login.clicked.connect(self.botaoLogin)
        self.tela_menu.pushButton_entrar_historico.clicked.connect(self.botaoHistorico)

        self.tela_cadastro.pushButton_cadastro_cadastrar.clicked.connect(self.botaoCadastro)
        self.tela_cadastro.pushButton_cadastro_entrar_login.clicked.connect(self.abrirLogin)

        self.tela_saque.pushButton_saque_sacar.clicked.connect(self.botaoSaca)
        self.tela_saque.pushButton_saque_voltar_menu.clicked.connect(self.abrirMenu)

        self.tela_deposito.pushButton_deposito_depositar.clicked.connect(self.botaoDeposito)
        self.tela_deposito.pushButton_deposito_voltar_menu.clicked.connect(self.botaoMenu)

        self.tela_transfere.pushButton_trnsf_transferir.clicked.connect(self.botaoTranfere)
        self.tela_transfere.pushButton_transf_voltar_menu.clicked.connect(self.botaoMenu)

        self.tela_saque.pushButton_saque_sacar.clicked.connect(self.botaoSaca)
        self.tela_saque.pushButton_saque_voltar_menu.clicked.connect(self.botaoMenu)

        self.tela_historico.pushButton_historic_voltar.clicked.connect(self.botaoMenu)

    def botaoCadastro(self):
        nome=self.tela_cadastro.lineEdit_cadastro_nome.text()
        sobrenome=self.tela_cadastro.lineEdit_cadastro_sobrenome.text()
        cpf=self.tela_cadastro.lineEdit_cadastro_CPF.text()
        if not(nome=='' or sobrenome=='' or cpf==''):
            if self.cad.busca(cpf)==None:
                p = Cliente(nome,sobrenome, cpf)
                conta=Banco(self.n_conta+1, p, 0.0, 1000)
                self.cad.cadastra(conta)
                QMessageBox.information(None, 'Cadastro', 'Cadastro realizado!')
                self.tela_cadastro.lineEdit_cadastro_nome.setText('')
                self.tela_cadastro.lineEdit_cadastro_sobrenome.setText('')
                self.tela_cadastro.lineEdit_cadastro_CPF.setText('')
            else:
                QMessageBox.information(None, 'Cadastro', 'CPF informado já cadastrado.')
                self.tela_cadastro.lineEdit_cadastro_nome.setText('')
                self.tela_cadastro.lineEdit_cadastro_sobrenome.setText('')
                self.tela_cadastro.lineEdit_cadastro_CPF.setText('')
        else:
            QMessageBox.information(None, 'Cadastro', 'Todos os campos devem ser preenchidos!')  

        self.QtStack.setCurrentIndex(0)
    def botaoLogin(self):
        cpf=self.tela_login.lineEdit_login_cpf.text()
        pes=self.cad.busca(cpf)
        if cpf != '':
            if pes!=None:
                self.contaLogada=pes
                self.tela_login.lineEdit_login_cpf.setText('')
                self.botaoMenu()
            else:
                self.contaLogada=None
                QMessageBox.information(None, 'Login', 'CPF não cadastrado!') 
                self.tela_login.lineEdit_login_cpf.setText('')
                self.abrirLogin() 
        else:
            self.abrirLogin() 

        
    def botaoTranfere(self):
        valor=self.tela_transfere.lineEdit_transf_valor.text()
        cpf=self.tela_transfere.lineEdit_trnsf_cpf.text()
        contaTransfere=self.cad.busca(cpf)
       
        if valor!='' and cpf !='':
            if contaTransfere != None and contaTransfere != self.contaLogada:
                try:
                    if(self.contaLogada.transferir(contaTransfere,float(valor))):
                        QMessageBox.information(None, 'Transferencia', 'Transferencia realizada!')
                        #self.cad[1].depositar(valor)
                        #self.contaTransfere.depositar(valor)
                        #self.contaTransfere=None
                    else:
                        QMessageBox.information(None, 'Transferencia', 'Transferencia não realizada!')

                except:
                    QMessageBox.information(None, 'Transferencia', 'Apenas digitos!')
            else:
                if contaTransfere == self.contaLogada:
                    QMessageBox.information(None, 'Transferencia', 'Conta destino não pode ser a mesma de origem!')
                else:
                    QMessageBox.information(None, 'Transferencia', 'Conta destino não enocontrada!')
            self.tela_transfere.lineEdit_transf_valor.setText('')
            self.tela_transfere.lineEdit_trnsf_cpf.setText('')
        #self.botaoMenu()

    def botaoSaca(self):
        valor=self.tela_saque.lineEdit_saque_valor.text()
        if(valor !=''):
            try:
                if(self.contaLogada.sacar(float(valor))):
                    QMessageBox.information(None, 'Saque', 'saque realizado!')
                else:
                    QMessageBox.information(None, 'Saque', 'Saque não realizado!')
            except:
                QMessageBox.information(None, 'Saque', 'Apenas digitos!')
            self.tela_saque.lineEdit_saque_valor.setText('')
        #self.botaoMenu()

        
    def botaoDeposito(self):
        valor=self.tela_deposito.lineEdit_deposito_valor.text()
        if valor !='':
            try:
                if(self.contaLogada.depositar(float(valor))):
                    QMessageBox.information(None, 'Deposito', 'Deposito realizado!')
                else:
                    QMessageBox.information(None, 'Deposito', 'Deposito não realizado,\n limite ultrapassado!')

            except:
                QMessageBox.information(None, 'Deposito', 'Apenas digitos!')
            self.tela_deposito.lineEdit_deposito_valor.setText('')
        #self.botaoMenu()

    def botaoMenu(self):
        if self.contaLogada!=None:
            self.abrirMenu()
            self.tela_menu.lineEdit_menu_nome_sobrenome_cliente.setText(self.contaLogada.titular.nome)
            self.tela_menu.lineEdit_menu_saldo_conta.setText(str(self.contaLogada.saldo))
        else:
            QMessageBox.information(None, 'Menu', 'CPF não cadastrado!') 
            self.abrirLogin() 
        
    def botaoHistorico(self):
        self.abrirHistorico()
        extrato = ''
        for i in self.contaLogada.historico.transacoes:
            extrato = extrato +'\n'+ i
        self.tela_historico.textEdit_historico.setText(extrato)

    def abrirLogin(self):
        self.QtStack.setCurrentIndex(0)
    def abrirMenu(self):
        self.QtStack.setCurrentIndex(1)
    def abrirCadastro(self):
        self.QtStack.setCurrentIndex(2)
    def abrirDeposito(self):
        self.QtStack.setCurrentIndex(3)
    def abrirTransfere(self):
        self.QtStack.setCurrentIndex(4)
    def abrirSaque(self):
        self.QtStack.setCurrentIndex(5)
    def abrirHistorico(self):
        self.QtStack.setCurrentIndex(6)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main=Main()
    sys.exit(app.exec_())
