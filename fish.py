import pygame
from pygame.sprite import Sprite

class Fish(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_079.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        self.lives = 3
    def update(self, obsticle):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 6
        if self.moving_down and self.rect.bottom < self.screen_rect.height - 64:
            self.rect.y += 6
        if self.moving_right and self.rect.right <  self.screen_rect.width:
            self.rect.x += 6
        if self.moving_left:
            self.rect.x -= 6

        # check if we hit the obsticle

        if pygame.sprite.collide_rect(self, obsticle):
            self.lives -= 1
            self.rect.right = obsticle.rect.left
            print("ouch")

        if self.rect.left <= 0:
            print("ouch")


    def blitme(self):
        self.screen.blit(self.image, self.rect)