import pygame
import sys
import settings
import time
from pygame import mixer
from fish import Fish
from obsticale import Obsticale
from powerup import PowerUp
from timer import Timer
from button import Button


pygame.init()
mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
settings.SCREEN_WIDTH = screen.get_rect().width
settings.SCREEN_HEIGHT = screen.get_rect().height

# Making a Play function
def play():
    pygame.display.set_caption("Flappy Fish")

    water_full = pygame.image.load("images/water_full.png")
    water_full_rect = water_full.get_rect()
    sand_full = pygame.image.load("images/kenney_fishpack/PNG/Default size/fishTile_001.png")
    sand_full_rect = sand_full.get_rect()
    # Building a background
    background = pygame.surface.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    background.fill((120, 181, 250))
    for y in range(settings.SCREEN_WIDTH // settings.TILE_SIZE):
        for x in range(settings.SCREEN_WIDTH // settings.TILE_SIZE):
            background.blit(water_full, (x * water_full_rect.width, y * water_full_rect.height))
            background.blit(sand_full, (x * sand_full_rect.width, settings.SCREEN_HEIGHT - settings.TILE_SIZE))

    # Creating Sprite Groups
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

    power_ups = pygame.sprite.Group(PowerUp((settings.SCREEN_WIDTH + 500, 200)),
                                    PowerUp((settings.SCREEN_WIDTH + 3100, 800)),
                                    PowerUp((settings.SCREEN_WIDTH + 6500, 400)),
                                    PowerUp((settings.SCREEN_WIDTH + 10000, 560)),
                                    PowerUp((settings.SCREEN_WIDTH + 13000, 740)))

    # music
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
        if fish.update(obsticales, power_ups) == False:
            game_over = True
            pygame.mouse.set_visible(True)
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
        # flip display
        pygame.display.flip()

# Making an Instructions page
def instructions():
    pygame.display.set_caption("Instructions")

    while True:
        screen.fill((128, 242, 255))
        mixer.music.load("sounds/kenney_interfacesounds/Audio/select_001.ogg")
        mixer.music.set_volume(0.3)
        font1 = pygame.font.SysFont("arialblack", 40)
        font2 = pygame.font.SysFont("cooperblack", 80)
        font3 = pygame.font.SysFont("arialblack", 35)
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = font2.render("INSTRUCTIONS", True, (196, 158, 71))
        menu_rect = menu_text.get_rect(center=(settings.SCREEN_WIDTH / 2, 100))
        back_button = Button(None, pos=(settings.SCREEN_WIDTH / 13, 100), text_input="< BACK", font=font1, base_color=(0, 0, 0))
        # defining instructions' text
        instructions_text1 = font3.render("* AVOID ONCOMING OBSTACLES!", True, (0, 0, 0))
        instructions_text2 = font3.render("use the arrow keys to move forward, backward, up, and down", True, (0, 0, 0))
        instructions_text3 = font3.render("* COLLECT POWER-UPS!", True, (0, 0, 0))
        instructions_text4 = font3.render("collect the power-ups to increase your swim speed", True, (0, 0, 0))
        instructions_text5 = font3.render("* SWIM AS LONG AS YOU CAN!", True, (0, 0, 0))
        instructions_text6 = font3.render("swim as long as you can before you get pushed too far", True, (0, 0, 0))
        instructions_rect1 = instructions_text1.get_rect(center=(settings.SCREEN_WIDTH / 2, 250))
        instructions_rect2 = instructions_text2.get_rect(center=(settings.SCREEN_WIDTH / 2, 325))
        instructions_rect3 = instructions_text3.get_rect(center=(settings.SCREEN_WIDTH / 2, 500))
        instructions_rect4 = instructions_text4.get_rect(center=(settings.SCREEN_WIDTH / 2, 575))
        instructions_rect5 = instructions_text5.get_rect(center=(settings.SCREEN_WIDTH / 2, 750))
        instructions_rect6 = instructions_text6.get_rect(center=(settings.SCREEN_WIDTH / 2, 825))
        # draw instructions
        screen.blit(menu_text, menu_rect)
        screen.blit(instructions_text1, instructions_rect1)
        screen.blit(instructions_text2, instructions_rect2)
        screen.blit(instructions_text3, instructions_rect3)
        screen.blit(instructions_text4, instructions_rect4)
        screen.blit(instructions_text5, instructions_rect5)
        screen.blit(instructions_text6, instructions_rect6)
        back_button.update(screen)
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(menu_mouse_pos):
                    mixer.music.play()
                    time.sleep(.3)
                    main_menu()

        pygame.display.flip()

# Making a Main Menu
def main_menu():
    pygame.display.set_caption("Main Menu")

    while True:
        screen.fill((128, 242, 255))
        font1 = pygame.font.SysFont("showcardgothic", 100)
        font2 = pygame.font.SysFont("cooperblack", 75)
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = font1.render("FLAPPY FISH", True, (196, 158, 71))
        menu_rect = menu_text.get_rect(center=(settings.SCREEN_WIDTH / 2, 150))
        # creating buttons
        play_button = Button(None, pos=(settings.SCREEN_WIDTH / 2, 300), text_input="PLAY", font=font2,
                             base_color=(0, 0, 0))
        instructions_button = Button(None, pos=(settings.SCREEN_WIDTH / 2, 500), text_input="INSTRUCTIONS", font=font2,
                                base_color=(0, 0, 0))
        quit_button = Button(None, pos=(settings.SCREEN_WIDTH / 2, 700), text_input="QUIT", font=font2,
                             base_color=(0, 0, 0))

        screen.blit(menu_text, menu_rect)
        # a sound for mouse clicks
        mixer.music.load("sounds/kenney_interfacesounds/Audio/select_001.ogg")
        mixer.music.set_volume(0.3)

        for button in [play_button, instructions_button, quit_button]:
            button.update(screen)
        # check to see what button was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_input(menu_mouse_pos):
                    mixer.music.play()
                    pygame.mouse.set_visible(False)
                    time.sleep(.3)
                    play()
                if instructions_button.check_input(menu_mouse_pos):
                    mixer.music.play()
                    time.sleep(.3)
                    instructions()
                if quit_button.check_input(menu_mouse_pos):
                    mixer.music.play()
                    sys.exit()
        pygame.display.update()

# calling main menu function
main_menu()