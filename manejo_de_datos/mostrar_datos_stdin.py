
def mostrar_camino(padres=None, hasta=None, tiempo=None, camino_lista=None) -> str:
    """
    Toma SI O SI parametros **(padre & hasta) o (camino_lista)**
    En caso un *tiempo* sea pasado este sera agregado al final del string format
    """
    if camino_lista is None:
        camino_lista = []
        while hasta is not None:
            camino_lista.append(hasta)
            hasta = padres[hasta]
        camino_lista = camino_lista[::-1]

    camino = ""
    for idx, ciudad in enumerate(camino_lista):
        if idx == len(camino_lista)-1:
            camino += ciudad.obtener_nombre()
        else:
            camino += ciudad.obtener_nombre() + " -> "

    return f"{camino}" if tiempo is None else f"{camino}\nTiempo total:{tiempo}"


def mostrar_peso_total(grafo) -> str:
    peso = 0
    visitados = set()
    for v in grafo:
        visitados.add(v)
        for w in grafo.adyacentes(v):
            if not w in visitados:
                peso += grafo.obtener_peso_arista(v, w)
    return f'Peso total: {peso}'
