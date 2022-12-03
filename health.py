import pygame
from pygame.sprite import Sprite
import settings
from random import randint


class Health(Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("images/kenney_simplifiedplatformer/PNG/Items/platformPack_item010.png")
        self.rect = self.image.get_rect()
        self.number = 3
        self.random_place = randint(0, 800)
        self.rect.center = position


    def update(self, fish):
        self.rect.x -= 3
        self.rect.y = self.random_place
        if self.rect.x < 0:
            self.rect.x = settings.SCREEN_WIDTH
            self.rect.y = self.random_place

        if pygame.sprite.collide_rect(self, fish):
            self.rect.x = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)