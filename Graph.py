from node import Node
from vector2 import Vector2


class Graph:
    '''Graph Class for storing nodes'''

    def create_nodes(self):
        '''Fill the Graph with nodes'''
        for i in range(0, self.length):
            for j in range(0, self.height):
                new_node = Node(Vector2(i, j))
                self.nodes.append(new_node)

    def __init__(self, length, height):
        '''Constructor for Graph class'''
        self.length = length
        self.height = height
        self.nodes = []
        self.create_nodes()


