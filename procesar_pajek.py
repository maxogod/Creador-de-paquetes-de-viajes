from grafo.grafo import Grafo
from ciudades import Ciudad


def crear_grafo_desde_pajek(archivo, nombre_a_ciudad) -> Grafo:
    """
    Procesa el archivo .pj, y Crea un grafo en base a este.
    Simultaneamente llena el diccionario *nombre_a_ciudad* con la informacion correspondiente
    """
    grafo = Grafo()

    with open(archivo) as a:

        numero_vertices = int(a.readline())

        for _ in range(numero_vertices):
            ciudad_nombre, latitud, longitud = a.readline().strip().split(',')
            ciudad_objeto = Ciudad(
                ciudad_nombre, float(latitud), float(longitud))
            nombre_a_ciudad[ciudad_nombre] = ciudad_objeto
            grafo.agregar_nodo(ciudad_objeto)

        numero_aristas = int(a.readline())

        for _ in range(numero_aristas):
            ciudad1_nombre, ciudad2_nombre, tiempo_ciudad_ciudad = a.readline().strip().split(',')
            ciudad1, ciudad2 = nombre_a_ciudad[ciudad1_nombre], nombre_a_ciudad[ciudad2_nombre]
            grafo.agregar_arista(ciudad1, ciudad2, int(tiempo_ciudad_ciudad))

    return grafo


if __name__ == '__main__':
    grafo = crear_grafo_desde_pajek('archivos/qatar.pj', {})
    for v in grafo:
        print(f'\n{v.obtener_nombre()}\n')
        for w in grafo.adyacentes(v):
            print(w.obtener_nombre())
