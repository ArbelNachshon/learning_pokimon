import pygame

pygame.init()

START_PICTURE = pygame.image.load("startbck.png")
GAME_PICTURE = pygame.image.load("background_picture.jpg")
WIDTH = 500
HIGHT = 707

BUTTON_UNPRESSED = (47, 162, 210)
BUTTON_PRESS = (111, 193, 227)
# defining a font
BUTTON_FONT = pygame.font.SysFont("aharoni", 18)
# rendering a text written in
# this font
BUTTON_TXT = BUTTON_FONT.render('START', 1, "white")

POKI_DICT = {
    0: [(180, 546) , pygame.image.load("characterseven-removebg-preview.png")],
1:[(100,440) ,pygame.image.load("charactertwo-removebg-preview.png")],
2: [(115,345), pygame.image.load("chararcterthree-removebg-preview.png")],
3: [(210,300) ,pygame.image.load("characterfour-removebg-preview.png")],
4: [(313,180), pygame.image.load("characterfive-removebg-preview.png")],
5: [(186,120), pygame.image.load("charactersix-removebg-preview.png")],
6: [(180,40), pygame.image.load("characterone.png")]
}
