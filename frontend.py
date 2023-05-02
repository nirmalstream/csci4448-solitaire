import pygame
import os
from constants import *
import random
import foundation
import board
import tableau
import simpleCardFactory

pygame.init()
my_path = os.path.dirname(os.path.realpath(__file__))
print(my_path)
screen_width = WIDTH
screen_height = HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solitaire")
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
deck = [(suit, rank) for suit in suits for rank in ranks]
random.shuffle(deck)
tableau = [[] for _ in range(7)]
foundation = {suit: [] for suit in suits}
for i in range(len(tableau)):
    for j in range(i, len(tableau)):
        tableau[j].append(deck.pop(0))

def draw_card(card, x, y):
    img = pygame.transform.scale(pygame.image.load(my_path+f'/cardPics/{card[1]}_of_{card[0]}.png'),CARD_SMALL_ITEM_SIZE)
    screen.blit(img, (x, y))

def draw_game():
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if j == len(tableau[i]) - 1:
                draw_card(tableau[i][j], i * 100 + 50, j * 30 + 50)
            else:
                img = pygame.transform.scale(pygame.image.load(my_path+'/cardPics/card_back.jpg'),CARD_SMALL_ITEM_SIZE)
                screen.blit(img, (i * 100 + 50, j * 30 + 50))
    for suit in suits:
        if len(foundation[suit]) > 0:
            draw_card(foundation[suit][-1], suits.index(suit) * 100 + 500, 50)

background_tex = pygame.image.load(my_path+"/background.png")
screen.blit(background_tex, (0,0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    draw_game()
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
