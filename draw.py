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
#Vector2(17, 17)      For center of square
    pygame.init()
    screen_width = 1360
    screen_height = 760
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 0))
    grid = Graph(34, 19)
    walls = []
    visual_graph = GraphVisual(grid, 40, screen)

    start_square = pygame.rect.Rect(3, 363, 36, 36)
    goal_square = pygame.rect.Rect(1323, 363, 36, 36)

    node_squares = []
    for node in grid.nodes:
        left = node.get_x()
        top = node.get_y()
        node_squares.append(pygame.rect.Rect(left, top, 36, 36))
    dragging_start = False
    dragging_goal = False
    mouse_is_down = False
    while True:
        screen.fill((0, 0, 0))
        visual_graph = GraphVisual(grid, 40, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if start_square.collidepoint(event.pos):
                    dragging_start = True
                    mouse_x, mouse_y = event.pos
                    offset_x = start_square.x - mouse_x
                    offset_y = start_square.y - mouse_y
                elif goal_square.collidepoint(event.pos):
                    dragging_goal = True
                    mouse_x, mouse_y = event.pos
                    offset_x = goal_square.x - mouse_x
                    offset_y = goal_square.y - mouse_y
                else:
                    count = 0
                    for node in node_squares:
                        if node.collidepoint(event.pos) and mouse_is_down is False:
                            grid.nodes[count].toggle_state("wall")
                            mouse_is_down = True
                        count += 1

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_is_down = False
            if event.button == 1:
                count = 0
                if dragging_start is True or dragging_goal is True:
                    for node in node_squares:
                        if start_square.colliderect(node):
                            start_square.left = grid.nodes[count].get_x()
                            start_square.top = grid.nodes[count].get_y()
                            dragging_start = False
                        if goal_square.colliderect(node):
                            goal_square.left = grid.nodes[count].get_x()
                            goal_square.top = grid.nodes[count].get_y()
                            dragging_goal = False
                        count += 1
        elif event.type == pygame.MOUSEMOTION:
            if dragging_start:
                mouse_x, mouse_y = event.pos
                start_square.x = mouse_x + offset_x
                start_square.y = mouse_y + offset_y
            elif dragging_goal:
                mouse_x, mouse_y = event.pos
                goal_square.x = mouse_x + offset_x
                goal_square.y = mouse_y + offset_y

        pygame.draw.rect(screen, (0, 255, 0), start_square)
        pygame.draw.rect(screen, (255, 0, 0), goal_square)
        count = 0
        for node in grid.nodes:
            if node.is_traversable is False:
                pygame.draw.rect(screen, (0, 0, 0), node_squares[count])
            count += 1
        pygame.display.flip()



main()
