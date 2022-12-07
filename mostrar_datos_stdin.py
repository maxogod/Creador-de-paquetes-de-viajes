
def mostrar_camino(padres, hasta, tiempo=None):
    """
    Imprime en StdIn el camino determinado por el diccionario *padres* hacia *hasta*.
    En caso un *tiempo* sea pasado este tambien sera impreso en la proxima linea
    """
    camino_lista = []
    while hasta is not None:
        camino_lista.append(hasta)
        hasta = padres[hasta]
    camino_lista = camino_lista[::-1]

    camino = ""
    for ciudad in camino_lista:
        ciudad_nombre = ciudad.obtener_nombre()
        if ciudad == camino_lista[-1]:
            camino += ciudad_nombre
        else:
            camino += ciudad_nombre + ' -> '

    return f"{camino}" if tiempo is None else f"{camino}\nTiempo total:{tiempo}"
