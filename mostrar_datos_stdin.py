
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


def mostrar_camino_itinerario(lista_itinerario,tiempo_total):

    camino = ""
    for ciudad in lista_itinerario:
        if ciudad == lista_itinerario[-1]:
            camino = camino + ciudad.obtener_nombre()
        else:
            camino = ciudad.obtener_nombre() + "->"

    return f"{camino}\nTiempo total:{tiempo_total}"

