#pylint: disable = E1101
import pygame
from draw_utils import Rectangle
from draw_utils import Circle
from draw_utils import Line
from vector2 import Vector2
from a_star import AStar
from graph import Graph
from node import Node

def main():
    pygame.init()
    screen_width = 1360
    screen_height = 760
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 0))
    scale_x = 36
    scale_y = 36
    grid = Graph(34, 19)
    rects = []

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
        rects.append(Rectangle(screen, (230, 230, 230),
                               (grid.nodes[i].position + Vector2(-17, -17)), scale_x, scale_y))
        i += 1


    while True:
        #screen.fill((230, 230, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()

        pygame.display.flip()
main()
