from sys import getsizeof


class Grafo:

    def __init__(self, dirigido=False, lista_nodos=None):
        """
        Crea un grafo (dict de dicts) a partir de los parametros opcionales (dirigido, lista_nodos)
        y permite aplicar sobre este diferentes metodos
        """
        if lista_nodos is None:
            lista_nodos = []
        self.__datos = {}  # Dict of dicts
        self.__es_dirigido = dirigido
        for i in lista_nodos:
            self.__datos[i] = {}

    def __len__(self):
        return len(self.__datos)

    def __sizeof__(self):
        return getsizeof(self.__datos)

    def __iter__(self):
        self.__iter = iter(self.__datos)
        return self

    def __next__(self):
        return next(self.__iter)

    def agregar_nodo(self, v):
        self.__datos[v] = {}

    def agregar_arista(self, v, w, peso=None):
        if v not in self.__datos or w not in self.__datos:
            raise Exception("NodoInexistente")
        if self.__es_dirigido:
            self.__datos[v][w] = peso
        else:
            self.__datos[v][w] = peso
            self.__datos[w][v] = peso

    def adyacentes(self, v):
        return self.__datos[v].keys()

    def obtener_peso_arista(self, v, w):
        if not self.arista_existe(v, w):
            raise Exception("AristaInexistente")
        return self.__datos[v][w]

    def arista_existe(self, v, w):
        return w in self.__datos[v]

    def sacar_arista(self, v, w):
        if not self.arista_existe(v, w):
            raise Exception("AristaInexistente")
        if self.__es_dirigido:
            del self.__datos[v][w]
        else:
            del self.__datos[v][w]
            del self.__datos[w][v]

    def sacar_nodo(self, v):
        del self.__datos[v]
        for i in self.__datos:
            if v in self.__datos[i]:
                del self.__datos[i][v]

    def obtener_un_nodo(self):
        """ Retorna un nodo NO random """
        for i in self.__datos:
            return i

    def obtener_nodos(self):
        return self.__datos.keys()
