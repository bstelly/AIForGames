#pylint: disable = W0312
#pylint: disable = E1101
from operator import attrgetter
from graph import Graph
from vector2 import Vector2

class AStar:

    #Prototype: def __init__(self)
    #Arguments: None
    #Description: Creates an instance of the AStar class
    #Precondition: None
    #Postcondition: An instance of the AStar class is created
    def __init__(self):
        self.grid = None
        self.open_list = []
        self.closed_list = []
        self.start_node = None
        self.goal_node = None
        self.current_node = None
        self.path = None

    #Prototype: def find_current(self)
    #Arguments: None
    #Description: Finds the current node in the path, adds it to the closed list and removes it
    #             from the open list
    #Precondition: There must be an instance of the AStar class
    #Postcondition: The current node is found, added to the closed list, and removed from open list
    def find_current(self):
        '''Function to find the current node in the path
        the current node gets added to the closed list and then removed from the open list'''
        self.current_node = min(self.open_list, key=attrgetter('f_score'))
        self.closed_list.append(self.current_node)
        self.open_list.remove(self.current_node)

    #Prototype: def find_path(self, start, goal, graph)
    #Arguments: A Node object for start, a Node object for goal, and a graph object for graph
    #Description: Finds the path from start node to goal node
    #Precondition: There must be an instance of AStar
    #Postcondition: The path is found and returned as a list of nodes
    def find_path(self, start, goal, graph):
        '''Function to generate a path from start to end node'''
        self.start_node = start
        self.goal_node = goal
        self.grid = graph
        self.open_list.append(self.start_node)
        while not self.closed_list.__contains__(self.goal_node) and self.open_list:
            self.find_current()
            valid_positions = [(self.current_node.position + Vector2(0, 1)), #Top
                               (self.current_node.position + Vector2(0, -1)), #Bot
                               (self.current_node.position + Vector2(1, 0)), #Right
                               (self.current_node.position + Vector2(-1, 0)), #Left
                               (self.current_node.position + Vector2(1, 1)), #Top Right
                               (self.current_node.position + Vector2(-1, 1)), #Top Left
                               (self.current_node.position + Vector2(1, -1)), #Bot Right
                               (self.current_node.position + Vector2(-1, -1))] #Bot Left
            neighbors = []
            for node in self.grid:
                for pos in valid_positions:
                    if node.position == pos:
                        neighbors.append(node)
            for neighbor in neighbors:
                if (neighbor.traversable and not self.closed_list.__contains__(neighbor)):
                    #Check to see if neighbor is in open list. If not append it and calculate
                    #g, h, and f scores, then set the parent of the neigbor as the current node
                    if not self.open_list.__contains__(neighbor):
                        self.open_list.append(neighbor)
                        neighbor.calculate_g_score(self.current_node)
                        neighbor.calculate_h_score(self.goal_node)
                        neighbor.calculate_f_score()
                        neighbor.set_parent(self.current_node)
                    #If neighbor is already in the open list, it already has a parent, so
                    #recalculate g score to find better path. Recalculate h and f scores
                    #incase path changes
                    elif self.open_list.__contains__(neighbor):
                        neighbor.calculate_g_score(self.current_node)
                        neighbor.calculate_h_score(self.goal_node)
                        neighbor.calculate_f_score()
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
