import sys
from constantes import *
from procesar_pajek import crear_grafo_desde_pajek
from heapq import *


class VamosMoshi:

    def __init__(self, args):
        self.nombre_a_ciudad = {}
        self.grafo = crear_grafo_desde_pajek(args, self.nombre_a_ciudad)

    def ejecutar(self):
        ingreso = input().lower()
        while ingreso is not CORTAR:
            comando = ingreso.split()
            if comando[0] == COMANDO1:
                try:
                    desde = self.nombre_a_ciudad[comando[1].rstrip(",")]
                    hasta = self.nombre_a_ciudad[comando[2].rstrip(",")]
                    tiempo, padres = self.camino_minimo(desde, hasta)
                    if tiempo is None:
                        print(RECORRIDO_NO_ENCONTRADO)
                    else:
                        mostrar_camino(padres, hasta, tiempo=tiempo)
                        # TODO crear KML
                except KeyError:
                    print(RECORRIDO_NO_ENCONTRADO)

            elif comando[0] == COMANDO2:
                pass
            elif comando[0] == COMANDO3:
                pass
            elif comando[0] == COMANDO4:
                pass

            ingreso = input().lower()

    def camino_minimo(self, desde, hasta) -> (int, dict):
        dist = padres = {}
        for v in self.grafo:
            dist[v] = float('inf')
        dist[desde], padres[desde] = 0, None
        hp = []
        heappush(hp, (0, desde))

        while len(hp) != 0:
            _, v = heappop(hp)
            if v == hasta:
                return dist[hasta], padres
            for w in self.grafo.get_edges_of_node(v):
                dist_por_camino = dist[v] + self.grafo.get_weight_of_edge(v, w)
                if dist_por_camino < dist[w]:
                    dist[w] = dist_por_camino
                    padres[w] = v
                    heappush(hp, (dist[w], w))
        return None, None

    def itinerario_recomendaciones(self):
        pass

    def recorrido_circular(self):
        pass

    def arbol_tendido_minimo(self):
        pass


def mostrar_camino(padres, hasta, tiempo=None):
    camino_lista = []
    while hasta is not None:
        camino_lista.append(hasta)
        hasta = padres[hasta]
    camino_lista = camino_lista[::-1]

    camino = ""
    for ciudad in camino_lista:
        ciudad_nombre = ciudad.obtener_nombre()
        camino.join(ciudad_nombre) if ciudad == camino_lista[-1] else camino.join(ciudad_nombre + " -> ")

    return f"{camino}" if tiempo is None else f"{camino}\nTiempo total:{tiempo}"


if __name__ == '__main__':
    archivo = sys.argv[1]
    programa = VamosMoshi(archivo)
    programa.ejecutar()
