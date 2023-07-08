import pygame
from pygame.math import Vector2

class Snake:
    def __init__(self, screen, cell_size):
        self.body = [
            Vector2(5, 10), Vector2(4,10), Vector2(3,10)
        ]
        self.direction = Vector2(1,0)
        self.is_growing = False
        self.screen = screen
        self.cell_size = cell_size
    
    def draw(self):
        for block in self.body:
            x = int(block.x * self.cell_size)
            y = int(block.y * self.cell_size) 
            block_rect = pygame.Rect(x,y, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, (183, 111, 122), block_rect)
    
    def move(self):
        if self.is_growing:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.is_growing = False
        else:    
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def grow(self):
        self.is_growing = True
        
    def move_up(self):
        self.direction = Vector2(0, -1)
    
    def move_down(self):
        self.direction = Vector2(0, 1)

    def move_left(self):
        self.direction = Vector2(-1, 0)
    
    def move_right(self):
        self.direction = Vector2(1, 0)
