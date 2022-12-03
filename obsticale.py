import pygame
from pygame.sprite import Sprite
import settings
from random import randint
class Obsticale(Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.surface.Surface((64, 200))
        self.rect = self.image.get_rect()
        self.color = (50, 50, 50)
        self.rect.center = position

    def update(self):
        self.rect.x -= settings.OBSTICALE_SPEED
        if self.rect.x < 0:
            self.rect.x = settings.SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)
