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


def crear_archivo_pj(nombre_archivo):
    pass

if __name__ == '__main__':
    crear_archivo_kml('athus.kml')
