#pylint: disable = E1101
import pygame
from draw_utils import Rectangle
from draw_utils import Circle
from draw_utils import Line
from draw_utils import Ellipse
from vector2 import Vector2
from a_star import AStar
from graph import Graph
from node import Node

def main():
    pygame.init()
    screen_width = 1360
    screen_height = 760
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((230, 230, 230))
    position = Vector2(3, 3)
    scale_x = 36
    scale_y = 36
    grid = Graph(34, 19)
    rects = []
    i = 0
    j = 0
    lines_vert = []
    lines_horz = []
    while i <= 1360:
        lines_vert.append(Line(screen, (0, 0, 0), Vector2(i, 0), Vector2(i, 768), 4))
        i += 40
    while j <= 760:
        lines_horz.append(Line(screen, (0, 0, 0), Vector2(0, j), Vector2(1360, j), 4))
        j += 40
        x = 3
        y = 3
        i = 0
    while y <= 760:
        while x <= 1360:
            grid.nodes[i].position = Vector2(x + 17, y + 17)
            x += 40
            i += 1
        y += 40
        x = 3
    
    i = 0
    while i < 646:
        rects.append(Rectangle(screen, (0, 0, 255),
                               (grid.nodes[i].position + Vector2(-17, -17)), scale_x, scale_y))
        i += 1
    

    while True:
        #screen.fill((230, 230, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 and
                position.x_pos >= 0):
            position = position + Vector2(-.005, 0)
        if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and
                position.x_pos <= screen_width - scale_x):
            position = position + Vector2(.005, 0)
        if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 and
                position.y_pos <= screen_height - scale_y):
            position = position + Vector2(0, .005)
        if (pygame.key.get_pressed()[pygame.K_UP] != 0 and
                position.y_pos >= 0):
            position = position + Vector2(0, -.005)

        pygame.display.flip()
main()
