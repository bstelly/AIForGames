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
        self.is_transversable = True

    def calc_g_score(self, other):
        '''Calculates the G-Score for a node'''
        if (self.position.x_pos is other.position.x_pos or
                self.position.y_pos is other.position.y_pos):
            self.g_score = other.g_score + 10
        else:
            self.g_score = other.g_score + 14

    def calc_h_score(self, other):
        '''Calculates the H-Score for a node'''
        distance_x = other.position.x_pos - self.position.x_pos
        distance_y = other.position.y_pos - self.position.y_pos
        total = distance_x + distance_y
        self.h_score = total * 10

    def calc_f_score(self):
        '''Calculates the F-Score for a node'''
        self.f_score = self.g_score + self.h_score

    def set_parent(self, other):
        '''Set the parent of a node to another node'''
        self.parent = other

    def set_traversable_off(self):
        '''Set the is_traversable value to off'''
        self.is_transversable = False
