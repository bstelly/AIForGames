#pylint: disable = E1101
#pylint: disable = I1101
import pygame
from graph import Graph
from node import Node
from a_star import AStar
from vector2 import Vector2
from draw_astar_visuals import GraphVisual


class Application:
        
    #Prototype: def __init__(self, width, height)
    #Arguments: an int for width and and int for height
    #Description: Creates an instance of the Application class
    #Precondition: None
    #Postcondition: An instance of the Application class is created
    def __init__(self, width, height):
        pygame.init()
        self.grid = Graph(27, 19)
        self.screen = pygame.display.set_mode((width, height))
        self.start_node = Node(None)
        self.goal_node = Node(None)
        self.astar = AStar(self.grid, self.start_node, self.goal_node)
        self.visual_graph = GraphVisual(self.astar, 40, self.screen)

    #Prototype: def update(self)
    #Arguments: None
    #Description: Updates the application by passing in a pygame event to the GraphVisual update
    #Precondition: None
    #Postcondition: The application is updated
    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return
            pygame.event.pump()
            current_event = event
            self.visual_graph.update(current_event)
            pygame.display.flip()
