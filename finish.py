import pygame

class Finish():
    def __init__(self):
        self.status = 'nonactivated'
    def finish(self,counter,player):
        player.direction = 'finish'
        self.font = pygame.font.Font("fonts/sofia.ttf", 60)
        self.surf = self.font.render(f'Your score is {counter.value}', True, [255, 255, 255], None)
        self.surf.set_alpha(110)
        self.rect = self.surf.get_rect(center=[350,207])
        self.status = 'activated'
    def check(self,screen):
        if self.status == 'activated':
            screen.blit(self.surf,self.rect)