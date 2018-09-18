import sys


class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None
        self.in_degree = 0
        self.out_degree = 0

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def set_indegree(self, in_degree):
        self.in_degree = in_degree

    def get_indegree(self):
        return self.in_degree

    def get_vertex_id(self):
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
        self.num_vertices = + 1
        new_vertex = Vertex(node)
        self.vert_dictionary[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dictionary:
            return self.vert_dictionary[n]
        else:
            return None

    def add_edge(self, frm, to, cost=1):
        if frm not in self.vert_dictionary:
            self.add_vertex(frm)
        if to not in self.vert_dictionary:
            self.add_vertex(to)

        self.vert_dictionary[frm].add_neighbor(self.vert_dictionary[to], cost)
        self.vert_dictionary[to].in_degree += 1

    def get_vertices(self):
        return self.vert_dictionary

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def get_edges(self):
        edge = []
        for v in self:
            for w in v.get_connections():
                vid = v.get_vertex_id()
                wid = w.get_vertex_id()
                edge.append((vid, wid, v.get_weight(w)))
        return edge


def topological_sort(G):
    ''' Performs tolological sort of the nodes'''
    topological_list = []
    topological_queue = []
    remaining_indegree = {}
    nodes = G.get_vertices()
    for v in G:
        indegree = v.get_indegree()
        if indegree == 0:
            topological_queue.append(v)
        else:
            remaining_indegree[v] = indegree
    while len(topological_queue):
        node = topological_queue.pop(0)
        topological_list.append(node)
        for son in node.get_connections():
            son.set_indegree(son.get_indegree() - 1)
            if son.get_indegree() == 0:
                topological_queue.append(son)
    if len(topological_list) != len(nodes):
        raise GraphTopologicalException(topological_list)
    while len(topological_list):
        node = topological_list.pop(0)
        print(node.get_vertex_id())


if __name__ == '__main__':
    G = Graph()
    G.add_vertex('A')
    G.add_vertex('B')
    G.add_vertex('C')
    G.add_vertex('D')
    G.add_vertex('E')
    G.add_vertex('F')
    G.add_vertex('G')
    G.add_vertex('H')
    G.add_vertex('I')
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('A', 'G')
    G.add_edge('A', 'E')
    G.add_edge('B', 'C')
    G.add_edge('C', 'G')
    G.add_edge('D', 'E')
    G.add_edge('D', 'F')
    G.add_edge('F', 'H')
    G.add_edge('E', 'H')
    G.add_edge('H', 'I')
    print('Graph data:')
    print(G.get_edges())
    topological_sort(G)
