#pylint: disable = W0312
#pylint: disable = E1101
from graph import Graph
from vector2 import Vector2
from node import Node
class A_star:
    def __init__(self, graph, start, end):
        self.grid = graph
        self.open_list = []
        self.closed_list = []
        self.start_node = start
        self.end_node = end
        self.current_node = start
        self.open_list.append(start)

    def get_neighbors(self):
        neighbors = [(self.current_node.position + Vector2(0, 1)), #Top
                     (self.current_node.position + Vector2(0, -1)), #Bot
                     (self.current_node.position + Vector2(1, 0)), #Right
                     (self.current_node.position + Vector2(-1, 0)), #Left
                     (self.current_node.position + Vector2(1, 1)), #Top Right
                     (self.current_node.position + Vector2(-1, 1)), #Top Left
                     (self.current_node.position + Vector2(1, -1)), #Bot Right
                     (self.current_node.position + Vector2(-1, -1))] #Bot Left
        counter = 0
        for node in self.grid.nodes:
            for pos in neighbors:
                if (self.grid.nodes[node].position is neighbors[pos] and
                        self.grid.node[node].is_transversable is True and counter <= 8):
                    self.open_list.append(self.grid.node[node])
                    self.grid.node[node].parent = self.current_node
                    counter += 1
    
    def find_gscore(self):
        