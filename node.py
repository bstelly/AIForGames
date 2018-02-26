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
        self.is_goal = False
        self.is_start = False

    def calc_g_score(self, other):
        '''Calculates the G-Score for a node'''
        #Check to see if you have a parent already. If so you need to see if the movement
        #cost from the current node to this node is a better option
        if self.position != other.position:
            if self.parent is None:
                if (self.position.x_pos == other.position.x_pos or
                        self.position.y_pos == other.position.y_pos):
                    self.g_score = other.g_score + 10
                else:
                    self.g_score = other.g_score + 14
            elif self.parent is not None:
                tentative_g_score = self.g_score
                if (self.position.x_pos == other.position.x_pos or
                        self.position.y_pos == other.position.y_pos):
                    self.g_score = other.g_score + 10
                else:
                    self.g_score = other.g_score + 14
                if tentative_g_score < self.g_score:
                    self.g_score = tentative_g_score
                    self.set_parent(other.parent)

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

    def toggle_state(self, state):
        '''Toggle the is_traversable variable'''
        if state == "wall":
            self.is_traversable = not self.is_traversable
        if state == "goal":
            self.is_goal = not self.is_goal
        if state == "start":
            self.is_start = not self.is_start
            