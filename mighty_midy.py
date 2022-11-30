import pygame
from sea_floor import SeaFloor
import sys
from fish import Fish
from random import randint

pygame.init()

TILE_SIZE = 64

screen = pygame.display.set_mode((25*TILE_SIZE, 15*TILE_SIZE))
screen_rect = screen.get_rect()

water_top = pygame.image.load("images/water_tile.png")
water_top_rect = water_top.get_rect()
water_full = pygame.image.load("images/water_full.png")
water_full_rect = water_full.get_rect()
sand_full = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_001.png")
sand_full_rect = sand_full.get_rect()
obsticle = pygame.image.load("images/kenney_simplifiedplatformer/PNG/Tiles/platformPack_tile016.png")
obsticle_rect = obsticle.get_rect()
#sea_floor = SeaFloor(screen_rect.width)


num_tiles = screen_rect.width // water_top_rect.width
fish = Fish(screen)

background = pygame.surface.Surface((screen_rect.width, screen_rect.height))
background.fill((120, 181, 250))
for y in range(num_tiles):
    for x in range(num_tiles):
        background.blit(water_full, (x * water_full_rect.width, y * water_full_rect.height))
        background.blit(sand_full, (x * sand_full_rect.width, 896))

obsticle_size = randint(1, 13)
x_offset = obsticle_rect.x
scroll = 0
clock = pygame.time.Clock()
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fish.moving_up = True
            if event.key == pygame.K_DOWN:
                fish.moving_down = True
        if event.type == pygame.KEYUP:
            fish.moving_up = False
            fish.moving_down = False
        if event.type == pygame.QUIT:
            sys.exit()

    fish.update()
    screen.blit(background, (0,0))

    for y in range(num_tiles):
        screen.blit(obsticle, ((25*TILE_SIZE) + scroll, y * (TILE_SIZE * obsticle_size)))
    scroll -= 10
    if abs(scroll) > 25 * TILE_SIZE:
        obsticle_size = randint(1, 3)
        scroll = 0

    fish.blitme()
    pygame.display.flip()
    clock.tick(60)