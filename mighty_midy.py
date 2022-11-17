import pygame
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
sand_convex = pygame.image.load("images/fishTile_025.png")
sand_convex_rect = sand_convex.get_rect()
sand_concave = pygame.image.load("images/fishTile_024.png")
sand_concave_rect = sand_concave.get_rect()

dead_fish = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_099.png")
dead_fish_rect = dead_fish.get_rect()
green_seaweed = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_028.png")
green_seaweed_rect = green_seaweed.get_rect()
purple_seaweed = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_017.png")
purple_seaweed_rect = purple_seaweed.get_rect()
rock = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_084.png")
rock_rect = rock.get_rect()


num_tiles = screen_rect.width // water_top_rect.width
fish = Fish(screen)

#for x in range(num_tiles):   Attempt to simplify the blit process
    #for y in range():
        #screen.blit(water_full, (x*water_full_rect.width, y*water_full_rect.height))


#screen.blit(main_fish, (main_fish_rect))


while True:
    for event in pygame.event.get():
        if event.type == pygame.K_UP:
            fish.moving_up = True
            print("moving up")
        if event.type == pygame.K_DOWN:
            fish.moving_down = True
        if event.type == pygame.QUIT:
            sys.exit()

    fish.update()
    
    screen.fill((120, 181, 250))
    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(water_top, (x * water_top_rect.width, 64))
            screen.blit(water_full, (x * water_full_rect.width, y * water_full_rect.height + 128))
            screen.blit(sand_full, (x * sand_full_rect.width, 896))
            screen.blit(sand_convex, (64, 832))
            screen.blit(sand_convex, (192, 832))
            screen.blit(sand_convex, (320, 832))
            screen.blit(sand_convex, (448, 832))
            screen.blit(sand_convex, (576, 832))
            screen.blit(sand_convex, (704, 832))
            screen.blit(sand_convex, (832, 832))
            screen.blit(sand_convex, (960, 832))
            screen.blit(sand_convex, (1088, 832))
            screen.blit(sand_convex, (1216, 832))
            screen.blit(sand_convex, (1344, 832))
            screen.blit(sand_convex, (1472, 832))
            screen.blit(sand_concave, (0, 832))
            screen.blit(sand_concave, (128, 832))
            screen.blit(sand_concave, (256, 832))
            screen.blit(sand_concave, (384, 832))
            screen.blit(sand_concave, (512, 832))
            screen.blit(sand_concave, (640, 832))
            screen.blit(sand_concave, (768, 832))
            screen.blit(sand_concave, (896, 832))
            screen.blit(sand_concave, (1024, 832))
            screen.blit(sand_concave, (1152, 832))
            screen.blit(sand_concave, (1280, 832))
            screen.blit(sand_concave, (1408, 832))
            screen.blit(sand_concave, (1536, 832))
            screen.blit(green_seaweed, (128, 777))
            screen.blit(green_seaweed, (1088, 771))
            screen.blit(purple_seaweed, (512, 777))
            screen.blit(dead_fish, (756, 850))
            screen.blit(rock, (5, 777))
            screen.blit(rock, (1408, 777))

    fish.blitme()
    pygame.display.flip()