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
        self.rect = self.surf.get_rect(center=(350,350))
        self.direction = ''
    def check_move(self,key_pressed):
        if key_pressed[K_UP] and self.direction != 'down':
            self.direction = 'up'
        if key_pressed[K_DOWN] and self.direction != 'up':
            self.direction = 'down'
        if key_pressed[K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        if key_pressed[K_RIGHT] and self.direction != 'left':
            self.direction = 'right'
    def update(self,keypresed):
        if self.direction == 'right':
            self.rect.move_ip(50,0)
        if self.direction == 'left':
            self.rect.move_ip(-50,0)
        if self.direction == 'up':
            self.rect.move_ip(0,-50)
        if self.direction == 'down':
            self.rect.move_ip(0,50)