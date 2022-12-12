from pyvis.network import Network  # Graph Visualization
from manejo_de_datos.tdas.grafo import Grafo


def crear_network_desde_pajek(archivo='archivos/qatar.pj', nuevo='graph_vis.html') -> None:
    grafo = Network()

    with open(archivo) as a:
        numero_vertices = int(a.readline())
        for _ in range(numero_vertices):
            ciudad_nombre, latitud, longitud = a.readline().strip().split(',')
            grafo.add_node(ciudad_nombre, label=str(
                ciudad_nombre), color='#85fff3', mass=5)

        numero_aristas = int(a.readline())
        for _ in range(numero_aristas):
            ciudad1_nombre, ciudad2_nombre, tiempo_ciudad_ciudad = a.readline().strip().split(',')
            grafo.add_edge(ciudad1_nombre, ciudad2_nombre,
                           title=str(tiempo_ciudad_ciudad), color='#77DD77')

    grafo.show(nuevo)


if __name__ == '__main__':
    crear_network_desde_pajek(
        'archivos_tests/qatar.pj', 'visualizations/graph_vis.html')
