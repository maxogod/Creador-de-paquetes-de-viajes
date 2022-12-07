import sys
from collections import deque

import procesar_archivos
from constantes import *
from procesar_archivos import crear_grafo_desde_pajek
from heapq import *
import mostrar_datos_stdin as md
import crear_archivos as ca
from grafo.grafo import Grafo


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

    def itinerario_recomendaciones(self,grafo_recomendaciones):

        indeg = obtener_grados_de_entrada(grafo_recomendaciones)
        ciudades_bloqueados = set()
        lista_itinerario = []
        tiempo_total = 0
        for ciudad in indeg:
            if indeg[ciudad] > 0:
                ciudades_bloqueados.add(ciudad)

        q = deque()
        for v in grafo_recomendaciones:
            if indeg[v] == 0:
                q.append(v)
        while len(q) != 0:
            v = q.popleft()
            lista_itinerario.append(v)
            for e in grafo_recomendaciones.adyacentes(v):
                indeg[e] -= 1
                if indeg[e] == 0 and grafo_recomendaciones.arista_existe(v, e):
                    q.append(e)
                    ciudades_bloqueados.remove(e)
                    lista_itinerario.append(e)
                    tiempo_total += grafo_recomendaciones.obtener_peso_arista(v, e)
                elif indeg[e] == 0:
                    ciudades_bloqueados.remove(e)
                    lista_nodos_a_unir,tiempo_sub_total = unir_nodos(self.grafo,v,e,ciudades_bloqueados)
                    lista_itinerario.extend(lista_nodos_a_unir)
                    tiempo_sub_total += tiempo_sub_total

        return lista_itinerario



    def recorrido_circular(self):
        pass

    def arbol_tendido_minimo(self):
        visitado, hp, v = set(), [], self.grafo.obtener_un_nodo()
        visitado.add(v)
        for w in self.grafo.adyacentes(v):
            heappush(hp, (self.grafo.obtener_peso_arista(v, w),
                     v.obtener_nombre(), w.obtener_nombre()))
        arbol = Grafo(lista_nodos=self.grafo.obtener_nodos())
        while len(hp) != 0:
            peso, v, w = heappop(hp)
            v, w = self.nombre_a_ciudad[v], self.nombre_a_ciudad[w]
            if w in visitado:
                continue
            arbol.agregar_arista(v, w, peso)
            visitado.add(w)
            for u in self.grafo.adyacentes(w):
                if u not in visitado:
                    heappush(hp, (self.grafo.obtener_peso_arista(
                        w, u), w.obtener_nombre(), u.obtener_nombre()))
        return arbol


def dfs(grafo, v, e, ciudades_bloqueados, visitados, lista_nodos, tiempo_total):
    for w in grafo.adyacentes(v):
        tiempo_total += grafo.obtener_peso_arista(v, w)

        if w == e:
            return True
        if w not in visitados and w not in ciudades_bloqueados:
            lista_nodos.append(w)
            visitados.add(w)
            return dfs(grafo, w, e, ciudades_bloqueados, visitados, lista_nodos, tiempo_total)
        return False



def unir_nodos(grafo,v,e,ciudades_bloqueados):
    lista_nodos = []
    tiempo_total = 0
    visitados = set()
    for w in grafo.adyacentes(v):
      encontado = dfs(grafo, w, e, ciudades_bloqueados, visitados, lista_nodos, tiempo_total)

    if encontado:
        return lista_nodos,tiempo_total
    else:
        #error



def obtener_grados_de_entrada(grafo):
        indeg = {}
        for v in grafo:
            indeg[v] = 0
        for v in grafo:
            for e in grafo.edges(v):
                indeg[e] += 1

        return indeg


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
            except KeyError:  # En caso no exista vertice *desde* o *hasta*
                print(RECORRIDO_NO_ENCONTRADO)

        elif comando == ITINERARIO:  # itinerario recomendaciones.csv
            recomendaciones = parametros[0]
            grafo_recomendacinoes = procesar_archivos.procesar_recomendaciones_csv(recomendaciones)
            print(programa.itinerario_recomendaciones(grafo_recomendacinoes))

        elif comando == VIAJE:  # viaje origen, archivo
            pass

        elif comando == REDUCIR_CAMINOS:  # reducir_caminos destino.pj
            arbol = programa.arbol_tendido_minimo()
            print(md.mostrar_peso_total(arbol))
            ca.crear_archivo_pj(parametros[0], arbol)

        ingreso = input().lower()


if __name__ == '__main__':
    archivo = sys.argv[1]
    ejecutar(archivo)
