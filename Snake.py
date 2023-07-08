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

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()    

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        if head_relation == Vector2(-1,0): self.head = self.head_right
        if head_relation == Vector2(0,1): self.head = self.head_up
        if head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        head_relation = self.body[-2] - self.body[-1]
        if head_relation == Vector2(1,0): self.tail = self.tail_left
        if head_relation == Vector2(-1,0): self.tail = self.tail_right
        if head_relation == Vector2(0,1): self.tail = self.tail_up
        if head_relation == Vector2(0,-1): self.tail = self.tail_down

    def draw(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x = int(block.x * self.cell_size)
            y = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x,y, self.cell_size, self.cell_size)
            
            if index == 0: self.screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1: self.screen.blit(self.tail, block_rect)
            else:
                prev_block = self.body[index - 1] - block
                next_block = self.body[index + 1] - block
                if prev_block.x == next_block.x:
                    self.screen.blit(self.body_vertical,block_rect)
                elif prev_block.y == next_block.y:
                    self.screen.blit(self.body_horizontal,block_rect)
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1: 
                        self.screen.blit(self.body_tl,block_rect)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1: 
                        self.screen.blit(self.body_br,block_rect)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1: 
                        self.screen.blit(self.body_bl,block_rect)
                    else: self.screen.blit(self.body_tr,block_rect) 

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
