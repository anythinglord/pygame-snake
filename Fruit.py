import pygame, random 
from pygame.math import Vector2

class Fruit:
    def __init__(self, screen, cell_size, cell_number):
        self.x = random.randint(0, cell_number)
        self.y = random.randint(0, cell_number)
        self.screen = screen
        self.cell_size = cell_size
        self.pos = Vector2(self.x, self.y) 
        
    def draw(self):
        x = int(self.pos.x * self.cell_size)
        y = int(self.pos.y * self.cell_size)
        fruit_rect = pygame.Rect( x,y, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, (126, 166, 114), fruit_rect)
