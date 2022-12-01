import pygame
from pygame.sprite import Sprite
import settings
from random import randint


class Health(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/kenney_simplifiedplatformer/PNG/Items/platformPack_item017.png")
        self.rect = self.image.get_rect()
        self.number = 3
        self.random_place = randint(0, 800)

    def update(self):
        self.rect.x -= 10
        self.rect.y = self.random_place
        if self.rect.x < 0:
            self.rect.x = settings.SCREEN_WIDTH
            self.rect.y = self.random_place

    def draw_health_item(self, screen):
        screen.blit(self.image, self.rect)