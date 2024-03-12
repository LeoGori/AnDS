from Node import Node
import random

WHITE = 'WHITE'
GRAY = 'GRAY'
BLACK = 'BLACK'


class Graph:

    def __init__(self):
        self.__v = []
        self.__adj = {}
        self.__scc_v = []

    def get_v(self):
        return self.__v

    def random_v(self, dim):
        for i in range(dim):
            a = Node()
            self.__v.append(a)

    def random_adj(self, prob):
        for vertex in self.__v:
            self.__adj[vertex] = []

        for vertex_i in self.__v:
            for vertex_j in self.__v:
                if vertex_j is not vertex_i:
                    num = random.random()
                    if num < prob or num == 1:
                        self.add_arc(vertex_i, vertex_j)

    def set_v(self, v):
        self.__v = v
        for vertex in self.__v:
            self.__adj[vertex] = []

    def print(self):
        for k, v in self.__adj.items():
            print(k, " => ", v)

    def print_v(self):
        for v in self.get_v():
            v.print()

    def add_arc(self, node_i, node_j):
        self.__adj[node_i].append(node_j)

    def dfs(self):
        for i in self.__v:
            i.set_color(WHITE)

        time = 0

        for i in self.__v:
            if i.get_color() is WHITE:
                time = self.dfs_visit(i, time)

    def dfs_visit(self, current_node, time):
        time = time + 1
        current_node.set_d(time)
        current_node.set_color(GRAY)
        for adj_node in self.__adj[current_node]:
            if adj_node.get_color() is WHITE:
                adj_node.set_father(current_node)
                time = self.dfs_visit(adj_node, time)
        current_node.set_color(BLACK)
        time = time + 1
        current_node.set_f(time)

        self.__scc_v.insert(0, current_node)

        return time

    def get_transpose(self):
        g = Graph()

        g.set_v(self.__scc_v)

        for v in g.get_v():
            v.reset()

        for node in self.__v:
            for adj_node in self.__adj[node]:
                g.add_arc(adj_node, node)

        return g

    def get_scc(self):

        count = 0
        for v in self.__v:
            if v.get_father() is None:
                count = count + 1

        return count
