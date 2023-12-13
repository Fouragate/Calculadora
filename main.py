import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from tela import Ui_MainWindow
from operator import neg

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Numeros
        self.ui.zero_Btt.clicked.connect(lambda: self.pressionado('0'))
        self.ui.OneBtt.clicked.connect(lambda: self.pressionado('1'))
        self.ui.TwoBtt.clicked.connect(lambda: self.pressionado('2'))
        self.ui.threeBtt.clicked.connect(lambda: self.pressionado('3'))
        self.ui.FourBtt.clicked.connect(lambda: self.pressionado('4'))
        self.ui.FiveBtt.clicked.connect(lambda: self.pressionado('5'))
        self.ui.SixBtt.clicked.connect(lambda: self.pressionado('6'))
        self.ui.SevenBtt.clicked.connect(lambda: self.pressionado('7'))
        self.ui.EightBtt.clicked.connect(lambda: self.pressionado('8'))
        self.ui.NineBtt.clicked.connect(lambda: self.pressionado('9'))

        # Botoes
        self.ui.ponto_Btt.clicked.connect(lambda: self.pressionado('.'))
        self.ui.limpar_Btt.clicked.connect(self.clearOutput)
        self.ui.backspace_Btt.clicked.connect(lambda: self.backspace())
        self.ui.igual_Btt.clicked.connect(lambda: self.resultado())

        # Operadores
        self.ui.mais_Btt.clicked.connect(lambda: self.pressionado('+'))
        self.ui.menos_Btt.clicked.connect(lambda: self.pressionado('-'))
        self.ui.multi_Btt.clicked.connect(lambda: self.pressionado('*'))
        self.ui.divisao_Btt.clicked.connect(lambda: self.pressionado('/'))
        self.ui.porcentagem_Btt.clicked.connect(lambda: self.pressionado('%'))

    def backspace(self):
        saida = self.ui.outputLabel.text()
        self.ui.outputLabel.setText(saida[:-1])
        if not len(saida[:-1]):
            self.ui.outputLabel.setText('0')

    def clearOutput(self):
        self.ui.outputLabel.setText('0')

    def pressionado(self, tecla):
        saida = self.ui.outputLabel.text()
        if tecla in ['+', '-', '*', '/', '%'] and saida[-1] in ['+', '-', '*', '/' '%']:
            saida = saida[:-1]
        if saida == '0':
            saida = ''
        if tecla == '.' in saida:
            return
        saida += tecla
        self.ui.outputLabel.setText(saida)


    def resultado(self):
        saida = self.ui.outputLabel.text()
        try:
            answer = eval(saida) if not '%' in saida else float(saida[:-1]) / 100
            self.ui.outputLabel.setText(f'{answer:.2f}')
        except:
            self.ui.outputLabel.setText('ERRO')
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())