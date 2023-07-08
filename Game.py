import pygame, sys

from Fruit import Fruit
from Snake import Snake

class Game:

    def __init__(self, screen, cell_size, cell_number):
        self.snake = Snake(screen, cell_size)
        self.fruit = Fruit(screen, cell_size, cell_number)

    def update(self):
        self.snake.move()
        self.check_collision()   
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw()
        self.snake.draw()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.grow()
    
    def check_fail(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        pygame.quit()
        sys.exit()