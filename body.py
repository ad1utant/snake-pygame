import pygame
class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.surf = pygame.Surface([50, 50])
        self.surf.fill([255, 255, 255])
        self.rect = self.surf.get_rect()
        self.list = []
    def render(self,direction_list,screen,counter):
        for i in range(counter.value+1):
            self.rect.x = direction_list[i][0]
            self.rect.y = direction_list[i][1]
            self.list.append(direction_list[i])
            screen.blit(self.surf,self.rect)