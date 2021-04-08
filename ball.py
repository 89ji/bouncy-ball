import pygame, sys, random
from pygame.locals import *

class physicsBall():
  xVel = 0
  xPFLC = 0 #Position from last click
  xTSLB = 59 #Time since last bounce

  yVel = 0
  yPFLC = 0
  yTSLB = 59

  WMOHLF = False #Was mouse one held last frame?

  def __init__(self, image, xStart = 0, yStart = 0, fps = 60):
    self.image = image
    self.xStart = xStart
    self.yStart = yStart
    self.tickSize = 1/fps
    self.ball = pygame.image.load(self.image)
    self.ballRect = self.ball.get_rect()
    self.ballRect.x = self.xStart
    self.ballRect.y = self.yStart

  ### Acceleration Related Methods ###

  def accelCalc(self):
    if pygame.mouse.get_pressed()[0]:
      self.snapToCursor()
    elif (self.ballRect.top < 0 or self.ballRect.bottom > 500) and self.yTSLB >= 5:
      self.bounce()
      self.yTSLB = 0
    else:
      self.naturalAccel()
    self.yTSLB += 1
    self.yMouseMovement()

  def snapToCursor(self):
    self.yVel = 0
    mouseX, mouseY = pygame.mouse.get_pos()
    self.ballRect.x = mouseX - 30
    self.ballRect.y = mouseY - 30

  def bounce(self):
    self.yVel *= -.95
    self.yTLSB = 0

  def naturalAccel(self):
    self.yVel += 30 * self.tickSize

  def yMouseMovement(self):
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseMove = mouseY - self.yPFLC

    if not pygame.mouse.get_pressed()[0] and self.WMOHLF:
      self.yVel = mouseMove    
    self.yPFLC = mouseY
    
  ### Horizontal Movement Related Methods ###

  def horizCalc(self):
    self.mouseMovement()
    self.hBounce()
    self.xTSLB += 1

  def mouseMovement(self):
    mouseX, mouseY = pygame.mouse.get_pos()
    
    if not pygame.mouse.get_pressed()[0] and self.WMOHLF:
      self.xVel = mouseX - self.xPFLC
    
    self.xPFLC = mouseX

  def hBounce(self):
    if (self.ballRect.left < 0 or self.ballRect.right > 500) and  self.xTSLB >= 5:
      self.xVel *= -.90
      self.xTSLB = 0

  def clampSpeed(self):
    if self.xVel > 30:
      self.xVel = 30
    if self.yVel > 30:
      self.yVel = 30

  def exist(self):
    self.accelCalc()
    self.horizCalc()
    self.clampSpeed()
    if pygame.mouse.get_pressed()[0]:
      self.WMOHLF = True
    else:
      self.WMOHLF = False
    self.ballRect.move_ip(self.xVel, self.yVel)