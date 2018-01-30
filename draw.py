#pylint: disable = E1101
import pygame
from vector2 import Vector2

def main():
    pygame.init()
    screen = pygame.display.set_mode((1360, 768))
    screen.fill((0, 0, 255))
    m_position = Vector2(500, 700)
    while True:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            m_position = m_position + Vector2(-1, 0)
        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            m_position = m_position + Vector2(1, 0)
        if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            m_position = m_position + Vector2(0, 1)
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            m_position = m_position + Vector2(0, -1)
        pygame.draw.rect(screen, (0, 255, 0), (m_position.x_pos, m_position.y_pos, 50, 50))
        pygame.display.flip()

main()
