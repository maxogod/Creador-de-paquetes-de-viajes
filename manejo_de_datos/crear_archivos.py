
def crear_archivo_kml(nombre_archivo, desde, hasta, padres=None, camino_lista=None):
    """
    Crea archivo KML a partir de ( *camino_lista* o *padres*, *desde*, *hasta* ) como
    parametros obligatorios
    """
    kml = Kml(nombre_archivo,
              f'Camino desde {desde.obtener_nombre()} hacia {hasta.obtener_nombre()}')

    if camino_lista is None:
        camino_lista = []
        while hasta is not None:
            camino_lista.append(hasta)
            hasta = padres[hasta]
        camino_lista = camino_lista[::-1]

    puntos_agregados = set()  # Para asegurarse de no repetir puntos (ej en comando -viaje-)
    for ciudad in camino_lista:
        if ciudad.obtener_nombre() not in puntos_agregados:
            kml.agregar_point(ciudad.obtener_nombre(),
                              ciudad.obtener_longitud(), ciudad.obtener_latitud(), ciudad.obtener_altitud())
            puntos_agregados.add(ciudad.obtener_nombre())

    for i in range(len(camino_lista)-1):
        # Agregar aristas (LineStrings)
        nombre = f'{camino_lista[i].obtener_nombre()} - {camino_lista[i+1].obtener_nombre()}'
        coords = [
            (camino_lista[i].obtener_longitud(),
             camino_lista[i].obtener_latitud(),
             camino_lista[i].obtener_altitud(),),
            (camino_lista[i+1].obtener_longitud(),
             camino_lista[i+1].obtener_latitud(),
             camino_lista[i+1].obtener_altitud(),),
        ]
        kml.agregar_linestring(coords, nombre)

    kml.guardar()


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


class Kml():
    def __init__(self, nombre_archivo, nombre_kml='default'):
        """
        Crea archivos KML con el nombre pasado Permite crear points y linestrings
        """
        self.kml = open(nombre_archivo, 'w')
        self.kml.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        self.kml.write(
            '<kml xmlns="http://earth.google.com/kml/2.1">\n\t<Document>\n')
        self.kml.write(f'\t\t<name>{nombre_kml}</name>\n')

    def agregar_point(self, nombre, lat=0.0, lon=0.0, alt=0.0):
        """
        Crea un point con los datos pasados
        """
        self.kml.write('\t\t<Placemark>\n')
        self.kml.write(f'\t\t\t<name>{nombre}</name>\n')
        self.kml.write(
            f'\t\t\t<Point>\n\t\t\t\t<coordinates>{lat},{lon},{alt}</coordinates>\n\t\t\t</Point>\n')
        self.kml.write('\t\t</Placemark>\n')

    def agregar_linestring(self, coords, nombre):
        """
        Crea un linestring a partir de un nombre, y una lista de 2 tuplas
        de la forma [(lat1, lon1), (lat2, lon2)]
        """
        coords1 = f'{coords[0][0]},{coords[0][1]},{coords[0][2]}'
        coords2 = f'{coords[1][0]},{coords[1][1]},{coords[1][2]}'
        self.kml.write('\t\t<Placemark>\n')
        self.kml.write(f'\t\t\t<name>{nombre}</name>\n')
        self.kml.write(
            f'\t\t\t<LineString>\n\t\t\t\t<coordinates>{coords1} {coords2}</coordinates>\n\t\t\t</LineString>\n')
        self.kml.write('\t\t</Placemark>\n')

    def guardar(self):
        self.kml.write('\t</Document>\n</kml>')
        self.kml.close()
