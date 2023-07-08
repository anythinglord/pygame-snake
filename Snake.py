import pygame
from pygame.math import Vector2

class Snake:
    def __init__(self, screen, cell_size):
        self.body = [
            Vector2(5, 10), Vector2(6,10), Vector2(7,10)
        ]
        self.screen = screen
        self.cell_size = cell_size
    
    def draw(self):
        for block in self.body:
            x = int(block.x * self.cell_size)
            y = int(block.y * self.cell_size) 
            block_rect = pygame.Rect(x,y, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, (183, 111, 122), block_rect)