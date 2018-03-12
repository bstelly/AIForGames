#pylint: disable = W0312
#pylint: disable = E1101
import pygame


class Rectangle:
    '''Class for drawing rectangles to the screen'''
    def __init__(self, draw_surface, color, position, scale_x, scale_y):
        self.surface = draw_surface
        self.color = color
        self.position = position
        self.length = scale_x
        self.height = scale_y
        self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.position.x_pos, self.position.y_pos,
                                                    self.length, self.height))

class Circle:
    '''Class for drawing circles to the screen'''
    def __init__(self, draw_surface, color, position, radius):
        self.surface = draw_surface
        self.color = color
        self.position = position
        self.radius = radius
        self.draw()

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.position.x_pos,
                                                      self.position.y_pos), self.radius)

class Line:
    '''Class for drawing lines to the screen'''
    def __init__(self, draw_surface, color, start_pos, end_pos, width):
        self.surface = draw_surface
        self.color = color
        self.start_position = start_pos
        self.end_position = end_pos
        self.width = width
        self.draw()

    def draw(self):
        pygame.draw.line(self.surface, self.color, (self.start_position.x_pos,
                                                    self.start_position.y_pos),
                         (self.end_position.x_pos, self.end_position.y_pos), self.width)

class Ellipse:
    '''Class for drawing ellipses to the screen'''
    def __init__ (self, draw_surface, color, position, scale_x, scale_y):
        self.surface = draw_surface
        self.color = color
        self.position = position
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.draw()

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, (self.position.x_pos,
                                                       self.position.y_pos, self.scale_x,
                                                       self.scale_y))

#class Text:
#    '''Class for drawing text to the screen'''
#    def __init__(self)