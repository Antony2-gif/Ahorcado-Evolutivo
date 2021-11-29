import random

class Pal:

    def Palabra(self):
        lista = ['perro','ave','hipopotamo','avestruz','godorniz','gallina','perico','pollino','dragon','cocodrilo','mariposa','rinoceronte','aguila','camello','flamenco','elefante','leopardo','jirafa','jabali','lagartija','murcielago','paloma','panda','mapache','pelicano','raton','serpiente','tiburon','tucan','bisonte','bufalo','buitre','caballo','puerco','canario']
        palabra = random.choice(lista)#Seleccionamos un elemento al azar de la lista
        ayuda = ""

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
    

        print(palabra)
        return ayuda


