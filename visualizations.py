from pyvis.network import Network  # Graph Visualization
from ciudades import Ciudad

# graph = Network()
# for i in range(4):
#     graph.add_node(i, label=str(i))
# graph.add_edges([(0, 3), (0, 2), (1, 3), (0, 1)])
# graph.show('athus.html')


def crear_network_desde_pajek(archivo='archivos/qatar.pj') -> None:
    grafo = Network()

    with open(archivo) as a:
        numero_vertices = int(a.readline())
        for _ in range(numero_vertices):
            ciudad_nombre, latitud, longitud = a.readline().strip().split(',')
            grafo.add_node(ciudad_nombre, label=str(ciudad_nombre))

        numero_aristas = int(a.readline())
        for _ in range(numero_aristas):
            ciudad1_nombre, ciudad2_nombre, tiempo_ciudad_ciudad = a.readline().strip().split(',')
            grafo.add_edge(ciudad1_nombre, ciudad2_nombre,
                           value=str(tiempo_ciudad_ciudad))

    grafo.show('graph_vis.html')


if __name__ == '__main__':
    crear_network_desde_pajek()
