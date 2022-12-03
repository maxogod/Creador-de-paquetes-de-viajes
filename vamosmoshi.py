import sys
from constantes import *
ARCHIVO = sys.argv[1]


def comandos():
    ingreso = input().lower()
    while ingreso is not CORTAR:
        comando = ingreso.split()
        if comando[0] == COMANDO1:
            pass
        elif comando[0] == COMANDO2:
            pass
        elif comando[0] == COMANDO3:
            pass
        elif comando[0] == COMANDO4:
            pass

        ingreso = input().lower()


def camino_minimo():
    pass


if __name__ == '__main__':
    comandos()
