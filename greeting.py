import pygame.font
class Greeting():
    def __init__(self):
        super(Greeting, self).__init__()
        pygame.font.init()
        self.font = pygame.font.Font("fonts/sofia.ttf", 60)
        self.font2 = pygame.font.Font("fonts/sofia.ttf", 30)
        self.surf_luck = self.font.render('Good Luck',True,[255,255,255],None)
        self.surf_arrow_press = self.font2.render('press any arrow to start', True, [255, 255, 255], None)
        self.rect_luck = self.surf_luck.get_rect(center=[350,207])
        self.rect_arrow_press = self.surf_arrow_press.get_rect(center = [350,250])
        self.surf_arrow_press.set_alpha(110)
        self.surf_welcome = self.font.render('Welcome to SNAKE',True,[255,255,255],None)
        self.rect_welcome = self.surf_welcome.get_rect(center = [350,207 ])
    def update(self,screen,player):
        if player.direction == "start" or player.direction == '':
            if player.direction == 'start':
                screen.blit(self.surf_luck,self.rect_luck)
            if player.direction == '':
                screen.blit(self.surf_welcome,self.rect_welcome)
            screen.blit(self.surf_arrow_press,self.rect_arrow_press)