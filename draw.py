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
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 80))
    position = Vector2(10, 10)
    scale_x = 1
    scale_y = 1
    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 and
                position.x_pos >= 0):
            position = position + Vector2(-1, 0)
        if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and
                position.x_pos <= screen_width - scale_x):
            position = position + Vector2(1, 0)
        if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 and
                position.y_pos <= screen_height - scale_y):
            position = position + Vector2(0, 1)
        if (pygame.key.get_pressed()[pygame.K_UP] != 0 and
                position.y_pos >= 0):
            position = position + Vector2(0, -1)
        rect = Rectangle(screen, (0, 0, 0), position, scale_x, scale_y)
        i = 0
        lines_vert = []
        lines_horz = []
        while i <= 1360:
            lines.append(Line(screen, (0, 0, 0), Vector2(i, 0), Vector2(i, 768), 4))
            i += 

        pygame.display.flip()
main()
