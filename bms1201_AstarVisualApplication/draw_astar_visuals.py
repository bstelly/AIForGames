import pygame
import time
from node import Node
from draw_utils import Rectangle
from draw_utils import Line
from draw_utils import Text
from vector2 import Vector2

class NodeVisual(object):

    #Prototype: def __init__(self, node, color, draw_pos, scale_x, scale_y, draw_surface)
    #Arguments: a Node object, a color, a Vector2, an int for length, an int for height,
    #           and a draw surface
    #Description: Creates an instance of the NodeVisual class and displays a rectangle
    #Precondition: None
    #Postcondition: An instance of the NodeVisual class is created
    def __init__(self, node, color, draw_pos, scale_x, scale_y, draw_surface):
        self.node = node
        self.shape = Rectangle(draw_surface, color, draw_pos,
                               scale_x, scale_y)

class GraphVisual(object):

    #Prototype: def __init__(self, astar, node_offset, draw_surface)
    #Arguments: an instance of astar, an int for node offset, and a draw surface
    #Description: Creates an instance of the GraphVisual class
    #Precondition: There must be an instance of AStar already created and a draw surface created
    #              using pygame
    #Postcondition: An instance of the GraphVisual class is created
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
        self.closed_list_drawn = 0
        self.closed_list_animated = 0
        self.closed_list_nodes = []
#        self.open_list_nodes =[]
        self.parents = []

        self.dragging_start = False
        self.dragging_goal = False
        self.mouse_is_down = False
        self.pressed_enter = False
        self.current_state = False
        self.closed_list_done = False
        self.toggle_shift = False
        self.toggle_ctrl = False
        self.path_done = True

        self.offset_x = 0
        self.offset_y = 0

        self.start_square = pygame.rect.Rect(1320, 640, 36, 36)
        self.goal_square = pygame.rect.Rect(1277, 640, 36, 36)
        self.draw_text()

    #Prototype: def gen_visual_nodes(self)
    #Arguments: None
    #Description: Generates the visual nodes and gives them colliders
    #Precondition: There must be an instance of GraphVisual
    #Postcondition: An instance of GraphVisual has a grid of visual nodes
    def gen_visual_nodes(self):
        count = 0
        x = 3
        y = 3
        while x <= 1080:
            while y <= 760:
                if self.astar.grid[count].traversable is True:
                    new_node = NodeVisual(self.astar.grid[count], (215, 215, 215),
                                          (Vector2(x, y)), 36, 36, self.draw_surface)
                self.node_visuals.append(new_node)
                self.node_visual_colliders.append(pygame.rect.Rect(x, y, 36, 36))
                count += 1
                y += self.node_offset
            x += self.node_offset
            y = 3

    #Prototype: def draw_nodes(self)
    #Arguments: None
    #Description: Draws the visual nodes every frame
    #Precondition: There must be an instance of GraphVisual
    #Postcondition: The screen displays the visual nodes
    def draw_nodes(self):
        if self.closed_list_done and self.path_done:
            for node in self.node_visuals:
                if not node.node.traversable:
                    node.shape.color = (0, 0, 0)
                else:
                    if not self.astar.closed_list.__contains__(node.node):
                        node.shape.color = (50, 50, 50)
                if self.closed_list_done is True:
                    if self.astar.open_list.__contains__(node.node):
                        node.shape.color = (0, 0, 75)
                node.shape.draw()
        self.sort_visual_nodes_in_closed_list()


    #Prototype: def draw_path(self)
    #Arguments: None
    #Description: Draws the path returned from AStar using the visual nodes
    #Precondition: There must be an instance of GraphVisual and an instance of Astar
    #              must retun a path
    #Postcondition: The screen now displays a line that travels from start to goal
    def draw_path(self):
        if not self.pressed_enter:
            self.animate_iterator = 0
            self.animate_iterator_two = 1
            del self.animated_path[:]
            del self.drawn_path[:]
        if self.pressed_enter and len(self.astar.path) is not 0:
            time.sleep(.01)
            count = 0
            count_two = 1
            if self.animate_iterator_two <= len(self.astar.path) - 1:
                line_start = Vector2(self.astar.path[self.animate_iterator].get_x() * 40,
                                     self.astar.path[self.animate_iterator].get_y() * 40)
                line_end = Vector2(self.astar.path[self.animate_iterator_two].get_x() * 40,
                                   self.astar.path[self.animate_iterator_two].get_y() * 40)
                self.animated_path.append(Line(self.draw_surface, (255, 240, 0),
                                               Vector2(line_start.x_pos + 20,
                                                       line_start.y_pos + 20),
                                               Vector2(line_end.x_pos + 20,
                                                       line_end.y_pos + 20), 11))
            while count_two <= len(self.animated_path):
                line_start = Vector2(self.astar.path[count].get_x() * 40,
                                     self.astar.path[count].get_y() * 40)
                line_end = Vector2(self.astar.path[count_two].get_x() * 40,
                                   self.astar.path[count_two].get_y() * 40)
                self.drawn_path.append(Line(self.draw_surface, (255, 240, 0),
                                            Vector2(line_start.x_pos + 20, line_start.y_pos + 20),
                                            Vector2(line_end.x_pos + 20,
                                                    line_end.y_pos + 20), 11))
                if len(self.animated_path) == len(self.astar.path) - 1:
                    self.path_done = True
                count += 1
                count_two += 1
            self.animate_iterator += 1
            self.animate_iterator_two += 1

    #Prototype: def draw_text(self)
    #Arguments: None
    #Description: Draws text to the screen
    #Precondition: There must be an instance of GraphVisual
    #Postcondition: Text is displayed to the screen
    def draw_text(self):
    #LEFT SIDE (1090)
        line_one = Text("A* Algorithm", "arial black", 37, (255, 255, 255), self.draw_surface, 1090, 10)


    #Prototype: def clear_grid(self)
    #Arguments: None Clears the grid by resetting astar, and setting traversability of all
    #           nodes to True
    #Description: Clears the grid by resetting astar, and setting traversability of all
    #             nodes to True
    #Precondition: There must be an instance of GraphVisual
    #Postcondition: The grid is reset to a default state
    def clear_grid(self):
        for x in range(0, self.astar.grid.length * self.astar.grid.height):
            if self.astar.grid.nodes[x].traversable is False:
                self.astar.grid.nodes[x].toggle_state()
        self.astar.reset()
        self.pressed_enter = False
        self.pressed_shift = False
        del self.parents[:]

    #Prototype: def clear_screen(self)
    #Arguments: None
    #Description: Wipes the screen to the background color and redraws text
    #Precondition: There must be a draw surface created using pygame
    #Postcondition: The screen is wiped to the background color
    def clear_screen(self):
        self.draw_surface.fill((0, 0, 0))
        self.draw_text()

    #Prototype: def sort_visual_nodes_in_closed_list(self)
    #Arguments: None
    #Description: Sorts closed list nodes for GraphVisual in the same order as the astar closed
    #             list
    #Precondition: There must be an instance of GraphVisual
    #Postcondition: The close_list_nodes are sorted in the same order as the astar closed list
    def sort_visual_nodes_in_closed_list(self):
        if self.astar.closed_list:
            done = False
            count = 0
            while not done:
                for node in self.node_visuals:
                    if count < len(self.astar.closed_list):
                        if node.node.position == self.astar.closed_list[count].position:
                            self.closed_list_nodes.append(node)
                            count += 1
                    else:
                        done = True
#            done = False
#            count = 0
#            new_list = map(len, self.astar.visual_neighbors)
#            total_neighbors = 0
#            x = 0
#            while x < len(self.astar.visual_neighbors):
#                total_neighbors += new_list[x] + new_list[x + 1]
#                x += 2
#            while not done:
#                for node in self.node_visuals:
#                    if count < len(map(len, self.astar.visual_neighbors)):
#                        if node.node.position == self.astar.visual_neighbors[count].position:
#                            self.open_list_nodes.append(node)
#                           count += 1
#                   else:
#                        done = True


    #Prototype: def draw_closed_list(self)
    #Arguments: None
    #Description: Draws an animated closed list to the screen
    #Precondition: There must be an instance of GraphVisual with A* algorithm finished running
    #Postcondition: The closed list is drawn to the screen
    def draw_closed_list(self):
        if (self.astar.closed_list and self.closed_list_animated < len(self.astar.closed_list)
                and self.closed_list_nodes):
            self.closed_list_drawn = 0
            self.closed_list_nodes[self.closed_list_animated].shape.color = (0, 0, 180)
            self.closed_list_nodes[self.closed_list_animated].shape.draw()
            self.closed_list_animated += 1

            while self.closed_list_drawn < self.closed_list_animated:
                self.closed_list_nodes[self.closed_list_drawn].shape.draw()
                self.closed_list_drawn += 1
        else:
            self.closed_list_done = True
            del self.closed_list_nodes[:]

    #Prototype: def draw_parents(self)
    #Arguments: None
    #Description: Draws the parents for every node in the open or closed list
    #Precondition: There must be an instance of GraphVisual with A* algorithm finished running
    #Postcondition: The screen has lines drawn from each node to its parent
    def draw_parents(self):
        for node in self.node_visuals:
            if (self.astar.open_list.__contains__(node.node) or
                    self.astar.closed_list.__contains__(node.node)):
                new_line = Line(self.draw_surface, (255, 100, 0),
                                Vector2(node.shape.position.x_pos + 17,
                                        node.shape.position.y_pos + 17),
                                Vector2(node.node.parent.get_x() * 40 + 20,
                                        node.node.parent.get_y() * 40 + 20), 3)

                self.parents.append(new_line)
        if self.parents:
            for line in self.parents:
                line.draw()

    #Prototype: def draw_node_information(self)
    #Arguments: None
    #Description: Displays the G, H, and F score of every node by drawing them using text on every
    #             visual node in the closed or open list
    #Precondition: There must be an instance of GraphVisual with A* finished running
    #Postcondition: Every visual node in the closed or open list now displays its own F, G, and H
    #               score
    def draw_node_information(self):
        color = (0, 150, 0)
        font = "impact"
        for node in self.node_visuals:
            if (self.astar.closed_list.__contains__(node.node) or
                    self.astar.open_list.__contains__(node.node)):
                gscore_text = Text("G = " + str(node.node.g_score), font, 11, color,
                                   self.draw_surface, node.shape.position.x_pos + 1,
                                   node.shape.position.y_pos - 1)
                hscore_text = Text("H = " + str(node.node.h_score), font, 11, color,
                                   self.draw_surface, node.shape.position.x_pos + 1,
                                   node.shape.position.y_pos + 10)
                fscore_text = Text("F = " + str(node.node.f_score), font, 11, color,
                                   self.draw_surface, node.shape.position.x_pos + 1,
                                   node.shape.position.y_pos + 21)


    #Prototype: def update(self, event)
    #Arguments: Pygame Event
    #Description: Updates the application according to the Pygame event passed in
    #Precondition: There must be an instance of GraphVisual and a pygame event must be passed in
    #Postcondition: The application is updated
    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.path_done = True
            self.clear_screen()
            self.pressed_enter = False
            self.astar.reset()
            del self.parents[:]
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
                        self.current_state = self.astar.grid.nodes[count].traversable
                        self.astar.grid.nodes[count].toggle_state()
                        self.mouse_is_down = True
                    count += 1
        if event.type == pygame.MOUSEBUTTONUP:
            self.clear_screen()
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
                self.clear_screen()
                mouse_x, mouse_y = event.pos
                self.start_square.x = mouse_x + self.offset_x
                self.start_square.y = mouse_y + self.offset_y
            elif self.dragging_goal:
                self.clear_screen()
                mouse_x, mouse_y = event.pos
                self.goal_square.x = mouse_x + self.offset_x
                self.goal_square.y = mouse_y + self.offset_y
            elif self.mouse_is_down:
                count = 0
                for node in self.node_visual_colliders:
                    if (node.collidepoint(event.pos) and
                            self.astar.grid.nodes[count].traversable is self.current_state):
                        self.astar.grid.nodes[count].toggle_state()
                    count += 1
        if pygame.key.get_pressed()[pygame.K_c]:
            self.clear_screen()
            self.clear_grid()
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            self.toggle_shift = False
            self.toggle_ctrl = False
            self.closed_list_animated = 0
            self.closed_list_done = False
            self.path_done = False
            self.pressed_enter = True
            if (self.astar.start_node.position is not None and
                    self.astar.goal_node.position is not None):
                self.astar.update(self.astar.start_node, self.astar.goal_node)
        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
            self.clear_screen()
            self.toggle_shift = not self.toggle_shift
            time.sleep(.1)
        if pygame.key.get_mods() & pygame.KMOD_CTRL:
            self.clear_screen()
            self.toggle_ctrl = not self.toggle_ctrl
            time.sleep(.1)
        self.draw_nodes()
        self.draw_closed_list()
        if self.closed_list_done:
            self.draw_path()
        if self.toggle_shift:
            self.draw_parents()
        pygame.draw.rect(self.draw_surface, (0, 230, 0), self.start_square)
        pygame.draw.rect(self.draw_surface, (235, 0, 0), self.goal_square)
        if self.toggle_ctrl:
            self.draw_node_information()
