#pylint: disable = E1101
import pygame
from draw_utils import Rectangle
from draw_utils import Circle
from draw_utils import Line
from vector2 import Vector2
from a_star import AStar
from graph import Graph
from node import Node
from visual_node import GraphVisual

def main():
#Vector2(-17, -17)      For center of square
    pygame.init()
    screen_width = 1360
    screen_height = 760
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 0))
    grid = Graph(34, 19)
    visual_graph = GraphVisual(grid, 40, screen)
    start_square = Rectangle(screen, (0, 255, 0), grid.nodes[0].position, 36, 36)
    rectangle = pygame.rect.Rect(start_square.position + Vector2(-17, 0),
                                 (start_square.position + Vector2(0, 17)), 36, 36)
    dragging = False


    while True:
        #screen.fill((230, 230, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.buton == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
            
#    if (pygame.mouse.get_pressed() != 0 and
#                m_position.x_pos >= 0):
        pygame.display.flip()



main()
