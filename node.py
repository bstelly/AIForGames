#pylint: disable = W0312
#pylint: disable = E1101

class Node:
    '''Node Class'''
    def __init__(self, pos):
        '''Constructor for a Node'''
        self.position = pos
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.traversable = True
        self.is_goal = False
        self.is_start = False

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

    def calculate_h_score(self, other):
        '''Calculates the H-Score for a node'''
        distance = self.position.distance(other.position)
        self.h_score = distance * 10

    def calculate_f_score(self):
        '''Calculates the F-Score for a node'''
        self.f_score = self.g_score + self.h_score

    def set_parent(self, other):
        '''Set the parent of a node to another node'''
        self.parent = other

    def toggle_state(self):
        '''Toggle the is_traversable variable'''
        self.traversable = not self.traversable


    def get_x(self):
        return self.position.x_pos

    def get_y(self):
        return self.position.y_pos
