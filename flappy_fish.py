import pygame
import sys
import settings
from pygame import mixer
from random import randint
from fish import Fish
from obsticale import Obsticale
from health import Health
from timer import Timer

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))


def main_menu():
    pygame.display.set_caption("Main Menu")

    while True:
        screen.blit(0, 0, 0)
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(settings.SCREEN_WIDTH/2, 100))

        play_button = Button(image=pygame.image.load(images/))
pygame.display.set_caption("Flappy Fish")
screen_rect = screen.get_rect()
water_top = pygame.image.load("images/water_tile.png")
water_top_rect = water_top.get_rect()
water_full = pygame.image.load("images/water_full.png")
water_full_rect = water_full.get_rect()
sand_full = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_001.png")
sand_full_rect = sand_full.get_rect()


random_position_x = randint(0, 200)
random_position_y = randint(0, 896)

fish = Fish(screen)
obsticales = pygame.sprite.Group(Obsticale((settings.SCREEN_WIDTH, 50)),
                                 Obsticale((settings.SCREEN_WIDTH + 200, 800)),
                                 Obsticale((settings.SCREEN_WIDTH + 300, 200)),
                                 Obsticale((settings.SCREEN_WIDTH + 400, 500)),
                                 Obsticale((settings.SCREEN_WIDTH + 800, 600)),
                                 Obsticale((settings.SCREEN_WIDTH + 1300, 700)),
                                 Obsticale((settings.SCREEN_WIDTH + 1200, 250)),
                                 Obsticale((settings.SCREEN_WIDTH + 1400, 400)))

power_ups = pygame.sprite.Group(Health((settings.SCREEN_WIDTH + 500, 200)),
                                Health((settings.SCREEN_WIDTH + 1000, 800)))



background = pygame.surface.Surface((screen_rect.width, screen_rect.height))
background.fill((120, 181, 250))
for y in range(settings.NUMTILES):
    for x in range(settings.NUMTILES):
        background.blit(water_full, (x * water_full_rect.width, y * water_full_rect.height))
        background.blit(sand_full, (x * sand_full_rect.width, 896))

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
            if event.key == pygame.K_DOWN:
                fish.moving_down = True
            if event.key == pygame.K_RIGHT:
                fish.moving_right = True
            if event.key == pygame.K_LEFT:
                fish.moving_left = True
        if event.type == pygame.KEYUP:
            fish.moving_up = False
            fish.moving_down = False
            fish.moving_right = False
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