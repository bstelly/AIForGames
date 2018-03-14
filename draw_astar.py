#pylint: disable = E1101
#pylint: disable = I1101
import pygame
from graph import Graph
from node import Node
from a_star import AStar
from draw_astar_visuals import GraphVisual



class Application:
    def __init__(self, width, height):
        pygame.init()
        self.grid = Graph(27, 19)
        self.screen = pygame.display.set_mode((width, height))
        self.start_node = Node(None)
        self.goal_node = Node(None)
        self.astar = AStar(self.graph, self.start_node, self.goal_node)
        self.start_square = pygame.rect.Rect(1320, 640, 36, 36)
        self.goal_square = pygame.rect.Rect(1277, 640, 36, 36)
        self.visual_graph = GraphVisual(self.astar, 40, self.screen)
        self.dragging_start = False
        self.dragging_goal = False
        self.mouse_is_down = False
        self.pressed_enter = False


