from pyvis.network import Network  # Graph Visualization
from manejo_de_datos.tdas.grafo import Grafo


def crear_network_desde_pajek(archivo_a_analizar, visualizacion='graph_vis.html') -> None:
    grafo = Network()

    with open(archivo_a_analizar) as a:
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

    grafo.show(visualizacion)


def create_pj_files():
    with open('gigante.pj', 'w') as f:
        f.write('1000000\n')
        for i in range(1000000):
            f.write(f'N{i},1,1\n')
        f.write('1000000\n')
        for i in range(1000000-1):
            f.write(f'N{i},N{i+1},1\n')
        f.write('N0,N999999,1\n')

    with open('small.pj', 'w') as f:
        f.write('5\n')
        for i in range(5):
            f.write(f'N{i},1,1\n')
        f.write('5\n')
        for i in range(5-1):
            f.write(f'N{i},N{i+1},1\n')
        f.write('N0,N4,1\n')


if __name__ == '__main__':
    crear_network_desde_pajek(
        '<nombre>.pj', '<nombre>.html')
