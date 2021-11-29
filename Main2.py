import random
import time
from FitnessFunction import FitnessFunction
from AlgoritmoEvolutivo import AlgoritmoEvolutivo
from PyQt5 import uic,QtWidgets
from Ventana_Ganar import Ganador
import sys
from Principal import *
from PyQt5.QtWidgets import *
from Ganaste import *
from Ganaste_Bot import *
import os
from Palabras import Pal
import threading
#Algoritmo Evolutivo
from Individuo import Individuo
from Poblacion import Poblacion
from Seleccion import Seleccion
from FitnessFunction import FitnessFunction
import numpy as n

class Ventana(QMainWindow):
    def __init__(self,parent =None):      
        #Iniciamos la interfaz  
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #Boton que iniciara la palabra a encontrar
        self.ui.prueba.clicked.connect(self.ocultar)
        #Compromabamos la palabra o letra que introducimos
        self.ui.Comprobar.clicked.connect(self.Comprobar)
        #Palabra aleatoria de una Lista
        self.palabra_pro = ""
        #Guardamos en esta variable todas las letras que hemos introducido
        self.tupalabra = ""
        #Numero de vidas
        self.vidas = 8
        self.led = ""
        #Ocultamos los QLabel deon destan las imagenes
        self.ui.Mean6.setHidden(True)
        self.ui.Mean4.setHidden(True)
        self.ui.Mean3.setHidden(True)
        self.ui.Mean2.setHidden(True)
        self.ui.Mean7.setHidden(True)
        self.ui.Mean5.setHidden(True)
        self.ui.Mean1.setHidden(True)
        self.ui.Mean6_2.setHidden(True)
        
        #Hilo
        self.thread = threading.Thread(target=self.pruebas)
    
    def search(self):
        #Obtenemos el texto del QtextEdit
        textboxValue = self.ui.Palabra.toPlainText()
        print(textboxValue)

    def func(): 
        while True: 
            time.sleep(0.5) 
            print('Thread alive, but it will die on program termination') 
  
    
    def ocultar(self):
        self.Reset()
        #Obtenemos el texto introducido en el QtextEdit
        self.search()
        #Inicialisamos la palabra que averiguaremos
        self.palabras()
        #Creamos un Hilo para poder ejecutar al mismo tiempo

        self.thread = threading.Thread(target=self.pruebas)
        self.thread.start()
        #self.pruebas()

    def elegir(self):
        tamaño = self.palabras
        print(tamaño)
    #Ventana que aparecera si ganamos o perdemos
    def Abrir_Ganar(self,palabra):
        self.hide()
        ventana = Ganador(self)
        ventana.ven(palabra)
        ventana.show()
    def Abrir_Ganar_2(self,palabra):
        self.hide()
        ventana = Ganador_Bot(self)
        ventana.ven(palabra)
        ventana.show()

    #Boton donde comprobaremos las letras introducidas
    def Comprobar(self):
        #Obtenemos el tamaño de la palabra a averiguar
        tamaño = len(self.palabra_pro)
        palabra = self.palabra_pro
        print(palabra)
        #Variable donde se guardara las letras que ayamos introducido correctamente
        self.led = ""
        #Obtenemos  el texto del Qtext      
        Letra = self.ui.Palabra.toPlainText()
        #Añadimos lo intrucido a esta variable
        self.tupalabra += Letra
        for i in palabra:
            if i in self.tupalabra:
                self.led += i#Sumamos la letra correnta
                self.ui.Mostrar.setText(self.led)#La mostramos en la ventana principal
                if self.led == self.palabra_pro:
                    self.Abrir_Ganar("Ganador")
                #self.thread.join()
            else:#Si la letra no correnta omitira este paso          
                pass
        #Restamos una vida si el usuario se equivoca
        if Letra not in palabra:
            self.vidas -= 1
        #Fromamos al muñequito del ahorcado
        if self.vidas == 7:
            self.ui.Mean1.setHidden(False)
        elif self.vidas == 6:
            self.ui.Mean2.setHidden(False)
        elif self.vidas == 5:
            self.ui.Mean3.setHidden(False)
        elif self.vidas == 4:
            self.ui.Mean4.setHidden(False)
        elif self.vidas == 3:
            self.ui.Mean5.setHidden(False)
        elif self.vidas == 2:
            self.ui.Mean6.setHidden(False)
        elif self.vidas == 1:
            self.ui.Mean6_2.setHidden(False)
            self.Abrir_Ganar("Perdiste")#Abrimos una ventana donde muestra que perdio
        elif self.vidas == 0:
            print("0vidas")
    #Resetamos todos los valores

    #Reseteamps todo
    def Reset(self):
        #Ocultamos el muñeco del ahorcado
        self.ui.Mean6.setHidden(True)
        self.ui.Mean4.setHidden(True)
        self.ui.Mean3.setHidden(True)
        self.ui.Mean2.setHidden(True)
        self.ui.Mean7.setHidden(True)
        self.ui.Mean5.setHidden(True)
        self.ui.Mean1.setHidden(True)
        self.ui.Mean6_2.setHidden(True)
        self.palabra_pro = ""
        self.tupalabra = ""
        self.led = ""
        self.vidas = 8
        self.ui.Palabra.setText("")
        self.ui.Mostrar.setText("")

    #Se seleccionara una palabra aleatoriamente a descubrir
    def palabras(self):
        #lista_palabras = ['Elefante','Osos','Leon','Perro','Gato','Aves','raton','Mariposa','hipopotamo','caballo']
        #palabra = random.choice(lista_palabras)#Seleccionamos un elemento al azar de la lista
        #Lista de palabras a averiguar
        lista_palabra = ['perro','ave','hipopotamo','avestruz','godorniz','gallina','perico','pollino','dragon','cocodrilo','mariposa','rinoceronte','aguila','camello','flamenco','elefante','leopardo','jirafa','jabali','lagartija','murcielago','paloma','panda','mapache','pelicano','raton','serpiente','tiburon','tucan','bisonte','bufalo','buitre','caballo','puerco','canario']
        palabra = random.choice(lista_palabra)#Seleccionamos un elemento al azar de la lista
        ayuda = ""
        #Ayuda
        if palabra == 'perro':
            ayuda = 'pe__o'
        elif palabra == 'ave':
            ayuda = "a_e"
        elif palabra == 'hipopotamo':
            ayuda = "hi__potamo"
        elif palabra == 'avestruz':
            ayuda = "avez__uz"
        elif palabra == 'godorniz':
            ayuda = "__dorniz"
        elif palabra == 'gallina':
            ayuda = "__llina"
        elif palabra == 'perico':
            ayuda = "pe__co"
        elif palabra == 'pollino':
            ayuda = "po__ino"
        elif palabra == 'dragon':
            ayuda = "drag__"
        elif palabra == 'cocodrilo':
            ayuda = "__codrilo"
        elif palabra == 'mariposa':
            ayuda = "__riposa"
        elif palabra == 'rinoceronte':
            ayuda = "rino__ronte"
        elif palabra == 'aguila':
            ayuda = "ag__ila"
        elif palabra == 'camello':
            ayuda = "ca__llo"
        elif palabra == 'flamenco':
            ayuda = "flamen__"
        elif palabra == 'elefante':
            ayuda = "e__fante"
        elif palabra == 'leopardo':
            ayuda = "le__ardo"
        elif palabra == 'jirafa':
            ayuda = "__rafa"
        elif palabra == 'jabali':
            ayuda = "__bali"
        elif palabra == 'lagartija':
            ayuda = "la__rtija"
        elif palabra == 'murcielago':
            ayuda = "__rcielago"
        elif palabra == 'paloma':
            ayuda = "pa__ma"
        elif palabra == 'panda':
            ayuda = "pan__"
        elif palabra == 'mapache':
            ayuda = "__pache"
        elif palabra == 'pelicano':
            ayuda = "__licano"
        elif palabra == 'raton':
            ayuda = "ra__n"
        elif palabra == 'tucan':
            ayuda = "tu__n"
        elif palabra == 'bisonte':
            ayuda = "bi__nte"
        elif palabra == 'bufalo':
            ayuda = "bufa__"
        elif palabra == 'buitre':
            ayuda = "buit__"
        elif palabra == 'caballo':
            ayuda = "ca__llo"
        elif palabra == 'puerco':
            ayuda = "pu__co"
        elif palabra == 'canario':
            ayuda = "can__io"
        elif palabra == "tiburon":
            ayuda = "_ibu__n"
        elif palabra == "serpiente":
            ayuda = "ser_ien_e"
        longitud = len(palabra)
        self.palabra_pro = palabra
        self.ui.label_2.setText(ayuda+"")
        print(longitud)
        print(palabra) 


    #Aplicamos un algoritmo Evolutivo
    def pruebas(self):
        start = time.time()
        ff = FitnessFunction(self.palabra_pro)
        ae = AlgoritmoEvolutivo(ff, 100, 600)# Al construir un objeto AE 
        sa = ae.evolve(500)
        self.ui.Genetico.setText(sa + "")
        final = time.time()
        if sa == self.palabra_pro:
            self.Abrir_Ganar_2("Gano la Maquina \n Tiempo: {0:.2f} s ".format(final-start))

#Ventana que se ejecutara al ganar el usuario
class Ganador(QMainWindow):
    def __init__(self,parent =None):        
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form_2()
        self.ui.setupUi(self)
        self.ui.Salir.clicked.connect(self.close)
        self.ui.Nuevo_Juego.clicked.connect(self.Principal)    
    #Reinicio de valores
    def reinicio(self):
        self.hide()
        ventana = Ventana(self)
        ventana.Reset()
    #Abrimos la ventana principal
    def Principal(self):
        self.reinicio()
        self.parent().show()
        self.close()
    #Escribimos en el label si gano o perdio el usuario
    def ven(self,palabra):
        self.ui.label.setText(palabra + "")
    
    def Mostrar(self):
        myapp = QApplication(sys.argv)
        myapp = Ganador()
        myapp.show()

#Ventana Bot
class Ganador_Bot(QMainWindow):
    def __init__(self,parent =None):        
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form_3()
        self.ui.setupUi(self)

    def ven(self,palabra):
        self.ui.label.setText(palabra + "")

#Esta parte muestra la ventana
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Ventana()
    myapp.show()
    sys.exit(app.exec_())