import pygame
import sys

pygame.init()

TILE_SIZE = 64

screen = pygame.display.set_mode((10*TILE_SIZE, 10*TILE_SIZE))
grass = pygame.image.load("images/Default/roadTexture_25.png")
grass_rect = grass.get_rect()
screen_rect = screen.get_rect()

num_tiles = screen_rect.width // grass_rect.width
for y in range(num_tiles):
    for x in range(num_tiles):
        screen.blit(grass, (x*grass_rect.width, y*grass_rect.height))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

