import pygame.font
class Counter():
    def __init__(self):
        super(Counter, self).__init__()
        pygame.font.init()
        self.font = pygame.font.Font("font.ttf", 150)
        self.value = 0
        self.surf = self.font.render(str(self.value),True,[255,255,255],None)
        self.surf.set_alpha(110)
        self.rect = self.surf.get_rect(center=[350,50])
    def update(self,screen):
        self.surf = self.font.render(str(self.value),True,[255,255,255],None)
        self.surf.set_alpha(110)
        screen.blit(self.surf,self.rect)

    def count(self):
        self.value += 1