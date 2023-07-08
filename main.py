import pygame, sys
from Fruit import Fruit

pygame.init()
cell_size = 35
cell_number = 20
width = cell_number * cell_size
height = cell_number * cell_size
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fruit = Fruit(screen, cell_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70)) 
    fruit.draw_fruit()

    pygame.display.update()
    clock.tick(60)