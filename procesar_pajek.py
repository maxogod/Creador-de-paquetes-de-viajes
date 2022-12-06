from graph.graph import Graph
from ciudades import Ciudad


def crear_grafo_desde_pajek(archivo, nombre_a_ciudad) -> Graph:
    grafo = Graph()

    with open(archivo) as a:
        numero_vertices = int(a.readline())
        for _ in range(numero_vertices):
            ciudad_nombre, latitud, longitud = a.readline().strip().split(',')
            ciudad_objeto = Ciudad(
                ciudad_nombre, float(latitud), float(longitud))
            nombre_a_ciudad[ciudad_nombre] = ciudad_objeto
            grafo.add_node(ciudad_objeto)

        numero_aristas = int(a.readline())
        for _ in range(numero_aristas):
            ciudad1_nombre, ciudad2_nombre, tiempo_ciudad_ciudad = a.readline().strip().split(',')
            ciudad1, ciudad2 = nombre_a_ciudad[ciudad1_nombre], nombre_a_ciudad[ciudad2_nombre]
            grafo.add_edge(ciudad1, ciudad2, int(tiempo_ciudad_ciudad))

    return grafo
