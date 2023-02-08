import random
import pygame
import pygame.sprite
import counter

class Fruit(pygame.sprite.Sprite):
    def __init__(self,screen,player,direction_list):
        super(Fruit, self).__init__()
        self.surf = pygame.Surface([50,50])
        self.surf.fill([255,0,0])
        self.surf = pygame.image.load('graphics/apple.png')
        self.rect = self.surf.get_rect(center = (-100,-100))
        self.spawn(direction_list)
    def spawn(self,direction_list):
        self.x = random.randint(0, 12) * 50 + 25
        self.y = random.randint(0, 12) * 50 + 25
        if (self.x,self.y) in direction_list:
            self.spawn(direction_list)
        else:
            self.rect.x = self.x
            self.rect.y = self.y

    def check(self,player,fruit_group,counter,direction_list):
        if pygame.sprite.spritecollideany(player,fruit_group):
            self.spawn(direction_list)
            counter.count()
