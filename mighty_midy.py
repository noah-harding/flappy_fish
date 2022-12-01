import pygame
from sea_floor import SeaFloor
import sys
from fish import Fish
from random import randint
from pygame import mixer
import settings
from obsticales import Obsticales
from health import Health

pygame.init()


screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
screen_rect = screen.get_rect()

water_top = pygame.image.load("images/water_tile.png")
water_top_rect = water_top.get_rect()
water_full = pygame.image.load("images/water_full.png")
water_full_rect = water_full.get_rect()
sand_full = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_001.png")
sand_full_rect = sand_full.get_rect()


obsticle = Obsticales()
health_item = Health()
# def hit_obsticle():
#     collision_range = 10
#     if obsticle.rect.colliderect(fish.rect):
#         if abs(fish.rect.top - obsticle.rect.bottom) < collision_range:
#             fish.moving_up = False
#             print("collide")
#             return True
#         if abs(fish.rect.bottom - obsticle.rect.top) < collision_range:
#             fish.moving_down = False
#             print("collide")
#             return True
#         if abs(fish.rect.right - obsticle.rect.left) < collision_range:
#             fish.moving_up = False
#             fish.moving_down = False
#             print("collide")
#             return True
#     else:
#         return False


fish = Fish(screen)

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

clock = pygame.time.Clock()
while True:

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
        if event.type == pygame.QUIT:
            sys.exit()

    fish.update(obsticle)
    obsticle.update()
    health_item.update()
    screen.blit(background, (0, 0))
    fish.blitme()
    obsticle.draw_obsticle(screen)
    health_item.draw_health_item(screen)
    pygame.display.flip()
    clock.tick(60)