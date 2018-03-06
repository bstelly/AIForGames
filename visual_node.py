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

    def gen_visual_nodes(self):
        count = 0
        for x in range(0, self.graph.height * self.node_offset, self.node_offset):
            for y in range(0, self.graph.length * self.node_offset, self.node_offset):
                new_node = NodeVisual(self.graph[count], Vector2(x, y), 36, 36,
                                      self.draw_surface)
                self.node_visuals.append(new_node)
                count += 1
