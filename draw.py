#pylint: disable = E1101
#pylint: disable = I1101
import time
import pygame
from draw_utils import Rectangle
from draw_utils import Line
from draw_utils import Text
from vector2 import Vector2
from a_star import AStar
from graph import Graph
from node import Node
from draw_astar_visuals import GraphVisual


def main():
#####Init Function for application class#####
    pygame.init()
    screen_width = 1360
    screen_height = 760
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 0))
    grid = Graph(27, 19)
    start_square = pygame.rect.Rect(1320, 640, 36, 36)
    goal_square = pygame.rect.Rect(1277, 640, 36, 36)
    start_node = Node(None)
    goal_node = Node(None)
    astar = AStar(grid, start_node, goal_node)
    animate_path = []
    drawn_path = []
    iterator = 0
    iterator_two = 1

    dragging_start = False
    dragging_goal = False
    mouse_is_down = False
    pressed_enter = False
    visual_graph = GraphVisual(astar, 40, screen)
########

#Application update
    while True:
        screen.fill((0, 0, 0))
        visual_graph.draw_nodes()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return

        pygame.event.pump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_enter = False
            del astar.closed_list[:]
            del astar.open_list[:]
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
                    for node in visual_graph.node_visual_colliders:
                        if node.collidepoint(event.pos) and mouse_is_down is False:
                            current_state = grid.nodes[count].is_traversable
                            grid.nodes[count].toggle_state()
                            mouse_is_down = True
                        count += 1
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_is_down = False
            if event.button == 1:
                count = 0
                if dragging_start is True or dragging_goal is True:
                    for collider in visual_graph.node_visual_colliders:
                        if start_square.colliderect(collider):
                            start_square.left = visual_graph.node_visual_colliders[count].left
                            start_square.top = visual_graph.node_visual_colliders[count].top
                            dragging_start = False
                            start_node = Node(Vector2(visual_graph.node_visuals[count].node.get_x(),
                                                      visual_graph.node_visuals[count].node.get_y()))
                        if goal_square.colliderect(collider):
                            goal_square.left = visual_graph.node_visual_colliders[count].left
                            goal_square.top = visual_graph.node_visual_colliders[count].top
                            dragging_goal = False
                            goal_node = Node(Vector2(visual_graph.node_visuals[count].node.get_x(),
                                                     visual_graph.node_visuals[count].node.get_y()))
                        count += 1
                    if dragging_start is True:
                        start_square.left = 1320
                        start_square.top = 640
                        dragging_start = False
                    if dragging_goal is True:
                        goal_square.left = 1277
                        goal_square.top = 640
                        dragging_goal = False
                    astar.set_start(start_node)
                    astar.set_goal(goal_node)
        elif event.type == pygame.MOUSEMOTION:
            if dragging_start:
                mouse_x, mouse_y = event.pos
                start_square.x = mouse_x + offset_x
                start_square.y = mouse_y + offset_y
            elif dragging_goal:
                mouse_x, mouse_y = event.pos
                goal_square.x = mouse_x + offset_x
                goal_square.y = mouse_y + offset_y
            elif mouse_is_down:
                count = 0
                for node in visual_graph.node_visual_colliders:
                    if node.collidepoint(event.pos) and grid.nodes[count].is_traversable is current_state:
                        grid.nodes[count].toggle_state()
                    count += 1

        if pygame.key.get_pressed()[pygame.K_c]:
            for x in range(0, grid.length * grid.height):
                if grid.nodes[x].is_traversable is False:
                    grid.nodes[x].toggle_state("wall")
                del astar.closed_list[:]
                del astar.open_list[:]
                pressed_enter = False

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            pressed_enter = True
            astar.set_start(start_node)
            astar.set_goal(goal_node)
            path = astar.find_path()

        if pressed_enter:
            time.sleep(.03)
            count = 0
            count_two = 1
            if iterator_two <= len(path) - 1:
                line_start = Vector2(path[iterator].get_x() * 40, path[iterator].get_y() * 40)
                line_end = Vector2(path[iterator_two].get_x() * 40, path[iterator_two].get_y() * 40)
                animate_path.append(Line(screen, (255, 255, 0), Vector2(line_start.x_pos + 20,
                                                                        line_start.y_pos + 20),
                                         Vector2(line_end.x_pos + 20, line_end.y_pos + 20), 5))
            while count_two <= len(animate_path):
                line_start = Vector2(path[count].get_x() * 40, path[count].get_y() * 40)
                line_end = Vector2(path[count_two].get_x() * 40, path[count_two].get_y() * 40)
                drawn_path.append(Line(screen, (255, 255, 0), Vector2(line_start.x_pos + 20,
                                                                      line_start.y_pos + 20),
                                       Vector2(line_end.x_pos + 20,
                                               line_end.y_pos + 20), 5))
                count += 1
                count_two += 1
            iterator += 1
            iterator_two += 1
        else:
            iterator = 0
            iterator_two = 1
            del animate_path[:]
            del drawn_path[:]

        line_one = Text("Test Font", "calibri", 20, (255, 255, 255), screen, 1090, 10)
        pygame.draw.rect(screen, (0, 230, 0), start_square)
        pygame.draw.rect(screen, (235, 0, 0), goal_square)
        pygame.display.flip()


main()
