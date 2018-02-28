#pylint: disable = E1101
import pygame
from draw_utils import Rectangle
from draw_utils import Circle
from draw_utils import Line
from draw_utils import Ellipse
from vector2 import Vector2

def main():
    pygame.init()
    screen_height = 768
    screen_width = 1360
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 255))
    position = Vector2(500, 700)
    scale_x = 50
    scale_y = 50
    while True:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 and
                position.x_pos >= 0):
            position = position + Vector2(-1, 0)
        if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and
                position.x_pos <= screen_width - scale_x):
            position = position + Vector2(1, 0)
        if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 and
                position.y_pos <= screen_height - scale_y):
            position = position + Vector2(0, 1)
        if (pygame.key.get_pressed()[pygame.K_UP] != 0 and
                position.y_pos >= 0):
            position = position + Vector2(0, -1)
        rect = Rectangle(screen, (0, 255, 0), position, scale_x, scale_y)
        circ = Circle(screen, (255, 0, 0), position, 20)
        line = Line(screen, (0, 255, 0), Vector2(100, 100), Vector2(1300, 700))
        ellipse = Ellipse(screen, (0, 255, 0), Vector2(300, 500), 100, 50)
        pygame.display.flip()

main()
