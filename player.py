import pygame
from pygame.locals import (
K_ESCAPE,
KEYDOWN,
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT
)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255,255,255))
        self.surf = pygame.image.load('graphics/head_down.png')
        self.rect = self.surf.get_rect(center=(350,350))
        self.direction = 'start'
    def check_move(self,key_pressed):
        if self.direction != 'finish':
            if key_pressed[K_UP] and self.direction != 'down':
                self.direction = 'up'
                self.surf = pygame.image.load('graphics/head_up.png')
            if key_pressed[K_DOWN] and self.direction != 'up':
                self.direction = 'down'
                self.surf = pygame.image.load('graphics/head_down.png')
            if key_pressed[K_LEFT] and self.direction != 'right':
                self.direction = 'left'
                self.surf = pygame.image.load('graphics/head_left.png')
            if key_pressed[K_RIGHT] and self.direction != 'left':
                self.direction = 'right'
                self.surf = pygame.image.load('graphics/head_right.png')
    def update(self,keypresed):
        if self.direction == 'right':
            self.rect.move_ip(50,0)
        if self.direction == 'left':
            self.rect.move_ip(-50,0)
        if self.direction == 'up':
            self.rect.move_ip(0,-50)
        if self.direction == 'down':
            self.rect.move_ip(0,50)

    def bodycollide(self):
        if self.direction == 'up':
            self.rect.move_ip(0, 50)
        if self.direction == 'down':
            self.rect.move_ip(0, -50)
        if self.direction == 'right':
            self.rect.x.move_ip(-50, 0)
        if self.direction == 'left':
            self.rect.move_ip(50, 0)