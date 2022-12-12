from manejo_de_datos.tdas.grafo import Grafo
import manejo_de_datos.procesar_archivos as pa
from collections import deque
from heapq import *


class VamosMoshi:

    def __init__(self, archivo_mapa, nombre_a_ciudad):
        """
        Crea un grafo a partir del archivo .pj, y permite aplicar diferentes metodos
        sobre este.
        Una vez instanciada la clase el dict *nombre_a_ciudad* queda lleno
        """
        self.__nombre_a_ciudad = nombre_a_ciudad
        self.__grafo = pa.crear_grafo_desde_pajek(
            archivo_mapa, self.__nombre_a_ciudad)

    def camino_minimo(self, desde, hasta):
        """
        Optimiza el camino de *desde* a *hasta*. Devuelve (tiempo_viaje, diccionario_padres)
        o (None, None) si no hay camino
        """
        dist, padres = {}, {}
        for v in self.__grafo:
            dist[v] = float('inf')
        dist[desde], padres[desde] = 0, None
        hp = []
        heappush(hp, (0, desde.obtener_nombre()))

        while len(hp) != 0:
            _, v = heappop(hp)
            v = self.__nombre_a_ciudad[v]

            if v == hasta:
                # Camino Encontrado
                return dist[hasta], padres

            for w in self.__grafo.adyacentes(v):
                dist_por_camino = dist[v] + \
                    self.__grafo.obtener_peso_arista(v, w)
                if dist_por_camino < dist[w]:
                    dist[w] = dist_por_camino
                    padres[w] = v
                    heappush(
                        hp, (dist[w], w.obtener_nombre()))
        # No se encontro camino
        return None, None

    def itinerario_recomendaciones(self, recomendaciones_csv):
        """ Devuelve un itinerario basado en recomendaciones o None si es imposible crearlo """
        grafo_recomendacion = pa.crear_grafo_recomendaciones_csv(
            recomendaciones_csv, self.__nombre_a_ciudad)

        entr = grados_entrada_grafo_recomendacion(grafo_recomendacion)
        lista_itinerario = []
        q = deque()

        for ciudad in grafo_recomendacion:
            if entr[ciudad] == 0:
                q.append(ciudad)

        while len(q) != 0:
            v = q.popleft()
            lista_itinerario.append(v)
            for w in grafo_recomendacion.adyacentes(v):
                entr[w] -= 1
                if entr[w] == 0:
                    q.append(w)

        if len(lista_itinerario) != len(grafo_recomendacion):
            # No se puede crear itinerario con las restricciones dadas
            return None

        return lista_itinerario

    def arbol_tendido_minimo(self):
        """ Devuelve un arbol(Grafo) para recorrer las menos rutas posibles en menos tiempo posible """

        visitado, hp, v = set(), [], self.__grafo.obtener_un_nodo()
        visitado.add(v)

        for w in self.__grafo.adyacentes(v):
            heappush(hp, (self.__grafo.obtener_peso_arista(v, w),
                          v.obtener_nombre(), w.obtener_nombre()))

        arbol = Grafo(lista_nodos=self.__grafo.obtener_nodos())

        while len(hp) != 0:
            peso, v, w = heappop(hp)
            v, w = self.__nombre_a_ciudad[v], self.__nombre_a_ciudad[w]

            if w in visitado:
                continue

            arbol.agregar_arista(v, w, peso)
            visitado.add(w)
            for u in self.__grafo.adyacentes(w):
                if u not in visitado:
                    heappush(hp, (self.__grafo.obtener_peso_arista(
                        w, u), w.obtener_nombre(), u.obtener_nombre()))

        return arbol

    def recorrido_completo(self, origen):
        """
        Calcula un recorrido desde un origen tal que se vean todas las rutas.
        Devuelve (lista_camino, tiempo_viaje)
        """
        grados_impares, origen_es_grado_impar = cantidad_grados_impares(
            self.__grafo, origen)
        if grados_impares == 0:
            return self.__recorrido_ciclo_euleriano(origen)
        elif grados_impares == 2 and origen_es_grado_impar:
            return self.__recorrido_camino_euleriano(origen)

    def __recorrido_camino_euleriano(self, origen):
        # Algoritmo Fleury
        caminos_visitados = set()
        camino_euleriano = []
        cantidad_aristas = obtener_cantidad_aristas(self.__grafo)

        self.__dfs_camino_euleriano(origen, caminos_visitados,
                                    cantidad_aristas, camino_euleriano)
        return camino_euleriano, 0

    def __dfs_camino_euleriano(self, v, caminos_visitados, cantidad_aristas, camino_euleriano):

        camino_euleriano.append(v)
        if len(caminos_visitados) / 2 == cantidad_aristas:
            return

        for w in self.__grafo.adyacentes(v):
            if (v, w) in caminos_visitados or (arista_puente(v, w) and len(self.__grafo.adyacentes(v)) > 1):
                continue

            caminos_visitados.add((v, w))
            caminos_visitados.add((w, v))

            self.__dfs_camino_euleriano(w, caminos_visitados,
                                        cantidad_aristas, camino_euleriano)

    def __recorrido_ciclo_euleriano(self, origen):
        # Algoritmo Hierholzer
        aristas_visitadas = set()
        recorrido = [origen]
        cantidad_aristas = obtener_cantidad_aristas(self.__grafo)

        self.__dfs_ciclo_euleriano(
            origen, origen, recorrido, aristas_visitadas, True)

        while len(recorrido) <= cantidad_aristas:
            nuevo_origen = recorrido[-2]
            camino_restante = [nuevo_origen]

            self.__dfs_ciclo_euleriano(
                nuevo_origen, nuevo_origen, camino_restante, aristas_visitadas, True)

            ultimo_elem = recorrido[-1]
            recorrido = recorrido[:-2] + camino_restante
            recorrido.append(ultimo_elem)

        tiempo_total = 0
        for i in range(len(recorrido)-1):
            tiempo_total += self.__grafo.obtener_peso_arista(
                recorrido[i], recorrido[i+1])

        return recorrido, tiempo_total

    def __dfs_ciclo_euleriano(self, v, origen, recorrido, aristas_visitadas, continuar):

        for w in self.__grafo.adyacentes(v):
            if v == origen and not continuar:
                return False

            if (v, w) not in aristas_visitadas:
                aristas_visitadas.add((v, w))
                aristas_visitadas.add((w, v))
                recorrido.append(w)

                if not self.__dfs_ciclo_euleriano(w, origen, recorrido, aristas_visitadas, False):
                    break


# Funciones auxiliares usadas en VamosMoshi


def obtener_cantidad_aristas(grafo):
    cantidad_aristas = 0
    for v in grafo:
        cantidad_aristas += len(grafo.adyacentes(v))
    return cantidad_aristas / 2


def cantidad_grados_impares(grafo, vertice_a_checkear):
    # Devuelve cantidad grados impares y bool si el vertice dado tiene grado impar
    cant = 0
    vertice_es_grado_impar = False

    for v in grafo:
        if len(grafo.adyacentes(v)) % 2 != 0:
            cant += 1
            if v == vertice_a_checkear:
                vertice_es_grado_impar = True

    return cant, vertice_es_grado_impar


def grados_entrada_grafo_recomendacion(grafo_recomendacion):
    entr = {}
    for v in grafo_recomendacion:
        entr[v] = 0
    for v in grafo_recomendacion:
        for w in grafo_recomendacion.adyacentes(v):
            entr[w] += 1
    return entr


def arista_puente(grafo, v, w):
    pass
