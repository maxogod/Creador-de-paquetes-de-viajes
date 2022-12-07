import sys
from constantes import *
from procesar_pajek import crear_grafo_desde_pajek
from heapq import *
import mostrar_datos_stdin as md
import crear_archivos as ca


class VamosMoshi:

    def __init__(self, archivo_mapa, nombre_a_ciudad):
        """
        Crea un grafo a partir del archivo .pj, y permite aplicar diferentes metodos
        sobre este. 
        Una vez instanciada esta clase el diccionario *nombre_a_ciudad* se encuentra lleno
        con Key-Values tal como lo indica su nombre.
        """
        self.nombre_a_ciudad = nombre_a_ciudad
        self.grafo = crear_grafo_desde_pajek(
            archivo_mapa, self.nombre_a_ciudad)

    def camino_minimo(self, desde, hasta):
        dist, padres = {}, {}
        for v in self.grafo:
            dist[v] = float('inf')
        dist[desde], padres[desde] = 0, None
        hp = []
        heappush(hp, (0, desde.obtener_nombre()))

        while len(hp) != 0:
            _, v = heappop(hp)
            v = self.nombre_a_ciudad[v]
            if v == hasta:
                return dist[hasta], padres
            for w in self.grafo.adyacentes(v):
                dist_por_camino = dist[v] + \
                    self.grafo.obtener_peso_arista(v, w)
                if dist_por_camino < dist[w]:
                    dist[w] = dist_por_camino
                    padres[w] = v
                    heappush(
                        hp, (dist[w], w.obtener_nombre()))
        return None, None

    def itinerario_recomendaciones(self):
        pass

    def recorrido_circular(self):
        pass

    def arbol_tendido_minimo(self):
        pass


def ejecutar(archivo_mapa):
    nombre_a_ciudad = {}
    programa = VamosMoshi(archivo_mapa, nombre_a_ciudad)

    ingreso = input().lower()
    while ingreso is not CORTAR_STDIN:

        comando, parametros = ingreso.split()[0], ingreso.split()[1:]

        if comando == IR:  # ir desde, hasta, archivo
            try:
                desde = nombre_a_ciudad[parametros[0].rstrip(',').capitalize()]
                hasta = nombre_a_ciudad[parametros[1].rstrip(',').capitalize()]

                tiempo, padres = programa.camino_minimo(desde, hasta)

                if tiempo is None:
                    print(RECORRIDO_NO_ENCONTRADO)
                else:
                    print(md.mostrar_camino(padres, hasta, tiempo=tiempo))
                    ca.crear_archivo_kml(parametros[2], desde, hasta, padres)
            except KeyError:  # Desde o Hasta no es un vertice
                print(RECORRIDO_NO_ENCONTRADO)

        elif comando == ITINERARIO:  # itinerario recomendaciones.csv
            pass

        elif comando == VIAJE:  # viaje origen, archivo
            pass

        elif comando == REDUCIR_CAMINOS:  # reducir_caminos destino.pj
            pass

        ingreso = input().lower()


if __name__ == '__main__':
    archivo = sys.argv[1]
    ejecutar(archivo)
