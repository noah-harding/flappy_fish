import pygame

class Obsticales:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/kenney_simplifiedplatformer/PNG/Tiles/platformPack_tile016.png")
        self.rect = self.image.get_rect()

    def build_obsticale(self):
        self.rect