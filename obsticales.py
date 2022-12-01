import pygame
from pygame.sprite import Sprite
import settings
class Obsticales(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((64, 200))
        self.rect = self.image.get_rect()
        self.color = (50, 50, 50)
        self.rect.x = settings.SCREEN_WIDTH

    def update(self):
        self.rect.x -= 15
        if self.rect.x < 0:
            self.rect.x = settings.SCREEN_WIDTH

    def draw_obsticle(self, screen):
        screen.blit(self.image, self.rect)
