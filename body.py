import pygame
class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.surf = pygame.Surface([50, 50])
        self.surf.fill([255, 255, 255])
        self.rect = self.surf.get_rect()
    def render(self,direction_list,screen,player,finish,counter):
        for i in range(1,len(direction_list)):
            self.rect.x = direction_list[i][0]
            self.rect.y = direction_list[i][1]
            if i % 2:
                self.surf.fill((0, 178, 246))
            else:
                self.surf.fill([0, 172, 242])
            if (self.rect.x,self.rect.y) == (player.rect.x,player.rect.y):
                finish.finish(counter,player)
                player.bodycollide()
            screen.blit(self.surf,self.rect)