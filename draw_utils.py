#pylint: disable = W0312
#pylint: disable = E1101
import pygame


class Rectangle:
    '''Class for drawing rectangles to the screen'''
 
    #Prototype: def __init__(self, draw_surface, color, position, scale_x, scale_y)
    #Arguments: A draw surface, color, Vector2, an interger for length, and interger for height
    #Description: Creates a Rectangle object and draws a rectangle to the screen
    #Precondition: There must be a drawing surface created using pygame
    #Postcondition: A Rectangle object is created and is drawn to the screen
    def __init__(self, draw_surface, color, position, scale_x, scale_y):
        self.surface = draw_surface
        self.color = color
        self.position = position
        self.length = scale_x
        self.height = scale_y
        self.draw()
        
    #Prototype: def draw(self)
    #Arguments: None
    #Description: Draws a rectangle to the screen
    #Precondition: There must be a drawing surface created using pygame
    #Postcondition: A rectangle is drawn to the screen
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.position.x_pos, self.position.y_pos,
                                                    self.length, self.height))

class Circle:
    '''Class for drawing circles to the screen'''
            
    #Prototype: def __init__(self, draw_surface, color, position, radius)
    #Arguments: A draw surface, color, Vector2, and an interger for radius
    #Description: Creates a circle object and draws a circle to the screen
    #Precondition: There must be a drawing surface created using pygame
    #Postcondition: A Circle object is created and drawn to the screen
    def __init__(self, draw_surface, color, position, radius):
        self.surface = draw_surface
        self.color = color
        self.position = position
        self.radius = radius
        self.draw()
        
    #Prototype: def draw(self)
    #Arguments: None
    #Description: Draws a Circle to the screen
    #Precondition: There must be a drawing surface created using pygame
    #Postcondition: A Circle is drawn to the screen
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.position.x_pos,
                                                      self.position.y_pos), self.radius)

class Line:
    '''Class for drawing lines to the screen'''
            
    #Prototype: def __init__(self, draw_surface, color, start_pos, end_pos, width)
    #Arguments: A drawing surface, color, a Vector2 for start pos, a Vector2 for end pos,
    #           and an int for width
    #Description: Creates an instance of the Line class and draws a line to the screen
    #Precondition: There must be a drawing surface created using pygame
    #Postcondition: An instance of the Line class is created and a line is drawn to the screen
    def __init__(self, draw_surface, color, start_pos, end_pos, width):
        self.surface = draw_surface
        self.color = color
        self.start_position = start_pos
        self.end_position = end_pos
        self.width = width
        self.draw()
        
    #Prototype: def draw(self)
    #Arguments: None
    #Description: Draws a line to the screen
    #Precondition: A drawing surface must be created using pygame
    #Postcondition: A line is drawn to the screen
    def draw(self):
        pygame.draw.line(self.surface, self.color, (self.start_position.x_pos,
                                                    self.start_position.y_pos),
                         (self.end_position.x_pos, self.end_position.y_pos), self.width)

class Ellipse:
    '''Class for drawing ellipses to the screen'''
            
    #Prototype: def __init__ (self, draw_surface, color, position, scale_x, scale_y)
    #Arguments: a draw surface, color, Vector2, an int for length and an int for height
    #Description: Creates an instance of the Ellipse class and draws an ellipse to the screen
    #Precondition: There must be a draw surface created using pygame
    #Postcondition: An Ellipse object is created and an ellipse is drawn to the screen
    def __init__ (self, draw_surface, color, position, scale_x, scale_y):
        self.surface = draw_surface
        self.color = color
        self.position = position
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.draw()
        
    #Prototype: def draw(self)
    #Arguments: None
    #Description: Draws an ellipse to the screen
    #Precondition: There must be a draw surface created using pygame
    #Postcondition: An ellipse is drawn to the screen
    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, (self.position.x_pos,
                                                       self.position.y_pos, self.scale_x,
                                                       self.scale_y))

class Text:
    '''Class for drawing text to the screen'''
            
    #Prototype: def __init__(self, text, font_theme, font_size, color, draw_surface, x_pos, y_pos)
    #Arguments: A string, A string for font name, an int for font size, color, draw surface, int
    #           for x pos, and int for y pos
    #Description: Creates a text object and draws it to the screen
    #Precondition: A draw surface must be created using pygame
    #Postcondition: A text object is created and drawn to the screen
    def __init__(self, text, font_theme, font_size, color, draw_surface, x_pos, y_pos):
        self.font_theme = font_theme
        self.font_size = font_size
        self.font = pygame.font.SysFont(font_theme, font_size)
        self.color = color
        self.surface = draw_surface
        self.text = self.font.render(text, True, self.color)
        self.x = x_pos
        self.y = y_pos
        self.draw()
        
    #Prototype: def draw(self)
    #Arguments: None
    #Description: Draws text to the screen
    #Precondition: There must be a draw surface created using pygame
    #Postcondition: Text is drawn to the screen
    def draw(self):
        self.surface.blit(self.text, (self.x, self.y))
