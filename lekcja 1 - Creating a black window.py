import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
# tytuł
pygame.display.set_caption("Runner")
# klatki na sekunde
clock = pygame.time.Clock()

while True:
    # draw all our elements
    # update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    # klatki
    clock.tick(60)
