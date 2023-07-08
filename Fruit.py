import pygame, random 
from pygame.math import Vector2

class Fruit:
    def __init__(self, screen, cell_size, cell_number):
        self.screen = screen
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.randomize()
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()
        
    def draw(self):
        x = int(self.pos.x * self.cell_size)
        y = int(self.pos.y * self.cell_size)
        fruit_rect = pygame.Rect( x,y, self.cell_size, self.cell_size)
        self.screen.blit(self.apple, fruit_rect)
        # pygame.draw.rect(self.screen, (126, 166, 114), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)