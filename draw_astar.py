#pylint: disable = E1101
#pylint: disable = I1101
import time
import pygame
from graph import Graph
from node import Node
from a_star import AStar
from vector2 import Vector2
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

    def update(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.visual_graph.draw_nodes()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return

            pygame.event.pump()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_enter = False
                del self.astar.closed_list[:]
                del self.astar.open_list[:]
                if event.button == 1:
                    if self.start_square.collidepoint(event.pos):
                        dragging_start = True
                        mouse_x, mouse_y = event.pos
                        offset_x = self.start_square.x - mouse_x
                        offset_y = self.start_square.y - mouse_y
                    elif self.goal_square.collidepoint(event.pos):
                        dragging_goal = True
                        mouse_x, mouse_y = event.pos
                        offset_x = self.goal_square.x - mouse_x
                        offset_y = self.goal_square.y - mouse_y
                    else:
                        count = 0
                        for node in self.visual_graph.node_visual_colliders:
                            if node.collidepoint(event.pos) and self.mouse_is_down is False:
                                current_state = self.grid.nodes[count].is_traversable
                                self.grid.nodes[count].toggle_state("wall")
                                mouse_is_down = True
                            count += 1
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_is_down = False
                if event.button == 1:
                    count = 0
                    if dragging_start is True or dragging_goal is True:
                        for collider in self.visual_graph.node_visual_colliders:
                            if self.start_square.colliderect(collider):
                                self.start_square.left = self.visual_graph.node_visual_colliders[count].left
                                self.start_square.top = self.visual_graph.node_visual_colliders[count].top
                                dragging_start = False
                                self.start_node = Node(Vector2(self.visual_graph.node_visuals[count].node.get_x(),
                                                        self.visual_graph.node_visuals[count].node.get_y()))
                            if self.goal_square.colliderect(collider):
                                self.goal_square.left = self.visual_graph.node_visual_colliders[count].left
                                self.goal_square.top = self.visual_graph.node_visual_colliders[count].top
                                dragging_goal = False
                                goal_node = Node(Vector2(self.visual_graph.node_visuals[count].node.get_x(),
                                                        self.visual_graph.node_visuals[count].node.get_y()))
                            count += 1
                        if dragging_start is True:
                            self.start_square.left = 1320
                            self.start_square.top = 640
                            dragging_start = False
                        if dragging_goal is True:
                            self.goal_square.left = 1277
                            self.goal_square.top = 640
                            dragging_goal = False
                        self.astar.set_start(self.start_node)
                        self.astar.set_goal(goal_node)
            elif event.type == pygame.MOUSEMOTION:
                if dragging_start:
                    mouse_x, mouse_y = event.pos
                    self.start_square.x = mouse_x + offset_x
                    self.start_square.y = mouse_y + offset_y
                elif dragging_goal:
                    mouse_x, mouse_y = event.pos
                    self.goal_square.x = mouse_x + offset_x
                    self.goal_square.y = mouse_y + offset_y
                elif mouse_is_down:
                    count = 0
                    for node in self.visual_graph.node_visual_colliders:
                        if node.collidepoint(event.pos) and self.grid.nodes[count].is_traversable is current_state:
                            self.grid.nodes[count].toggle_state("wall")
                        count += 1

            if pygame.key.get_pressed()[pygame.K_c]:
                for x in range(0, self.grid.length * self.grid.height):
                    if self.grid.nodes[x].is_traversable is False:
                        self.grid.nodes[x].toggle_state("wall")
                    del self.astar.closed_list[:]
                    del self.astar.open_list[:]
                    pressed_enter = False

            if pygame.key.get_pressed()[pygame.K_RETURN]:
                pressed_enter = True
                self.astar.set_start(self.start_node)
                self.astar.set_goal(goal_node)
                path = self.astar.find_path()

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
