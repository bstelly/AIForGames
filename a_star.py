#pylint: disable = W0312
#pylint: disable = E1101
from operator import attrgetter
from graph import Graph
from vector2 import Vector2
from node import Node

class AStar:
    def __init__(self, graph, start, end):
        self.grid = graph
        self.open_list = []
        self.closed_list = []
        self.start_node = start
        self.end_node = end
        self.current_node = start
        self.open_list.append(start)
        self.path = None

    def find_current(self):
        '''Function to find the current node in the path'''
        self.current_node = min(self.open_list, key=attrgetter('f_score'))
        self.closed_list.append(min(self.open_list, key=attrgetter('f_score')))
        index = self.open_list.index(min(self.open_list, key=attrgetter('f_score')))
        self.open_list.pop(index)

    def find_path(self):
        '''Function to generate a path from start to end node'''
        while not self.closed_list.__contains__(self.end_node) and self.open_list:
            self.find_current()
            neighbors = self.grid.get_neighbors(self.current_node)
            for neighbor in neighbors:
                if (neighbor.is_traversable and not self.closed_list.__contains__(neighbor)):
                    if not self.open_list.__contains__(neighbor):
                        self.open_list.append(neighbor)
                        neighbor.calc_g_score(self.current_node)
                        neighbor.calc_h_score(self.end_node)
                        neighbor.calc_f_score()
                        neighbor.set_parent(self.current_node)
                    elif self.open_list.__contains__(neighbor):
                        neighbor.calc_g_score(self.current_node)
                        neighbor.calc_h_score(self.end_node)
                        neighbor.calc_f_score()
                    if neighbor.position == self.end_node.position:
                        self.closed_list.append(self.end_node)
                        self.find_current()
        path = []
        while self.current_node.parent:
            path.append(self.current_node)
            self.current_node = self.current_node.parent
        path.append(self.current_node)
        self.path = path

    def print_path(self):
        counter = 0
        for node in self.grid.nodes:
            if counter is 10:
                print '\n',
                counter = 0
            if node.is_traversable is False:
                print'[#]',
            elif AI.start_node.position == node.position:
                print '[S]',
            elif AI.end_node.position == node.position:
                print '[G]',
            elif AI.path.__contains__(node):
                print '[x]',
            else:
                print '[ ]',
            counter += 1
        print 'done'




TEST_Grid = Graph(10, 10)
START = Node(Vector2(2, 0))
END = Node(Vector2(2, 4))
TEST_Grid.nodes[12].toggle_traversable()
TEST_Grid.nodes[22].toggle_traversable()
TEST_Grid.nodes[32].toggle_traversable()

AI = AStar(TEST_Grid, START, END)
AI.find_path()
AI.print_path()