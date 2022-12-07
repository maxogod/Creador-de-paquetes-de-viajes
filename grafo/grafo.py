from sys import getsizeof


class Grafo:

    def __init__(self, dirigido=False, lista_nodos=None):
        if lista_nodos is None:
            lista_nodos = []
        self.datos = {}  # Dict of dicts
        self.es_dirigido = dirigido
        for i in lista_nodos:
            self.datos[i] = {}

    def __len__(self):
        return len(self.datos)

    def __sizeof__(self):
        return getsizeof(self.datos)

    def __iter__(self):
        self.iter = iter(self.datos)
        return self

    def __next__(self):
        return next(self.iter)

    def agregar_nodo(self, v):
        self.datos[v] = {}

    def agregar_arista(self, v, w, peso=None):
        if v not in self.datos or w not in self.datos:
            raise Exception("NodoInexistente")
        if self.es_dirigido:
            self.datos[v][w] = peso
        else:
            self.datos[v][w] = peso
            self.datos[w][v] = peso

    def adyacentes(self, v):
        return self.datos[v].keys()

    def obtener_peso_arista(self, v, w):
        if not self.arista_existe(v, w):
            raise Exception("AristaInexistente")
        return self.datos[v][w]

    def arista_existe(self, v, w):
        return w in self.datos[v]

    def sacar_arista(self, v, w):
        if not self.arista_existe(v, w):
            raise Exception("AristaInexistente")
        if self.es_dirigido:
            del self.datos[v][w]
        else:
            del self.datos[v][w]
            del self.datos[w][v]

    def sacar_nodo(self, v):
        del self.datos[v]
        for i in self.datos:
            if v in self.datos[i]:
                del self.datos[i][v]

    def obtener_un_nodo(self):
        """ Retorna un nodo NO random """
        for i in self.datos:
            return i
