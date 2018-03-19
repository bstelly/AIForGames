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
        self.astar = AStar(self.grid, self.start_node, self.goal_node)
        self.start_square = pygame.rect.Rect(1320, 640, 36, 36)
        self.goal_square = pygame.rect.Rect(1277, 640, 36, 36)
        self.visual_graph = GraphVisual(self.astar, 40, self.screen)
        self.path = []
        self.dragging_start = False
        self.dragging_goal = False
        self.mouse_is_down = False
        self.pressed_enter = False

    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    return
            pygame.event.pump()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed_enter = False
                del self.astar.closed_list[:]
                del self.astar.open_list[:]
                if event.button == 1:
                    if self.start_square.collidepoint(event.pos):
                        self.dragging_start = True
                        mouse_x, mouse_y = event.pos
                        offset_x = self.start_square.x - mouse_x
                        offset_y = self.start_square.y - mouse_y
                    elif self.goal_square.collidepoint(event.pos):
                        self.dragging_goal = True
                        mouse_x, mouse_y = event.pos
                        offset_x = self.goal_square.x - mouse_x
                        offset_y = self.goal_square.y - mouse_y
                    else:
                        count = 0
                        for node in self.visual_graph.node_visual_colliders:
                            if node.collidepoint(event.pos) and self.mouse_is_down is False:
                                current_state = self.grid.nodes[count].is_traversable
                                self.grid.nodes[count].toggle_state("wall")
                                self.mouse_is_down = True
                            count += 1
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_is_down = False
                if event.button == 1:
                    count = 0
                    if self.dragging_start is True or self.dragging_goal is True:
                        for collider in self.visual_graph.node_visual_colliders:
                            if self.start_square.colliderect(collider):
                                self.start_square.left = self.visual_graph.node_visual_colliders[count].left
                                self.start_square.top = self.visual_graph.node_visual_colliders[count].top
                                self.dragging_start = False
                                self.start_node = Node(Vector2(self.visual_graph.node_visuals[count].node.get_x(),
                                                        self.visual_graph.node_visuals[count].node.get_y()))
                            if self.goal_square.colliderect(collider):
                                self.goal_square.left = self.visual_graph.node_visual_colliders[count].left
                                self.goal_square.top = self.visual_graph.node_visual_colliders[count].top
                                self.dragging_goal = False
                                self.goal_node = Node(Vector2(self.visual_graph.node_visuals[count].node.get_x(),
                                                        self.visual_graph.node_visuals[count].node.get_y()))
                            count += 1
                        if self.dragging_start is True:
                            self.start_square.left = 1320
                            self.start_square.top = 640
                            self.dragging_start = False
                        if self.dragging_goal is True:
                            self.goal_square.left = 1277
                            self.goal_square.top = 640
                            self.dragging_goal = False
                        self.astar.set_start(self.start_node)
                        self.astar.set_goal(self.goal_node)
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging_start:
                    mouse_x, mouse_y = event.pos
                    self.start_square.x = mouse_x + offset_x
                    self.start_square.y = mouse_y + offset_y
                elif self.dragging_goal:
                    mouse_x, mouse_y = event.pos
                    self.goal_square.x = mouse_x + offset_x
                    self.goal_square.y = mouse_y + offset_y
                elif self.mouse_is_down:
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
                    self.pressed_enter = False
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.pressed_enter = True
                self.astar.set_start(self.start_node)
                self.astar.set_goal(self.goal_node)
                self.path = self.astar.find_path()
            self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.visual_graph.draw_nodes()
        self.visual_graph.draw_path(self.pressed_enter, self.path)
        pygame.draw.rect(self.screen, (0, 230, 0), self.start_square)
        pygame.draw.rect(self.screen, (235, 0, 0), self.goal_square)
        pygame.display.flip()


astar_application = Application(1360, 760)
astar_application.update()