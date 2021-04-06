import pygame, sys
from pygame.locals import *

fps = 60
fpsClock = pygame.time.Clock()

xVel = 0
yVel = 0

yPFLC = 0 #Vertical position from last click
yWMOHLF = False #Vertical was mouse one held last frame?

PFLC = 0 #Position from last click
WMOHLF = False #Was mouse one held last frame?

xTSLB = 59
yTSLB = 59

tickSize = 1/fps

### Acceleration Related Methods ###

def accelCalc():
  global yTSLB
  if pygame.mouse.get_pressed()[0]:
    snapToCursor()
  elif (ballRect.top < 0 or ballRect.bottom > 500) and yTSLB >= 5:
    bounce()
    yTSLB = 0
  else:
    naturalAccel()
  yTSLB += 1
  yMouseMovement()

def snapToCursor():
  global yVel
  yVel = 0
  mouseX, mouseY = pygame.mouse.get_pos()
  ballRect.x = mouseX - 30
  ballRect.y = mouseY - 30

def bounce():
  global yVel, yTSLB
  yVel *= -.95
  yTLSB = 0
  #print('bounce')

def naturalAccel():
  global yVel
  yVel += 30 * tickSize

def yMouseMovement():
  global yPFLC, yWMOHLF, yVel
  mouseX, mouseY = pygame.mouse.get_pos()
  mouseMove = mouseY - yPFLC
  if not pygame.mouse.get_pressed()[0] and yWMOHLF:
    yVel = mouseMove

  if pygame.mouse.get_pressed()[0]:
    yWMOHLF = True
  else:
    yWMOHLF = False

  yPFLC = mouseY

### Horizontal Movement Related Methods ###

def horizCalc():
  global xTSLB
  mouseMovement()
  hBounce()
  xTSLB += 1
  #print(xVel, yVel, xTSLB)

def mouseMovement():
  global PFLC, WMOHLF, xVel
  mouseX, mouseY = pygame.mouse.get_pos()
  mouseMove = mouseX - PFLC
  if not pygame.mouse.get_pressed()[0] and WMOHLF:
    xVel = mouseMove

  if pygame.mouse.get_pressed()[0]:
    WMOHLF = True
  else:
    WMOHLF = False

  PFLC = mouseX

def hBounce():
  global xVel, xTSLB
  if (ballRect.left < 0 or ballRect.right > 500) and xTSLB >= 5:
    xVel *= -.90
    xTSLB = 0

def clampSpeed():
  global xVel, yVel
  if xVel > 30:
    xVel = 30
  if yVel > 30:
    yVel = 30

### Pygame Stuff ###

screenSize = (500,500)
pygame.init()
screen = pygame.display.set_mode(screenSize)
fpsClock = pygame.time.Clock()

ball = pygame.image.load('ball_blue_large.png')
ballRect = ball.get_rect()
ballRect.x = 200
ballRect.y = 0

active = True

while active:
  for event in pygame.event.get():
    if event.type == QUIT:
      active = False
  
  accelCalc()
  horizCalc()
  clampSpeed()

  screen.fill((255, 255, 255))

  ballRect.move_ip(xVel, yVel)
  screen.blit(ball, ballRect)

  pygame.display.update()
  fpsClock.tick(fps)