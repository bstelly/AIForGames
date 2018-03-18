import time
from draw_utils import Rectangle
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


    def gen_visual_nodes(self):
        count = 0
        x = 3
        y = 3
        while x <= 1080:
            while y <= 760:
                if self.astar.grid[count].is_traversable is True:
                    new_node = NodeVisual(self.astar.grid[count], (215, 215, 215), (Vector2(x, y)), 36, 36,
                                          self.draw_surface)
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

    def draw_path(self, bool):
        
