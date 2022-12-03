import pygame
import settings
from pygame.sprite import Sprite

class Timer(Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 80)

    def update(self, screen):
        total_seconds = settings.FRAME_COUNT // settings.FRAME_RATE
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        time_display = "{0:02}:{1:02}".format(minutes, seconds)
        text = self.font.render(time_display, True, (227, 124, 7))
        screen.blit(text, (20, 20))
        total_seconds = settings.START_TIME + (settings.FRAME_COUNT // settings.FRAME_RATE)
        settings.FRAME_COUNT += 1
        if total_seconds > 10:
            settings.OBSTICALE_SPEED = 8
        if total_seconds > 20:
            settings.OBSTICALE_SPEED = 11
        if total_seconds > 30:
            settings.OBSTICALE_SPEED = 14
        if total_seconds > 40:
            settings.OBSTICALE_SPEED = 17
        if total_seconds > 60:
            settings.OBSTICALE_SPEED = 20