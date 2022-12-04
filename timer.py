import pygame
import settings
from pygame.sprite import Sprite

class Timer(Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont("bahnschrift", 80)
        self.minutes = 0
        self.seconds = 0

    def update(self):
        total_seconds = settings.FRAME_COUNT // settings.FRAME_RATE
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60
        total_seconds = settings.START_TIME + (settings.FRAME_COUNT // settings.FRAME_RATE)
        settings.FRAME_COUNT += 1
        if total_seconds >= 10:
            settings.OBSTICALE_SPEED = 8
        if total_seconds >= 20:
            settings.OBSTICALE_SPEED = 11
        if total_seconds >= 30:
            settings.OBSTICALE_SPEED = 14
        if total_seconds >= 40:
            settings.OBSTICALE_SPEED = 17
        if total_seconds >= 60:
            settings.OBSTICALE_SPEED = 20

    def draw(self, screen):
        time_display = "{0:02}:{1:02}".format(self.minutes, self.seconds)
        text = self.font.render(time_display, True, (227, 124, 7))
        screen.blit(text, (20, 20))