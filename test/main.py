#initialization
import pygame
from counter import Counter
from fruit import Fruit
from player import Player
from board import Board,Border,Layout
from greeting import Greeting
from body import Body
from pygame.locals import (
K_ESCAPE,
KEYDOWN,
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT
)
#deafults variables
pygame.init()
screen = pygame.display.set_mode([700,700])
clock = pygame.time.Clock()
greeting = Greeting()
layout = Layout()
player = Player()
border = Border()
board = Board()
fruit = Fruit(screen,player)
counter = Counter()
running = True
body = Body()
snake_move = pygame.USEREVENT + 1
pygame.time.set_timer(snake_move,200)


fruit_group = pygame.sprite.Group()
fruit_group.add(fruit)
body_group = pygame.sprite.Group()
direction_list = []
while running:
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == snake_move:
            player.update(key_pressed)
            if player.direction != '':
                direction_list.insert(0,(player.rect.x,player.rect.y))
    if len(direction_list) > counter.value + 1:
        direction_list.pop()
    print(direction_list)
    player.check_move(key_pressed)
    fruit.check(player,fruit_group,counter)
    border.check(player)
    layout.update(screen)
    board.loop(screen)
    screen.blit(player.surf, player.rect)
    body.render(direction_list, screen, player)
    screen.blit(fruit.surf, fruit.rect)
    counter.update(screen)
    greeting.update(screen, player)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

