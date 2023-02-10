import pygame
from pygame.locals import (K_SPACE)
class Finish():
    def __init__(self):
        self.font = pygame.font.Font("fonts/sofia.ttf", 60)
        self.font2 = pygame.font.Font("fonts/sofia.ttf", 30)
        self.surf = self.font.render('', True, [255, 255, 255], None)
        self.surf2 = self.font.render('', True, [255, 255, 255], None)
        self.surf.set_alpha(110)

        self.surf2.set_alpha(110)
        self.rect = self.surf.get_rect(center=[350,207])
        self.rect2 = self.surf2.get_rect(center=[350,500])

    def finish(self,counter,player):

        if player.direction == 'up':
            player.surf = pygame.image.load('graphics/up_death.png')
        elif player.direction == 'down':
            player.surf = pygame.image.load('graphics/down_death.png')
        elif player.direction == 'left':
            player.surf = pygame.image.load('graphics/left_death.png')
        elif player.direction == 'right':
            player.surf = pygame.image.load('graphics/right_death.png')
        player.direction = 'finish'
        self.surf = self.font.render(f'Your score is {counter.value}', True, [255, 255, 255], None)
        self.surf2 = self.font2.render('press space to play again', True, [255, 255, 255], None)
        self.surf2.set_alpha(110)
        self.rect = self.surf.get_rect(center=[350,207])
        self.rect2 = self.surf2.get_rect(center=[350,250])
    def update(self,screen,player):
        if player.direction == 'finish':
            screen.blit(self.surf,self.rect)
            screen.blit(self.surf2,self.rect2)
    def restart(self,player,key_pressed,direction_list,counter):
        if player.direction == 'finish':
            if key_pressed[K_SPACE]:
                player.surf = pygame.image.load('graphics/head_down.png')
                counter.value = 0
                direction_list.clear()
                player.direction = 'start'
                player.rect.x = 325
                player.rect.y = 325