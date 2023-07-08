import pygame, sys
from Fruit import Fruit
from Snake import Snake
from Game import Game

pygame.init()
cell_size = 35
cell_number = 20
width = cell_number * cell_size
height = cell_number * cell_size
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 90)

game = Game(screen, cell_size, cell_number)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                if game.snake.direction.y != 1: game.snake.move_up()
            if event.key == pygame.K_DOWN: 
                if game.snake.direction.y != -1: game.snake.move_down()
            if event.key == pygame.K_LEFT: 
                if game.snake.direction.x != -1: game.snake.move_left()
            if event.key == pygame.K_RIGHT: 
                if game.snake.direction.x != -1: game.snake.move_right()

    screen.fill((175,215,70)) 
    game.draw_elements()

    pygame.display.update()
    clock.tick(60)