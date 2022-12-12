
class Ciudad:

    def __init__(self, nombre, lat, lon):
        """
        Crea un objeto Ciudad con los datos pasados al instanciarse la clase (nombre, lat, lon)
        """
        self.__nombre = nombre
        self.__lat = lat
        self.__lon = lon

    def obtener_nombre(self):
        return self.__nombre

    def obtener_latitud(self):
        return self.__lat

    def obtener_longitud(self):
        return self.__lon
