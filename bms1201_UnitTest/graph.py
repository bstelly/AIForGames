from node import Node
from vector2 import Vector2


class Graph:
    '''Graph Class for storing nodes'''

    #Prototype: def __init__(self, length, height)
    #Arguments: An interger for the length of the graph and an interger for the height of the graph
    #Description: Creates an instance of the Graph class and populates it with nodes
    #Precondition: None
    #Postcondition: An instance of the Graph class is created
    def __init__(self, length, height):
        '''Constructor for Graph class'''
        self.length = length
        self.height = height
        self.nodes = []
        self.create_nodes()

    #Prototype: def create_nodes(self)
    #Arguments: None
    #Description: Creates the nodes in the Graph and assigns then a position
    #Precondition: There must be an instance of the Graph class
    #Postcondition: A graph is created with nodes
    def create_nodes(self):
        '''Fill the Graph with nodes'''
        for i in range(0, self.length):
            for j in range(0, self.height):
                new_node = Node(Vector2(i, j))
                self.nodes.append(new_node)

    #Prototype: def get_neighbors(self, current_node)
    #Arguments: An instance of the node class
    #Description: Finds valid neighbor positions and returns them in a list
    #Precondition: There must be an instance of the Graph class
    #Postcondition: A list of nodes with neighboring postitions is returned
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

    #Prototype: def __getitem__(self, index)
    #Arguments: An interger
    #Description: returns the node in the index that corresponds to the passed in interger
    #Precondition: There must be an instance of the graph class already created
    #Postcondition: A node is returned
    def __getitem__(self, index):
        return self.nodes[index]
