import sys
from constantes import *
from procesar_pajek import crear_grafo_desde_pajek


class VamosMoshi:

    def __init__(self, args):
        self.grafo = crear_grafo_desde_pajek(args)

    def ejecutar(self):
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

    def camino_minimo(self):
        pass

    def itinerario_recomendaciones(self):
        pass

    def recorrido_circular(self):
        pass

    def arbol_tendido_minimo(self):
        pass


if __name__ == '__main__':
    archivo = sys.argv[1]
    programa = VamosMoshi(archivo)
    programa.ejecutar()
