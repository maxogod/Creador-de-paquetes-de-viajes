
class Ciudad:

    def __init__(self, nombre, lon, lat, alt):
        """
        Crea un objeto Ciudad con los datos pasados al instanciarse la clase (nombre, lat, lon)
        """
        self.__nombre = nombre
        self.__lon = lon
        self.__lat = lat
        self.__alt = alt

    def obtener_nombre(self):
        return self.__nombre

    def obtener_longitud(self):
        return self.__lon

    def obtener_latitud(self):
        return self.__lat

    def obtener_altitud(self):
        return self.__alt
