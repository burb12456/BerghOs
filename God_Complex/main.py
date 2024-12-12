
import pygame
pygame.init()
clock = pygame.time.Clock()

BG_COLOUR = (255, 255, 255)

screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Project God Complex")
while True:
    screen.fill((BG_COLOUR))
    pygame.display.flip()
    print('hi')
    clock.tick(60)
    pygame.display.update()
pygame.exit()