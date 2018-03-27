#pylint: disable = W0312
#pylint: disable = E1101

class Node:
    '''Node Class'''

    #Prototype: def __init__(self, pos)
    #Arguments: A Vector2
    #Description: The initializer for creating an instance of the Node Class
    #Precondition: None
    #Postcondition: An instance of the Node class is created
    def __init__(self, Vector2):
        '''Constructor for a Node'''
        self.position = Vector2
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.traversable = True
        self.is_goal = False
        self.is_start = False

    #Prototype: def calculate_g_score(self, other)
    #Arguments: An instance of the Node class
    #Description: Calculates the G-Score for a node
    #Precondition: There must be two instances of the Node class
    #Postcondition: The g_score for the node is calculated
    def calculate_g_score(self, other):
        '''Calculates the G-Score for a node'''
        #Find the g-Score for a neighbor that has just been discovered
        if self.parent is None:
            if (self.position.x_pos == other.position.x_pos or
                    self.position.y_pos == other.position.y_pos):
                self.g_score = other.g_score + 10
            else:
                self.g_score = other.g_score + 14
        #If node has already been discovered, it should already have a parent
        #Check to see if path to current node is faster by using a tentative g-score
        elif self.parent is not None:
            tentative_g_score = self.g_score
            if (self.position.x_pos == other.position.x_pos or
                    self.position.y_pos == other.position.y_pos):
                tentative_g_score = other.g_score + 10
            else:
                tentative_g_score = other.g_score + 14
            if tentative_g_score < self.g_score:
                self.g_score = tentative_g_score
                self.set_parent(other.parent)
            else:
                self.g_score = self.g_score

    #Prototype: def calculate_h_score(self, other)
    #Arguments: An instance of the Node class
    #Description: Calculates the H-Score for a node
    #Precondition: There must be two instances of the Node class
    #Postcondition: The nodes H-Score is calculated
    def calculate_h_score(self, other):
        '''Calculates the H-Score for a node'''
        distance = self.position.distance(other.position)
        self.h_score = distance * 10

    #Prototype: def calculate_f_score(self)
    #Arguments: None
    #Description: Calculates the F-Score for a node
    #Precondition: There must be an instance of the Node class
    #Postcondition: The nodes F-Score is calculated
    def calculate_f_score(self):
        '''Calculates the F-Score for a node'''
        self.f_score = self.g_score + self.h_score

    #Prototype: def set_parent(self, other)
    #Arguments: An instance of the node class
    #Description: Sets the parent of a node to the node that is passed in
    #Precondition: There must be two instances of the Node class
    #Postcondition: The node's parent is set to the node passed in
    def set_parent(self, other):
        '''Set the parent of a node to another node'''
        self.parent = other

    #Prototype: def toggle_state(self)
    #Arguments: None
    #Description: toggles the traversable state of a node
    #Precondition: There must be an instance of the Node class
    #Postcondition: The nodes traversability is assigned the opposite of its current state
    def toggle_state(self):
        '''Toggle the is_traversable variable'''
        self.traversable = not self.traversable


    #Prototype: def get_x(self)
    #Arguments: None
    #Description: returns the node position's x-value
    #Precondition: There must be an instance of the Node class
    #Postcondition: The x-value is returned
    def get_x(self):
        '''Returns a node's x-position'''
        return self.position.x_pos

    #Prototype: def get_y(self)
    #Arguments: None
    #Description: returns the node position's y-value
    #Precondition: There must be an instance of the Node class
    #Postcondition: The y-value is returned
    def get_y(self):
        '''Returns a node's y-position'''
        return self.position.y_pos
