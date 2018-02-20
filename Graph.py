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

    def get_neighbors(self, current_node):
        '''Returns a list of valid neighbor positions'''
        #List of valid neighbor positions
        neighbors_positions = [(current_node.position + Vector2(0, 1)), #Top
                               (current_node.position + Vector2(0, -1)), #Bot
                               (current_node.position + Vector2(1, 0)), #Right
                               (current_node.position + Vector2(-1, 0)), #Left
                               (current_node.position + Vector2(1, 1)), #Top Right
                               (current_node.position + Vector2(-1, 1)), #Top Left
                               (current_node.position + Vector2(1, -1)), #Bot Right
                               (current_node.position + Vector2(-1, -1))] #Bot Left
        neighbors = []
        for node in self.nodes:
            for pos in neighbors_positions:
                if node.position == pos:
                    neighbors.append(node)
        return neighbors

TEST_GRID = Graph(10, 10)
POSITION = Vector2(2, 5)
TEST_NODE = Node(POSITION)
TEST_GRID.get_neighbors(TEST_NODE)
