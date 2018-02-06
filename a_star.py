#pylint: disable = W0312
#pylint: disable = E1101
from graph import Graph

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
        

