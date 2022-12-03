import simplekml


def crear_archivo_kml(nombre_archivo=None):
    kml = simplekml.Kml()
    kml.document.name = 'Dohathus'
    kml.newpoint(name='Doha', coords=[(25.286549, 51.534741)])
    kml.save('athus.kml')


def crear_archivo_pj(nombre_archivo):
    pass


def crear_archivo_csv(nombre_archivo):
    pass


crear_archivo_kml()
