#pylint: disable = W0312
#pylint: disable = E1101
from vector2 import Vector2

class Node:
    '''Node Class'''
    def __init__(self):
        self.position = Vector2
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = Node

    def calc_g_score(self, other):
        '''Calculates the G-Score for a node'''
        

class Graph:
    def __init__(self, length, height):
        self.length = length
        self.height = height
