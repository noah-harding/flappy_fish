import pygame.font
import settings

class Scoreboard:

    def __init__(self):
        self.settings = settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("bahnschrift", 40)
        self.stats =
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
