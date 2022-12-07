from pyvis.network import Network  # Graph Visualization
from ciudades import Ciudad


def crear_network_desde_pajek(archivo='archivos/qatar.pj') -> None:
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

    grafo.show('graph_vis.html')


if __name__ == '__main__':
    crear_network_desde_pajek()
