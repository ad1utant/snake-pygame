import pygame
class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    def loop(self,screen):
        self.surf = pygame.Surface((50,50))
        self.surf.fill((142, 191, 84))
        self.rect = self.surf.get_rect(center = (50,50))
        divisibility = 2
        screen.blit(self.surf, self.rect)
        for vertical_square in range(13):
            if divisibility % 2 == 0:
                for horizontal_square in range(7):
                    screen.blit(self.surf, self.rect)
                    self.rect.move_ip(100,0)
                self.rect.move_ip(-650,50)
            else:
                for horizontal_square in range(6):
                    screen.blit(self.surf,self.rect)
                    self.rect.move_ip(100,0)
                self.rect.move_ip(-650,50)
            divisibility += 1
class Layout(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((650,650))
        self.surf.fill((164, 215, 99))
        self.rect = self.surf.get_rect(center=(350,350))
    def update(self,screen):
        screen.fill((79, 138, 63))
        screen.blit(self.surf,self.rect)
class Border():
    def check(self,player,finish,counter,totaldo):
        if player.rect.y < 25:
            player.rect.move_ip(0,50)
            finish.finish(counter,player,totaldo)
        if player.rect.y > 650:
            player.rect.move_ip(0,-50)
            finish.finish(counter,player,totaldo)
        if player.rect.x > 650:
            player.rect.move_ip(-50,0)
            finish.finish(counter,player,totaldo)
        if player.rect.x < 25:
            player.rect.move_ip(50,0)
            finish.finish(counter,player,totaldo)