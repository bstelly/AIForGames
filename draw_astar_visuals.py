import time
from draw_utils import Rectangle
from draw_utils import Line
from vector2 import Vector2
import pygame

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

    def draw_path(self, boolean):
        if not boolean:
            self.animate_iterator = 0
            self.animate_iterator_two = 1
            del self.animated_path[:]
            del self.drawn_path[:]
        if boolean and len(self.astar.path) is not 0:
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









#   (1090, 10)    starting position for text
