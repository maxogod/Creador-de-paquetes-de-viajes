from sys import getsizeof


class Graph:

    def __init__(self, directed=False, nodes_list=()):
        if nodes_list is None:
            nodes_list = []
        self.data = {}  # Dict of dicts
        self.is_directed = directed
        for i in nodes_list:
            self.data[i] = {}

    def __len__(self):
        return len(self.data)

    def __sizeof__(self):
        return getsizeof(self.data)

    def __iter__(self):
        self.iter = iter(self.data)
        return self

    def __next__(self):
        return next(self.iter)

    def add_node(self, v):
        self.data[v] = {}

    def add_edge(self, v, w, weight=None):
        if v not in self.data or w not in self.data:
            raise Exception("NodeDoesntExist")
        if self.is_directed:
            self.data[v][w] = weight
        else:
            self.data[v][w] = weight
            self.data[w][v] = weight

    def get_edges_of_node(self, v):
        return self.data[v].keys()

    def get_weight_of_edge(self, v, w):
        if not self.edge_exists(v, w):
            raise Exception("InexistentEdge")
        return self.data[v][w]

    def edge_exists(self, v, w):
        return w in self.data[v]

    def remove_edge(self, v, w):
        if not self.edge_exists(v, w):
            raise Exception("InexistentEdge")
        if self.is_directed:
            del self.data[v][w]
        else:
            del self.data[v][w]
            del self.data[w][v]

    def remove_node(self, v):
        del self.data[v]
        for i in self.data:
            if v in self.data[i]:
                del self.data[i][v]

    def get_a_node(self):
        """ Returns a non-random node """
        # I could make it random but I'd have to use a second dict, and it'd make the graph
        # O(2V + E) in memory instead of O(V + E). maybe I do it eventually
        for i in self.data:
            return i


# def populated_graph() -> Graph:
#     """ Returns a small undirected and unweighted graph for **testing** """
#     g = Graph()
#     for i in "ABCDEFGHIJK":
#         g.add_node(i)
#     g.add_edge("A", "B")
#     g.add_edge("A", "D")
#     g.add_edge("A", "E")
#     g.add_edge("A", "C")
#     g.add_edge("C", "J")
#     g.add_edge("D", "G")
#     g.add_edge("G", "H")
#     g.add_edge("G", "F")
#     g.add_edge("G", "I")
#     g.add_edge("K", "G")
#     return g
