import sys
from Ganaste import *
from PyQt5.QtWidgets import *
class Ganador(QWidget):
    def __init__(self,parent =None):        
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form_2()
        self.ui.setupUi(self)

        self.ui.Salir.clicked.connect(self.Sal)
        
    def Sal(self):
        print("Salir")
        
    def Mostrar(self):
        app = QApplication(sys.argv)
        myapp = Ganador()
        myapp.show()
