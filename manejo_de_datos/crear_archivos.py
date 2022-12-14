import xml.etree.ElementTree as et


def crear_archivo_kml(nombre_archivo, desde, hasta, padres=None, camino_lista=None):
    """
    Crea archivo KML a partir de ( *camino_lista* o *padres*, *desde*, *hasta* ) como
    parametros obligatorios
    """
    kml = Kml(
        f'Camino desde {desde.obtener_nombre()} hacia {hasta.obtener_nombre()}')

    if camino_lista is None:
        camino_lista = []
        while hasta is not None:
            camino_lista.append(hasta)
            hasta = padres[hasta]
        camino_lista = camino_lista[::-1]

    for ciudad in camino_lista:
        kml.agregar_point(ciudad.obtener_nombre(),
                          ciudad.obtener_latitud(), ciudad.obtener_longitud())

    for i in range(len(camino_lista)-1):
        # Agregar aristas (LineStrings)
        nombre = f'{camino_lista[i].obtener_nombre()} - {camino_lista[i+1].obtener_nombre()}'
        coords = [
            (camino_lista[i].obtener_latitud(),
             camino_lista[i].obtener_longitud(),
             0.0),
            (camino_lista[i+1].obtener_latitud(),
             camino_lista[i+1].obtener_longitud(),
             0.0),
        ]
        kml.agregar_linestring(nombre, coords)

    kml.guardar(nombre_archivo)


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
    def __init__(self, nombre_kml=''):
        """
        Crea archivos KML utilizando XML.ETREE.ELEMENTTREE.
        Permite crear points y linestrings
        """
        atributos_kml = {
            'xmlns': 'http://www.opengis.net/kml/2.2',
            'xmlns:gx': 'http://www.google.com/kml/ext/2.2',
        }
        self.raiz = et.Element('kml', attrib=atributos_kml)
        self.doc = et.SubElement(self.raiz, 'Document')
        # et.indent(self.raiz, space='    ', level=0)
        # Para que el .kml sea mas lejible (no incluido porque el corrector automatico no lo tiene)
        et.SubElement(self.doc, 'name').text = nombre_kml

    def agregar_point(self, nombre, lat=0.0, lon=0.0, alt=0.0):
        """
        Crea un point con los datos pasados
        """
        pm = et.SubElement(self.doc, 'Placemark')
        et.SubElement(pm, 'name').text = nombre

        pt = et.SubElement(pm, 'Point')
        et.SubElement(pt, 'coordinates').text = f'{lat},{lon},{alt}'

        # et.indent(self.doc, space='    ', level=1) # Para que el .kml sea mas lejible

    def agregar_linestring(self, name, coords):
        """
        Crea un linestring a partir de un nombre, y una lista de 2 tuplas
        de la forma [(lat1, lon1, alt1), (lat2, lon2, alt2)]
        """
        pm = et.SubElement(self.doc, 'Placemark')
        et.SubElement(pm, 'name').text = name

        ls = et.SubElement(pm, 'LineString')
        coords1 = f'{coords[0][0]},{coords[0][1]},{coords[0][2]}'
        coords2 = f'{coords[1][0]},{coords[1][1]},{coords[1][2]}'
        et.SubElement(ls, 'coordinates').text = f'{coords1} {coords2}'

        # et.indent(self.doc, space='    ', level=1) # Para que el .kml sea mas lejible

    def guardar(self, filename):
        tree = et.ElementTree(self.raiz)
        tree.write(filename, encoding='UTF-8', xml_declaration=True)
