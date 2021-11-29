#Juego del Ahorcado


import time

nombre  = input("Escribe tu nombre ")
print("Hola, " + nombre)
print("")

time.sleep(1.2)
print("Comienza a adivinar")

palabra = "Lucio"

tupalabra = ""
vidas = 5

while vidas>0:
    fallas = 0
    for letra in palabra:#Buecamos si la letra esta en la palabra
        if letra in tupalabra:
            print(letra,end = "")
        else:
            print("*",end="")
            fallas += 1
    
    if fallas ==0:
        print("Eres un Crack")
        break
    print("")
    tuletra = input("Introduce una letra ")
    tupalabra += tuletra
    print(tupalabra)
    if tuletra not in palabra:
        vidas -= 1
        print("Mal vidas restantes {}".format(vidas) )
    if vidas ==0:
        print("Perdiste")
        break
else:
    print("Adios")

