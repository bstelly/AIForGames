#pylint: disable = W0312
#pylint: disable = E1101
from operator import attrgetter
from graph import Graph

class AStar:
    def __init__(self, start, end, graph):
        self.grid = graph
        self.open_list = []
        self.closed_list = []
        self.start_node = start
        self.goal_node = end
        self.current_node = start
        self.path = None

    def find_current(self):
        '''Function to find the current node in the path
        the current node gets added to the closed list and then removed from the open list'''
        self.current_node = min(self.open_list, key=attrgetter('f_score'))
        self.closed_list.append(self.current_node)
        self.open_list.remove(self.current_node)
    def find_path(self):
        '''Function to generate a path from start to end node'''
        self.open_list.append(self.start_node)
        while not self.closed_list.__contains__(self.goal_node) and self.open_list:
            self.find_current()
            neighbors = self.grid.get_neighbors(self.current_node)
            for neighbor in neighbors:
                if (neighbor.is_traversable and not self.closed_list.__contains__(neighbor)):
                    #Check to see if neighbor is in open list. If not append it and calculate
                    #g, h, and f scores, then set the parent of the neigbor as the current node
                    if not self.open_list.__contains__(neighbor):
                        self.open_list.append(neighbor)
                        neighbor.calc_g_score(self.current_node)
                        neighbor.calc_h_score(self.goal_node)
                        neighbor.calc_f_score()
                        neighbor.set_parent(self.current_node)
                    #If neighbor is already in the open list, it already has a parent, so
                    #recalculate g score to find better path. Recalculate h and f scores
                    #incase path changes
                    elif self.open_list.__contains__(neighbor):
                        neighbor.calc_g_score(self.current_node)
                        neighbor.calc_h_score(self.goal_node)
                        neighbor.calc_f_score()
                    #Check to see if goal node is found, then add it to the closed list
                    #and set goal node as current
                    if neighbor.position == self.goal_node.position:
                        self.closed_list.append(self.goal_node)
                        self.find_current()
        #Create the path
        path = []
        while self.current_node.parent:
            path.append(self.current_node)
            self.current_node = self.current_node.parent
        path.append(self.current_node)
        self.path = path
        return path

    def print_path(self):
        '''Function that will print the path that is found'''
        counter = 0
        for node in self.grid.nodes:
            if counter is self.grid.length:
                print '\n',
                counter = 0
            if node.is_traversable is False:
                print'[X]',
            elif node.is_start:
                print '[S]',
            elif node.is_goal:
                print '[G]',
            elif self.path.__contains__(node):
                print '[o]',
            else:
                print '[ ]',
            counter += 1


