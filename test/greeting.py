import pygame.font
class Greeting():
    def __init__(self):
        super(Greeting, self).__init__()
        pygame.font.init()
        self.font = pygame.font.Font("sofia.ttf", 60)
        self.surf = self.font.render('press any arrow to start',True,[255,255,255],None)
        self.rect = self.surf.get_rect(center=[350,207])
    def update(self,screen,player):
        if player.direction == "":
            screen.blit(self.surf,self.rect)