import pygame, random 
from pygame.math import Vector2

class Fruit:
    def __init__(self, surface, cell_size):
        self.x = random.randint(0, cell_size)
        self.y = random.randint(0, cell_size)
        self.surface = surface
        self.cell_size = cell_size
        self.pos = Vector2(self.x, self.y) 
        # create x, y position
        # draw a square 
    
    def draw_fruit(self):
        x = int(self.pos.x * self.cell_size)
        y = int(self.pos.y * self.cell_size)
        fruit_rect = pygame.Rect( x,y, self.cell_size, self.cell_size)
        pygame.draw.rect(self.surface, (126, 166, 114), fruit_rect)
