import pygame
from pygame.locals import (K_SPACE)
class Finish():
    def __init__(self,totaldo):
        self.font = pygame.font.Font("fonts/sofia.ttf", 60)
        self.font2 = pygame.font.Font("fonts/sofia.ttf", 30)
        self.font3 = pygame.font.Font('fonts/sofia.ttf', 35)
        self.font4 = pygame.font.Font('fonts/sofia.ttf',43)
        self.surf = self.font.render('', True, [255, 255, 255], None)
        self.surf2 = self.font.render('', True, [255, 255, 255], None)
        self.surf3 = self.font3.render('MAX SCORE',True,[255,255,255],None)
        self.surf4 = self.font4.render(str(max(totaldo)),True,[255,255,255],None)
        self.surf.set_alpha(110)
        self.surf2.set_alpha(110)
        self.rect3 = self.surf3.get_rect(center=[575,45])
        self.rect4 = self.surf4.get_rect(center = [575,75])
        self.surf3.set_alpha(110)
        self.surf4.set_alpha(110)

    def finish(self,counter,player,totaldo):
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
        screen.blit(self.surf3,self.rect3)
        screen.blit(self.surf4,self.rect4)
    def restart(self,player,key_pressed,direction_list,counter,totaldo):
        if player.direction == 'finish':
            if key_pressed[K_SPACE]:
                player.surf = pygame.image.load('graphics/head_down.png')
                totaldo.append(counter.value)
                self.surf4 = self.font4.render(str(max(totaldo)), True, [255, 255, 255], None)
                self.surf4.set_alpha(110)
                counter.value = 0
                direction_list.clear()
                player.direction = 'start'
                player.rect.x = 325
                player.rect.y = 325