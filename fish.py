import pygame

class Fish:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_079.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 64:
            self.y -= 6
        if self.moving_down and self.rect.bottom < self.screen_rect.height - 64:
            self.y += 6

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)