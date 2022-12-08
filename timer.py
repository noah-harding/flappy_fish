import pygame
import settings
from pygame.sprite import Sprite

class Timer(Sprite):
# A class to define a timer
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont("bahnschrift", 80)
        self.minutes = 0
        self.seconds = 0
        self.frame_count = 0
        self.total_seconds = 0

    def update(self):
        # Update my clock every second and increase obstacle speed based on time
        self.frame_count += 1
        self.total_seconds = self.frame_count // settings.FRAME_RATE
        self.minutes = self.total_seconds // 60
        self.seconds = self.total_seconds % 60

        if self.total_seconds >= 10:
            settings.OBSTICALE_SPEED = 8
        if self.total_seconds >= 20:
            settings.OBSTICALE_SPEED = 11
        if self.total_seconds >= 30:
            settings.OBSTICALE_SPEED = 14
        if self.total_seconds >= 40:
            settings.OBSTICALE_SPEED = 17
        if self.total_seconds >= 60:
            settings.OBSTICALE_SPEED = 20
        if self.total_seconds >= 70:
            settings.OBSTICALE_SPEED = 23
        if self.total_seconds >= 80:
            settings.OBSTICALE_SPEED = 26
        if self.total_seconds >= 90:
            settings.OBSTICALE_SPEED = 29

    def reset(self): # Received help from Riley Haugen
        # Reset timer, obstacle speed, and fish speed
        self.frame_count = 0
        settings.OBSTICALE_SPEED = 5
        settings.FISH_SPEED = 8

    def draw(self, screen):
        # Draw the clock on the screen to count up every second
        time_display = "{0:02}:{1:02}".format(self.minutes, self.seconds)
        text = self.font.render(time_display, True, (227, 124, 7))
        screen.blit(text, (1700, 20))