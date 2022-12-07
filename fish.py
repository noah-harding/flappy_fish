import pygame
from pygame.sprite import Sprite
import settings

class Fish(Sprite):
# A class to define my fish
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_079.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.rect.x = 400
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.lives = 3

    def update(self, obsticales, power_ups, timer):
    # Update my fish by checking for collisions and movement inputs
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= settings.FISH_SPEED
        if self.moving_down and self.rect.bottom < self.screen_rect.height - 64:
            self.rect.y += settings.FISH_SPEED
        if self.moving_right and self.rect.right <  self.screen_rect.width:
            self.rect.x += settings.FISH_SPEED
        if self.moving_left:
            self.rect.x -= settings.FISH_SPEED

        # check if we hit an obsticale
        for obsticale in obsticales:
            if pygame.sprite.collide_rect(self, obsticale):
                self.rect.right = obsticale.rect.left
                settings.COLLISION_COUNTER += 1

        # check if we hit a power up
        for power_up in power_ups:
            if pygame.sprite.collide_rect(self, power_up) and settings.COLLISION_COUNTER <= 1:
                settings.FISH_SPEED += 4
                settings.COLLISION_COUNTER += 1
                print("power up!")

        # check if the fish is off the screen
        if self.rect.left <= -30:
            self.lives = 0

        # if the fish is off the screen the game is over
        if self.lives == 0:
            print("game over")
            return False
        return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)