import pygame
import sys

pygame.init()

TILE_SIZE = 64

screen = pygame.display.set_mode((20*TILE_SIZE, 10*TILE_SIZE))
grass = pygame.image.load("images/Default/roadTexture_25.png")
grass_rect = grass.get_rect()
water_top = pygame.image.load("images/water_tile.png")
water_top_rect = water_top.get_rect()
water_full = pygame.image.load("image")

screen_rect = screen.get_rect()

num_tiles = screen_rect.width // water_top_rect.width
for y in range(num_tiles):
    for x in range(num_tiles):
        screen.blit(water_top, (x*water_top_rect.width, 64))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

