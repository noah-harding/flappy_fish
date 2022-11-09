import pygame
import sys

pygame.init()

TILE_SIZE = 64

screen = pygame.display.set_mode((25*TILE_SIZE, 15*TILE_SIZE))
grass = pygame.image.load("images/Default/roadTexture_25.png")
grass_rect = grass.get_rect()
water_top = pygame.image.load("images/water_tile.png")
water_top_rect = water_top.get_rect()
water_full = pygame.image.load("images/water_full.png")
water_full_rect = water_full.get_rect()
sand_full = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_001.png")
sand_full_rect = sand_full.get_rect()
sand_convex = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile025.png")
sand_convex_rect = sand_convex.get_rect()

screen_rect = screen.get_rect()

num_tiles = screen_rect.width // water_top_rect.width
screen.fill((56, 129, 245))
for y in range(num_tiles):
    for x in range(num_tiles):
        screen.blit(water_top, (x*water_top_rect.width, 64))
        screen.blit(water_full, (x*water_full_rect.width, y*water_full_rect.height + 128))
        screen.blit(sand_full, (x*sand_full_rect.width, 896))
        screen.blit(sand_convex, ((x*sand_convex_rect)/15, 832)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()