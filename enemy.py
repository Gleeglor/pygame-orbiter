import random
from pygame import *
import game

from pygame.locals import *

class Enemy():
      
      surface: Surface

      def __init__(self, surface):
        self.surface = surface

        self.image = image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, game.Settings.screen_width - 40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self):
        self.surface.blit(self.image, self.rect) 
 