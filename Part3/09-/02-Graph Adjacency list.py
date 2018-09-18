import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_vertexID(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_previous(self, previous):
        self.previous = previous

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dictionary = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dictionary.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dictionary[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        for n in self.vert_dictionary:
            return self.vert_dictionary[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dictionary:
            self.add_vertex(frm)
        if to not in self.vert_dictionary:
            self.add_vertex(to)
        
        self.vert_dictionary[frm].add_neighbor(self.vert_dictionary[to], cost)
        # self.vert_dictionary[to].add_neighbor(self.vert_dictionary(frm), cost)

    def get_vertices(self):
        return self.vert_dictionary.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self):
        return self.previous

    def get_edges(self):
        edges = []
        for v in self:
            for w in v.get_connections():
                vid = v.get_vertexID()
                wid = w.get_vertexID()
                edges.append((vid, wid, v.get_weight(w)))
        return edges

def main():
    print('This is main')
    G = Graph()
    G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')
    G.add_vertex('f')
    G.add_vertex('g')
    G.add_edge('a', 'b', 5)
    G.add_edge('b', 'a', 5)
    G.add_edge('b', 'd', 10)
    G.add_edge('e', 'f', 15)
    G.add_edge('g', 'a', 12)
    G.add_edge('f', 'd', 8)
    G.add_edge('c', 'a', 4)
    print('Graph Data: ')
    print(G.get_edges())


if __name__ == '__main__':
    main()
