import os
import pygame as pg
os.chdir('C:/Python Projects/sgv2')

SCREEN_X = 1920
SCREEN_Y = 1080
FPS = 60
CAPTION = "SG V.2"



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
SILVER = (192, 192, 192)
GREY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)
DARKRED = (139, 0, 0)
BROWN = (165, 42, 42)
FIREBRICK = (178, 34, 34)
CRIMSON = (220, 20, 60)
ORANGE = (255, 265, 0)
ORANGERED = (255, 69, 0)
DARKORANGE = (255, 140, 0)
GOLD = (255, 215, 0)
DARKGREEN = (0, 100, 0)
LIGHTGREEN = (144, 238, 144)
DARKSLATEGREY = (47, 79, 79)
TEAL = (0, 128, 128)
STEELBLUE = (70, 130, 180)
MIDNIGHTBLUE = (25, 25, 112)
BLUEVIOLET = (138, 43, 226)
INDIGO = (75, 0, 130)
DARKSLATEBLUE = (72, 61, 139)
DARKMAGENTA = (139, 0, 139)
DARKVIOLET = (148, 0, 211)
SLATEGREY = (112, 128, 144)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.display.set_caption(CAPTION)
WINDOW = pg.display.set_mode((SCREEN_X, SCREEN_Y))




