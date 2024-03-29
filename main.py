#initialization
import pygame
from counter import Counter
from fruit import Fruit
from player import Player
from board import Board,Border,Layout
from greeting import Greeting
from body import Body
from finish import *

from pygame.locals import (
K_SPACE,
K_ESCAPE,
KEYDOWN,
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT
)
#deafults variables
pygame.init()
direction_list = []
totaldo = [0]
screen = pygame.display.set_mode([700,700])
clock = pygame.time.Clock()
greeting = Greeting()
layout = Layout()
player = Player()
border = Border()
board = Board()
fruit = Fruit(screen,player,direction_list)
counter = Counter()
running = True
body = Body()
finish = Finish(totaldo)
snake_move = pygame.USEREVENT + 1
pygame.time.set_timer(snake_move,200)
fruit_group = pygame.sprite.Group()
fruit_group.add(fruit)
body_group = pygame.sprite.Group()
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
            border.check(player, finish, counter,totaldo)
            if player.direction == 'start' or player.direction == 'finish':
                pass
            else:
                direction_list.insert(0,(player.rect.x,player.rect.y))
                if len(direction_list) > counter.value + 1:
                    direction_list.pop()
    player.check_move(key_pressed)
    fruit.check(player,fruit_group,counter,direction_list)
    layout.update(screen)
    board.loop(screen)
    body.render(direction_list, screen, player,finish,counter,totaldo)
    screen.blit(fruit.surf, fruit.rect)
    screen.blit(player.surf, player.rect)
    greeting.update(screen, player)
    counter.update(screen)
    finish.update(screen,player)
    finish.restart(player,key_pressed,direction_list,counter,totaldo)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

