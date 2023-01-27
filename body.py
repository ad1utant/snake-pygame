import pygame
class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.surf = pygame.Surface([40,40])
        self.surf.fill([255,255,255])
        self.rect = self.surf.get_rect()
