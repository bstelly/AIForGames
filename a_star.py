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
        #Can't depend on the nodes being found in a specific order everytime
        for node in self.grid.nodes:
            for pos in neighbors:
                if (node == pos and node.is_traversable and node not in self.closed_list):
                    if node not in self.open_list:
                        self.open_list.append(node)
                    node.calc_g_score(self.current_node)
                    node.calc_h_score(self.end_node)
                    node.calc_f_score()
                    node.set_parent(self.current_node)




#                    if node.parent is not None:
#                        if node.g_score < :
#                            node.set_parent(self.current_node)
#                    elif node.parent is None:
#                        node.set_parent(self.current)
