from draw_utils import Rectangle
from vector2 import Vector2

class NodeVisual(object):
    def __init__(self, node, draw_pos, scale_x, scale_y, draw_surface):
        self.node = node
        self.shape = Rectangle(draw_surface, (255, 255, 255), draw_pos,
                               scale_x, scale_y)

class GraphVisual(object):
    def __init__(self, graph, node_offset, draw_surface):
        self.graph = graph
        self.node_offset = node_offset
        self.draw_surface = draw_surface
        self.node_visuals = []
        self.gen_visual_nodes()

    def gen_visual_nodes(self):
        count = 0
        x = 3
        y = 3
        while x <= 1360:
            while y <= 760:
                new_node = NodeVisual(self.graph[count], Vector2(x, y), 36, 36,
                                      self.draw_surface)
                self.graph[count].position = Vector2(x, y)
                self.node_visuals.append(new_node)
                count += 1
                y += self.node_offset
            x += self.node_offset
            y = 3

