import pygame
import time
from node import Node
from draw_utils import Rectangle
from draw_utils import Line
from vector2 import Vector2
class NodeVisual(object):
    def __init__(self, node, color, draw_pos, scale_x, scale_y, draw_surface):
        self.node = node
        self.shape = Rectangle(draw_surface, color, draw_pos,
                               scale_x, scale_y)

class GraphVisual(object):
    def __init__(self, astar, node_offset, draw_surface):
        self.astar = astar
        self.node_offset = node_offset
        self.draw_surface = draw_surface
        self.node_visuals = []
        self.node_visual_colliders = []
        self.gen_visual_nodes()

        self.animated_path = []
        self.drawn_path = []
        self.animate_iterator = 0
        self.animate_iterator_two = 1
        self.draw_counter = 0
        self.draw_counter_two = 1

        self.dragging_start = False
        self.dragging_goal = False
        self.mouse_is_down = False
        self.pressed_enter = False
        self.current_state = False
        self.offset_x = 0
        self.offset_y = 0

        self.start_square = pygame.rect.Rect(1320, 640, 36, 36)
        self.goal_square = pygame.rect.Rect(1277, 640, 36, 36)

    def gen_visual_nodes(self):
        count = 0
        x = 3
        y = 3
        while x <= 1080:
            while y <= 760:
                if self.astar.grid[count].is_traversable is True:
                    new_node = NodeVisual(self.astar.grid[count], (215, 215, 215),
                                          (Vector2(x, y)), 36, 36, self.draw_surface)
                self.node_visuals.append(new_node)
                self.node_visual_colliders.append(pygame.rect.Rect(x, y, 36, 36))
                count += 1
                y += self.node_offset
            x += self.node_offset
            y = 3

    def draw_nodes(self):
        for node in self.node_visuals:
            if not node.node.is_traversable:
                node.shape.color = (0, 0, 0)
            elif self.astar.open_list.__contains__(node.node):
                node.shape.color = (0, 255, 255)
            elif self.astar.closed_list.__contains__(node.node):
                node.shape.color = (0, 0, 220)
            else:
                node.shape.color = (50, 50, 50)

            node.shape.draw()
        pygame.draw.rect(self.draw_surface, (0, 230, 0), self.start_square)
        pygame.draw.rect(self.draw_surface, (235, 0, 0), self.goal_square)

    def draw_path(self):
        if not self.pressed_enter:
            self.animate_iterator = 0
            self.animate_iterator_two = 1
            del self.animated_path[:]
            del self.drawn_path[:]
        if self.pressed_enter and len(self.astar.path) is not 0:
            time.sleep(.03)
            count = 0
            count_two = 1
            if self.animate_iterator_two <= len(self.astar.path) - 1:
                line_start = Vector2(self.astar.path[self.animate_iterator].get_x() * 40,
                                     self.astar.path[self.animate_iterator].get_y() * 40)
                line_end = Vector2(self.astar.path[self.animate_iterator_two].get_x() * 40,
                                   self.astar.path[self.animate_iterator_two].get_y() * 40)
                self.animated_path.append(Line(self.draw_surface, (255, 255, 0),
                                               Vector2(line_start.x_pos + 20,
                                                       line_start.y_pos + 20),
                                               Vector2(line_end.x_pos + 20,
                                                       line_end.y_pos + 20), 5))
            while count_two <= len(self.animated_path):
                line_start = Vector2(self.astar.path[count].get_x() * 40,
                                     self.astar.path[count].get_y() * 40)
                line_end = Vector2(self.astar.path[count_two].get_x() * 40,
                                   self.astar.path[count_two].get_y() * 40)
                self.drawn_path.append(Line(self.draw_surface, (255, 255, 0),
                                            Vector2(line_start.x_pos + 20, line_start.y_pos + 20),
                                            Vector2(line_end.x_pos + 20,
                                                    line_end.y_pos + 20), 5))
                count += 1
                count_two += 1
            self.animate_iterator += 1
            self.animate_iterator_two += 1


    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pressed_enter = False
            self.astar.reset()
            if self.start_square.collidepoint(event.pos):
                self.dragging_start = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.start_square.x - mouse_x
                self.offset_y = self.start_square.y - mouse_y
            elif self.goal_square.collidepoint(event.pos):
                self.dragging_goal = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.goal_square.x - mouse_x
                self.offset_y = self.goal_square.y - mouse_y
            else:
                count = 0
                for node in self.node_visual_colliders:
                    if node.collidepoint(event.pos) and self.mouse_is_down is False:
                        self.current_state = self.astar.grid.nodes[count].is_traversable
                        self.astar.grid.nodes[count].toggle_state()
                        self.mouse_is_down = True
                    count += 1
        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_is_down = False
            count = 0
            for collider in self.node_visual_colliders:
                if self.start_square.colliderect(collider):
                    self.start_square.left = self.node_visual_colliders[count].left
                    self.start_square.top = self.node_visual_colliders[count].top
                    self.dragging_start = False
                    self.astar.start_node = Node(Vector2(self.node_visuals[count].node.get_x(),
                                            self.node_visuals[count].node.get_y()))
                if self.goal_square.colliderect(collider):
                    self.goal_square.left = self.node_visual_colliders[count].left
                    self.goal_square.top = self.node_visual_colliders[count].top
                    self.dragging_goal = False
                    self.astar.goal_node = Node(Vector2(self.node_visuals[count].node.get_x(),
                                            self.node_visuals[count].node.get_y()))
                count += 1
            if self.dragging_start is True:
                self.start_square.left = 1320
                self.start_square.top = 640
                self.dragging_start = False
            if self.dragging_goal is True:
                self.goal_square.left = 1277
                self.goal_square.top = 640
                self.dragging_goal = False
            self.astar.set_start(self.astar.start_node)
            self.astar.set_goal(self.astar.goal_node)
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_start:
                mouse_x, mouse_y = event.pos
                self.start_square.x = mouse_x + self.offset_x
                self.start_square.y = mouse_y + self.offset_y
            elif self.dragging_goal:
                mouse_x, mouse_y = event.pos
                self.goal_square.x = mouse_x + self.offset_x
                self.goal_square.y = mouse_y + self.offset_y
            elif self.mouse_is_down:
                count = 0
                for node in self.node_visual_colliders:
                    if node.collidepoint(event.pos) and self.astar.grid.nodes[count].is_traversable is self.current_state:
                        self.astar.grid.nodes[count].toggle_state()
                    count += 1
        if pygame.key.get_pressed()[pygame.K_c]:
            self.clear_grid()
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            self.pressed_enter = True
            self.astar.update(self.astar.start_node, self.astar.goal_node)

    def clear_grid(self):
        for x in range(0, self.astar.grid.length * self.astar.grid.height):
            if self.astar.grid.nodes[x].is_traversable is False:
                self.astar.grid.nodes[x].toggle_state()
        self.astar.reset()
        self.pressed_enter = False


#   line_one = Text("Test Font", "calibri", 20, (255, 255, 255), screen, 1090, 10)
