import pygame
import time
import sys
import random
import requests
import config
import keyboard
import map_generation

pygame.init()

num_tiles = []
num_tiles.append(int(input('Введите размер тайлов: ')))
tile_size = num_tiles[0]
num_tiles[0] = int(round(pygame.display.Info().current_w/tile_size))
num_tiles.append(int(round(pygame.display.Info().current_h/tile_size)))
print('генерация началась')
map = map_generation.generate(num_tiles)
print('генерация закончилась')

tile1 = pygame.image.load("sprites/tiles/tile1.png")
tile1 = pygame.transform.scale(tile1, (tile_size, tile_size))
tile2 = pygame.image.load("sprites/tiles/tile2.png")
tile2 = pygame.transform.scale(tile2, (tile_size, tile_size))
tile3 = pygame.image.load("sprites/tiles/tile3.png")
tile3 = pygame.transform.scale(tile3, (tile_size, tile_size))

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm Game on Python")

pygame.mixer.music.load("sounds/background_sound.mp3")
pygame.mixer.music.play(-1)
def exit(reason):
    print(f'Выход.\nПричина выхода: {reason}.')
    sys.exit()

map_ready = False

running = True
while running:
    if not map_ready:
        map_ready = True
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    otst1 = 0
    for x in range(len(map)):
        otst2 = 0
        for y in range(len(map[x])):
            if map[x][y] == 0:
                screen.blit(tile1, (otst1, otst2))
            elif map[x][y] == 2:
                screen.blit(tile2, (otst1, otst2))
            else:
                screen.blit(tile3, (otst1, otst2))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    exit('user escape')
            otst2 += tile_size
        otst1 += tile_size
    pygame.display.flip()
pygame.quit()