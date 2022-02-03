"""
PyQT é um toolkit desenvolvido em c++ utilizado em vários programas para
criação de aplicações GUI(Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação da rede,
etc...
"""


import sys
from PyQt5.QtWidgets import QGridLayout, QMainWindow, QApplication, QPushButton, QWidget


class App(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.centralW = QWidget()
        self.grade = QGridLayout(self.centralW)

        self.botao = QPushButton("Texto do botao")
        self.grade.addWidget(self.botao, 0,0 ,1 ,1)

        self.setCentralWidget(self.centralW)

        # self.
        # Passando um afunção para executara pos click no botão

        self.botao.clicked.connect(self.acao)
    def acao(self):
        print("O botão foi clicado!")
if __name__ =='__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()