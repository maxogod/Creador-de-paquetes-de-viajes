import simplekml


def crear_archivo_kml(nombre_archivo, desde, hasta, padres):
    kml = simplekml.Kml()
    kml.document.name = f'Camino desde {desde.obtener_nombre()} hacia {hasta.obtener_nombre()}'

    camino_lista = []
    while hasta is not None:
        camino_lista.append(hasta)
        hasta = padres[hasta]
    camino_lista = camino_lista[::-1]

    for ciudad in camino_lista:
        kml.newpoint(name=ciudad.obtener_nombre(), coords=[
                     (ciudad.obtener_latitud(), ciudad.obtener_longitud())])
    kml.save(nombre_archivo)


def crear_archivo_pj(nombre_archivo, arbol):
    with open(nombre_archivo, 'w') as archivo_pj:

        archivo_pj.write(f'{len(arbol)}\n')

        cantidad_aristas = 0
        visitado = set()
        lista_aristas = []

        for v in arbol:
            archivo_pj.write(
                f'{v.obtener_nombre()},{v.obtener_latitud()},{v.obtener_longitud()}\n')
            visitado.add(v)
            for w in arbol.adyacentes(v):
                if w not in visitado:
                    cantidad_aristas += 1
                    lista_aristas.append(
                        (v.obtener_nombre(), w.obtener_nombre(), arbol.obtener_peso_arista(v, w)))

        archivo_pj.write(f'{cantidad_aristas}\n')
        for arista in lista_aristas:  # arista = (v, w, peso)
            archivo_pj.write(f'{arista[0]},{arista[1]},{arista[2]}\n')


if __name__ == '__main__':
    crear_archivo_kml('athus.kml')
