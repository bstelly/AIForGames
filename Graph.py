from node import Node
from vector2 import Vector2

class Graph:
    '''Graph Class for storing nodes'''
    def __init__(self, length, height):
        '''Contructor for Graph class'''
        self.length = length
        self.height = height
        self.nodes = []

    def create_nodes(self):
        '''Fill the Graph with nodes'''
        for i in range(0, self.length):
            for j in range(0, self.height):
                new_node = Node(Vector2(i, j))
                self.nodes.append(new_node)

GRID = Graph(10, 10)
GRID.create_nodes()
print GRID.nodes

CURRENT_NODE = Node(Vector2(5, 10))
FIRST_NODE = Node(Vector2(5, 10))
SECOND_NODE = Node(Vector2(10, 25))

CURRENT_NODE.calc_g_score(FIRST_NODE)
print CURRENT_NODE.g_score
CURRENT_NODE.calc_g_score(SECOND_NODE)
print CURRENT_NODE.g_score

CURRENT_NODE.calc_h_score(SECOND_NODE)
print CURRENT_NODE.h_score

CURRENT_NODE.calc_f_score()
print CURRENT_NODE.f_score
