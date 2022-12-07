
class Ciudad:

    def __init__(self, nombre, lat, lon):
        """
        Crea un objeto Ciudad con los datos pasados al instanciarse la clase (nombre, lat, lon)
        """
        self.nombre = nombre
        self.lat = lat
        self.lon = lon

    def obtener_nombre(self):
        return self.nombre

    def obtener_latitud(self):
        return self.lat

    def obtener_longitud(self):
        return self.lon
