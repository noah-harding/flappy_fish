import pygame
from pygame.sprite import Sprite
import settings

class PowerUp(Sprite):
# A class to define power-ups
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("images/kenney_simplifiedplatformer/PNG/Items/platformPack_item010.png")
        self.rect = self.image.get_rect()
        self.rect.center = position


    def update(self, fish): # Update the power-up across the screen
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.x = settings.SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)