from .tdas.grafo import Grafo
from .tdas.ciudades import Ciudad


def crear_grafo_desde_pajek(archivo, nombre_a_ciudad):
    """
    Procesa el archivo .pj, y Crea un grafo en base a este.
    Simultaneamente llena el diccionario *nombre_a_ciudad* con la informacion correspondiente
    """
    grafo_ciudades = Grafo()

    with open(archivo) as a:

        numero_vertices = int(a.readline())

        for _ in range(numero_vertices):
            ciudad_nombre, latitud, longitud, altitud = a.readline().strip().split(',')
            ciudad_objeto = Ciudad(
                ciudad_nombre, float(latitud), float(longitud), float(altitud))
            nombre_a_ciudad[ciudad_nombre] = ciudad_objeto
            grafo_ciudades.agregar_nodo(ciudad_objeto)

        numero_aristas = int(a.readline())

        for _ in range(numero_aristas):
            ciudad1_nombre, ciudad2_nombre, tiempo_ciudad_ciudad = a.readline().strip().split(',')
            ciudad1, ciudad2 = nombre_a_ciudad[ciudad1_nombre], nombre_a_ciudad[ciudad2_nombre]
            grafo_ciudades.agregar_arista(
                ciudad1, ciudad2, int(tiempo_ciudad_ciudad))

    return grafo_ciudades


def crear_grafo_recomendaciones_csv(recomendaciones, nombre_a_ciudad):
    grafo_itinerario = Grafo(dirigido=True)
    with open(recomendaciones) as r:
        for line in r:
            ciudad1_nombre, ciudad2_nombre = line.strip().split(",")
            ciudad1, ciudad2 = nombre_a_ciudad[ciudad1_nombre], nombre_a_ciudad[ciudad2_nombre]
            if ciudad1 not in grafo_itinerario:
                grafo_itinerario.agregar_nodo(ciudad1)
            if ciudad2 not in grafo_itinerario:
                grafo_itinerario.agregar_nodo(ciudad2)
            grafo_itinerario.agregar_arista(ciudad1, ciudad2)

    return grafo_itinerario
