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
        self.is_traversable = True

    def calc_g_score(self, other):
        '''Calculates the G-Score for a node'''
        #Check to see if you have a parent already. If so you need to see if the movement
        #cost from the current node to this node is a better option
        if self.position != other.position:
            if (self.position.x_pos == other.position.x_pos or
                    self.position.y_pos == other.position.y_pos):
                self.g_score = other.g_score + 10
            else:
                self.g_score = other.g_score + 14

    def calc_h_score(self, other):
        '''Calculates the H-Score for a node'''
        distance = self.position.distance(other.position)
        total = distance.x_pos + distance.y_pos
        self.h_score = total * 10

    def calc_f_score(self):
        '''Calculates the F-Score for a node'''
        self.f_score = self.g_score + self.h_score

    def set_parent(self, other):
        '''Set the parent of a node to another node'''
        self.parent = other

    def toggle_traversable(self):
        '''Toggle the is_traversable variable'''
        self.is_traversable = not self.is_traversable
