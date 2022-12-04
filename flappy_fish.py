import pygame
import sys
import settings
from pygame import mixer
from random import randint
from fish import Fish
from obsticale import Obsticale
from health import Health
from timer import Timer
from button import Button

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
settings.SCREEN_WIDTH = screen.get_rect().width
settings.SCREEN_HEIGHT = screen.get_rect().height
def play():
    pygame.display.set_caption("Flappy Fish")

    water_full = pygame.image.load("images/water_full.png")
    water_full_rect = water_full.get_rect()
    sand_full = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_001.png")
    sand_full_rect = sand_full.get_rect()

    background = pygame.surface.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    background.fill((120, 181, 250))
    for y in range(settings.SCREEN_WIDTH // settings.TILE_SIZE):
        for x in range(settings.SCREEN_WIDTH // settings.TILE_SIZE):
            background.blit(water_full, (x * water_full_rect.width, y * water_full_rect.height))
            background.blit(sand_full, (x * sand_full_rect.width, settings.SCREEN_HEIGHT - settings.TILE_SIZE))


    fish = Fish(screen)
    obsticales = pygame.sprite.Group(Obsticale((settings.SCREEN_WIDTH, 50)),
                                     Obsticale((settings.SCREEN_WIDTH + 200, 910)),
                                     Obsticale((settings.SCREEN_WIDTH + 250, 200)),
                                     Obsticale((settings.SCREEN_WIDTH + 550, 500)),
                                     Obsticale((settings.SCREEN_WIDTH + 720, 100)),
                                     Obsticale((settings.SCREEN_WIDTH + 800, 720)),
                                     Obsticale((settings.SCREEN_WIDTH + 1100, 250)),
                                     Obsticale((settings.SCREEN_WIDTH + 1300, 850)),
                                     Obsticale((settings.SCREEN_WIDTH + 1400, 400)),
                                     Obsticale((settings.SCREEN_WIDTH + 1600, 800)),
                                     Obsticale((settings.SCREEN_WIDTH + 1700, 200)),
                                     Obsticale((settings.SCREEN_WIDTH + 1850, 650)))

    power_ups = pygame.sprite.Group(Health((settings.SCREEN_WIDTH + 500, 200)),
                                    Health((settings.SCREEN_WIDTH + 1000, 800)))

    # music
    mixer.init()
    mixer.music.load("sounds/summer.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play()

    timer = Timer()

    game_over = False

    while not game_over:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    fish.moving_up = True
                elif event.key == pygame.K_DOWN:
                    fish.moving_down = True
                elif event.key == pygame.K_RIGHT:
                    fish.moving_right = True
                elif event.key == pygame.K_LEFT:
                    fish.moving_left = True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    fish.moving_up = False
                elif event.key == pygame.K_DOWN:
                    fish.moving_down = False
                elif event.key == pygame.K_RIGHT:
                    fish.moving_right = False
                elif event.key == pygame.K_LEFT:
                    fish.moving_left = False
            if event.type == pygame.QUIT:
                sys.exit()

        # update objects
        fish.update(obsticales, power_ups)
        obsticales.update()
        power_ups.update(fish)
        timer.update()
        for power_up in power_ups.copy():
            if pygame.sprite.collide_rect(power_up, fish):
                power_ups.remove(power_up)

        # blit objects
        screen.blit(background, (0, 0))
        fish.blitme()
        obsticales.draw(screen)
        power_ups.draw(screen)
        timer.draw(screen)
        clock.tick(settings.FRAME_RATE)
        pygame.display.flip()

def options():
    pygame.display.set_caption("Options")

    while True:
        screen.fill((128, 242, 255))

def main_menu():
    pygame.display.set_caption("Main Menu")

    while True:
        screen.fill((128, 242, 255))
        font1 = pygame.font.SysFont("showcardgothic", 100)
        font2 = pygame.font.SysFont("cooperblack", 75)
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = font1.render("FLAPPY FISH", True, (196, 158, 71))
        menu_rect = menu_text.get_rect(center=(settings.SCREEN_WIDTH / 2, 100))

        play_button = Button(None, pos=(settings.SCREEN_WIDTH / 2, 300), text_input="PLAY", font=font2,
                             base_color=(0, 0, 0))
        high_score_button = Button(None, pos=(settings.SCREEN_WIDTH / 2, 500), text_input="HIGH SCORE", font=font2,
                                base_color=(0, 0, 0))
        quit_button = Button(None, pos=(settings.SCREEN_WIDTH / 2, 700), text_input="QUIT", font=font2,
                             base_color=(0, 0, 0))

        screen.blit(menu_text, menu_rect)

        for button in [play_button, high_score_button, quit_button]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_input(menu_mouse_pos):
                    pygame.mouse.set_visible(False)
                    play()
                if high_score_button.check_input(menu_mouse_pos):
                    options()
                if quit_button.check_input(menu_mouse_pos):
                    sys.exit()
        pygame.display.update()


main_menu()