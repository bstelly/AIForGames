#pylint: disable = E1101
import pygame
from vector2 import Vector2

def main():
    pygame.init()
    screen_height = 768
    screen_width = 1360
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 255))
    m_position = Vector2(500, 700)
    scale_x = 50
    scale_y = 50
    while True:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 and
                m_position.x_pos >= 0):
            m_position = m_position + Vector2(-1, 0)
        if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 and
                m_position.x_pos <= screen_width - scale_x):
            m_position = m_position + Vector2(1, 0)
        if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 and
                m_position.y_pos <= screen_height - scale_y):
            m_position = m_position + Vector2(0, 1)
        if (pygame.key.get_pressed()[pygame.K_UP] != 0 and
                m_position.y_pos >= 0):
            m_position = m_position + Vector2(0, -1)
        pygame.draw.rect(screen, (0, 255, 0), (m_position.x_pos, m_position.y_pos,
                                               scale_x, scale_y))
        pygame.display.flip()

main()
