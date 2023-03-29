import random
import pygame
import pygame.sprite
import counter

class Fruit(pygame.sprite.Sprite):
    def __init__(self,screen,player):
        super(Fruit, self).__init__()
        self.surf = pygame.Surface([50,50])
        self.surf.fill([255,0,0])
        self.rect = self.surf.get_rect(center = (-100,-100))
        self.spawn()
        print('spawned')
    def spawn(self):
        self.rect.x = random.randint(0, 12) * 50 + 25
        self.rect.y = random.randint(0, 12) * 50 + 25
    def check(self,player,fruit_group,counter):
        if pygame.sprite.spritecollideany(player,fruit_group):
            self.spawn()
            counter.count()
