from operator import attrgetter
from graph import Graph
from vector2 import Vector2
from node import Node

class AStar:

    #Prototype: def __init__(self, graph, start, end)
    #Arguments: An instance of the graph class and two Node objects for the start and goal
    #Description: Creates an instance of the AStar class
    #Precondition: There must be an instance of the Graph class and two instances of the Node class
    #Postcondition: An instance of the AStar class is created
    def __init__(self, graph, start, goal):
        '''Constructor for AStar class'''

        self.grid = graph
        self.open_list = []
        self.closed_list = []
        self.start_node = start
        self.goal_node = goal
        self.current_node = start
        self.open_list.append(start)
        self.path = []
#        self.visual_neighbors = []

    #Prototype: def set_start(self, start_node)
    #Arguments: A Node object
    #Description: Sets the start node of the graph to the node passed in
    #Precondition: There must be an instance of the AStar class and a node object
    #Postcondition: The AStar instance is given a new starting node
    def set_start(self, start_node):
        self.start_node = start_node
        self.current_node = start_node
        self.open_list.append(start_node)

    #Prototype: def set_goal(self, goal_node)
    #Arguments: A Node object
    #Description: Sets the goal ode of the graph to the node passed in
    #Precondition: There must be an instance of the AStar class and a node object
    #Postcondition: The AStar instance is given a new goal node
    def set_goal(self, goal_node):
        self.goal_node = goal_node

    #Prototype: def find_current(self)
    #Arguments: None
    #Description: Finds the current node in the path
    #Precondition: There must be an instance of the AStar class
    #Postcondition: The current node is set and moved to the closed list and out of the open list
    def find_current(self):
        '''Function to find the current node in the path'''
        #Find current node, add current node to closed list and remove it from open list
        self.current_node = min(self.open_list, key=attrgetter('f_score'))
        self.closed_list.append(self.current_node)
        self.open_list.remove(self.current_node)

    #Prototype: def find_path(self)
    #Arguments: None
    #Description: Generates a path from start to goal node
    #Precondition: The closed list has to contain the goal node
    #Postcondition: A list of nodes is returned in order from start to goal node
    def find_path(self):
        '''Function to generate a path from start to goal node'''
        self.reset()
        self.open_list.append(self.start_node)
        while not self.closed_list.__contains__(self.goal_node) and self.open_list:
            self.find_current()
            neighbors = self.grid.get_neighbors(self.current_node)
#            self.visual_neighbors.append((neighbors[:]))
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
        if self.closed_list.__contains__(self.goal_node):
            self.start_node.g_score = 0
            path = []
            while self.current_node.parent:
                path.append(self.current_node)
                self.current_node = self.current_node.parent
            path.append(self.current_node)
            self.path = path
            path.reverse()
            return path

    #Prototype: def reset(self)
    #Arguments: None
    #Description: Resets the AStar algorithm for multiple runs
    #Precondition: There must be an instance of the AStar algorithm
    #Postcondition: The AStar instance has and empty open list, closed list, and path. All node
    #               parents are set to none
    def reset(self):
        '''Delete open list, closed list, path, and set all node
        parents to None for running AStar more than once'''
        del self.open_list[:]
        del self.closed_list[:]
        del self.path[:]
        for node in self.grid.nodes:
            node.parent = None

    #Prototype: def update(self, start_node, goal_node)
    #Arguments: A Node object for the starting node and a Node object for the goal node
    #Description: Updates the start and goal node and runs the AStar algorithm
    #Precondition: There must be an instance of the Astar algorithm and two Node objects
    #Postcondition: The instance of Astar is updated with a path
    def update(self, start_node, goal_node):
        self.set_start(start_node)
        self.set_goal(goal_node)
        self.find_path()
