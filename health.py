import pygame
from pygame.sprite import Sprite
import settings


class Health(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/kenney_simplifiedplatformer/PNG/Items/platformPack_item017.png")
        self.rect = self.image.get_rect()
        self.number = 3

    def update(self):
        self.rect.x -= 10
        if self.rect.x < 0:
            self.rect.x = settings.SCREEN_WIDTH

    def draw_health_item(self, screen):
        for y in range(settings.NUMTILES):
            screen.blit(self.image, self.rect)