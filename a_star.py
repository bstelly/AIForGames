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
        self.goal_node = end
        self.current_node = start
        self.open_list.append(start)
        self.path = []

    def set_start(self, start_node):
        self.start_node = start_node
        self.current_node = start_node
        self.open_list.append(start_node)

    def set_goal(self, goal_node):
        self.goal_node = goal_node

    def find_current(self):
        '''Function to find the current node in the path'''
        #Find current node, add current node to closed list and remove it from open list
        self.current_node = min(self.open_list, key=attrgetter('f_score'))
        self.closed_list.append(self.current_node)
        self.open_list.remove(self.current_node)

    def find_path(self):
        '''Function to generate a path from start to end node'''
        self.reset()
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
        if self.closed_list.__contains__(self.goal_node):
            path = []
            while self.current_node.parent:
                path.append(self.current_node)
                self.current_node = self.current_node.parent
            path.append(self.current_node)
            self.path = path
            path.reverse()
            return path

    def reset(self):
        '''Delete open list, closed list, path, and set all node
        parents to None for running AStar more than once'''
        del self.open_list[:]
        del self.closed_list[:]
        del self.path[:]
        for node in self.grid.nodes:
            node.parent = None

    def update(self, start_node, goal_node):
        self.set_start(start_node)
        self.set_goal(goal_node)
        self.find_path()
