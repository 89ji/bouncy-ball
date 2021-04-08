import pygame, sys, random
from pygame.locals import *
from ball import *

fps = 60
fpsClock = pygame.time.Clock()

screenSize = (500,500)
pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('Dick Vitales "Awesome Baby" College Hoops 2!')
fpsClock = pygame.time.Clock()

ballImage = 'ball_blue_large.png'

ball = physicsBall(ballImage, 100, 100, 60)

active = True

while active:
  for event in pygame.event.get():
    if event.type == QUIT:
      active = False
  
  screen.fill((255, 255, 255))

  ball.exist()
  screen.blit(ball.ball, ball.ballRect)

  
  pygame.display.update()
  fpsClock.tick(fps)