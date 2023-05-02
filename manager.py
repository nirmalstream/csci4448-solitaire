import pygame
import os
from constants import *
import random
from board import *
from simpleCardFactory import *


pygame.init()
my_path = os.path.dirname(os.path.realpath(__file__))
print(my_path)
screen_width = WIDTH
screen_height = HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solitaire")

s = simpleCardFactory()
deck = s.createDeck()
b = Board(deck)
suits = ['hearts', 'diamonds', 'clubs', 'spades']

print (b.tableau)
def draw_card(card, x, y):
    if card.face == False:
        img = pygame.transform.scale(pygame.image.load(my_path+f'/cardPics/{str(card.value)}_of_{card.suite}.png'),CARD_DIM)
    else:
        c=""
        if card.value == 1:
            c = "ace"
        elif card.value == 11:
            c = "jack"
        elif card.value == 12:
            c = "queen"
        else:
            c = "king"
        img = pygame.transform.scale(pygame.image.load(my_path+f'/cardPics/{c}_of_{card.suite}.png'),CARD_DIM)

    screen.blit(img, (x, y))

def draw_game(b):
    background_tex = pygame.image.load(my_path+"/background.png")
    screen.blit(background_tex, (0,0))
    for i in range(1,len(b.tableau.slots)+1):
        for j in range(len(b.tableau.slots[i])):
            if j == len(b.tableau.slots[i]) - 1:
                draw_card(b.tableau.slots[i][j], i * 120 + 100, j * 30 + 50)
            else:
                img = pygame.transform.scale(pygame.image.load(my_path+'/cardPics/card_back.jpg'),CARD_DIM)
                screen.blit(img, (i * 120 + 100, j * 30 + 50))

    if len(b.foundation.slot1) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(0) * 100 + 500, 50)
    if len(b.foundation.slot2) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(1) * 100 + 500, 50)
    if len(b.foundation.slot3) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(2) * 100 + 500, 50)
    if len(b.foundation.slot4) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(3) * 100 + 500, 50)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    draw_game(b)
    pygame.display.flip()
pygame.quit()
