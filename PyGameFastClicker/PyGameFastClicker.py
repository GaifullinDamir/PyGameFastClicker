import pygame
import time

pygame.init()
backColor = (255, 255, 255) 
mainWindow = pygame.display.set_mode((500, 500)) 
mainWindow.fill(backColor)
clock = pygame.time.Clock()  

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fillColor = color
    def color(self,newColor):
        self.fillColor = newColor
    def fill(self):
        pygame.draw.rect(mainWindow, self.fillColor, self.rect)
    def outline(self, frameColor, thickness):
        pygame.draw.rect(mainWindow, frameColor, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Label(Area):
    def setText(self, text, fsize = 12, textColor = (0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, textColor)
    def draw(self, shiftX = 0, shiftY = 0):
        self.fill()
        mainWindow.blit(self.image, (self.rect.x + shiftX, self.rect.y +shiftY))

RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
cards = []
num_cards = 4
x = 70

for i in range(num_cards):
  newCard = Label(x, 170, 70, 100, YELLOW)
  newCard.outline(BLUE, 10)
  newCard.setText('CLICK', 14)
  cards.append(newCard)
  x = x + 100
 
wait = 0
from random import randint

while True:
  if wait == 0:
      #переносим надпись:
      wait = 20 #столько тиков надпись будет на одном месте
      click = randint(1, num_cards)
      for i in range(num_cards):
          cards[i].color((255,255,0))
          if (i + 1) == click:
              cards[i].draw(10, 40)
          else:
              cards[i].fill()
  else:
      wait -= 1
 
  pygame.display.update()
  clock.tick(60)
 

