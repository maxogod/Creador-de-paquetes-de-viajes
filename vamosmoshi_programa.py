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

        for v in self.__grafo:
            if v not in grafo_recomendacion:
                lista_itinerario.append(v)

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

        if cantidad_grados_impares(self.__grafo) == 0:
            return self.__recorrido_circular(origen)

        return None, None  # No es ciclo euleriano

    def __recorrido_circular(self, origen):
        # Copiamos el grafo en un dict de listas, para poder borrar las aristas facilmente
        adyacentes = {}
        for v in self.__grafo:
            adyacentes[v] = []
            for w in self.__grafo.adyacentes(v):
                adyacentes[v].append(w)

        tiempo = 0
        camino_actual = [origen]
        recorrido = []
        aristas_visitadas = set()

        while camino_actual:
            v = camino_actual[-1]
            if adyacentes[v] and not (v, adyacentes[v][-1]) in aristas_visitadas:
                w = adyacentes[v].pop()

                aristas_visitadas.add((v, w))
                aristas_visitadas.add((w, v))
                tiempo += self.__grafo.obtener_peso_arista(v, w)

                camino_actual.append(w)

            elif adyacentes[v] and (v, adyacentes[v][-1]) in aristas_visitadas:
                adyacentes[v].pop()
            else:
                recorrido.append(camino_actual.pop())
        return recorrido, tiempo


# Funciones auxiliares usadas en VamosMoshi


def obtener_cantidad_aristas(grafo):
    cantidad_aristas = 0
    for v in grafo:
        cantidad_aristas += len(grafo.adyacentes(v))
    return cantidad_aristas / 2


def cantidad_grados_impares(grafo):
    # Devuelve cantidad grados impares y bool si el vertice dado tiene grado impar
    cant = 0

    for v in grafo:
        if len(grafo.adyacentes(v)) % 2 != 0:
            cant += 1

    return cant


def grados_entrada_grafo_recomendacion(grafo_recomendacion):
    entr = {}
    for v in grafo_recomendacion:
        entr[v] = 0
    for v in grafo_recomendacion:
        for w in grafo_recomendacion.adyacentes(v):
            entr[w] += 1
    return entr


def obtener_suma_pesos_grafo(grafo):
    suma = 0
    visitados = set()
    for v in grafo:
        for w in grafo.adyacentes(v):
            if w not in visitados:
                suma += grafo.obtener_peso_arista(v, w)
        visitados.add(v)
    return suma
