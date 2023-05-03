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
stock_cards = [0]
suits = ['hearts', 'diamonds', 'clubs', 'spades']

#print (b.tableau)
def draw_card(card, x, y):
    if card != None:
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
    else:
        img = pygame.transform.scale(pygame.image.load(my_path+'/cardPics/empty_holder.png'),CARD_DIM)

    screen.blit(img, (x, y))

def draw_game(b,deck, event, stock_cards):
    # size 52

    #background_tex = pygame.image.load(my_path+"/background.png")
    #screen.blit(background_tex, (0,0))
    for i in range(1,len(b.tableau.slots)+1):
        for j in range(len(b.tableau.slots[i])):
            if j == len(b.tableau.slots[i]) - 1:
                draw_card(b.tableau.slots[i][j], i * 120 + 100, j * 30 + 250)
            else:
                img = pygame.transform.scale(pygame.image.load(my_path+'/cardPics/card_back.jpg'),CARD_DIM)
                screen.blit(img, (i * 120 + 100, j * 30 + 250))

    if len(b.foundation.slot1) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(0) * 120 + 500, 50)
    else :
        draw_card(None, 0 * 120 + 500, 50)
    if len(b.foundation.slot2) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(1) * 120 + 500, 50)
    else :
        draw_card(None, 1 * 120 + 500, 50)
    if len(b.foundation.slot3) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(2) * 120 + 500, 50)
    else :
        draw_card(None, 2 * 120 + 500, 50)
    if len(b.foundation.slot4) > 0:
        draw_card(b.foundation.slot1[-1], suits.index(3) * 120 + 500, 50)
    else :
        draw_card(None, 3 * 120 + 500, 50)

    img = pygame.transform.scale(pygame.image.load(my_path+'/cardPics/card_back.jpg'),CARD_DIM)
    screen.blit(img, (100, 50))
    # for i in range(3):
    #     d_card = deck.pop(0)
    #     draw_card(d_card, i*30 + 200,50)

        # check event here
    if(event.type == pygame.MOUSEBUTTONDOWN):
        card = handle_mouse_click(event.pos, b, deck)
        stock_cards[0] = card

    if(stock_cards[0] != 0):
        draw_card(stock_cards[0], 110 + CARD_DIM[0], 50)


def handle_mouse_click(pos, b, deck):
    print(pos)
    for i in range(1,len(b.tableau.slots)+1):
        for j in range(len(b.tableau.slots[i])):
            if j == len(b.tableau.slots[i]) - 1:
                if pos[0] > i * 120 + 100 and pos[0] < i * 120 + 100 + CARD_DIM[0] and pos[1] > j * 30 + 250 and pos[1] < j * 30 + 250 + CARD_DIM[1]:
                    print("clicked on card")
                    b.tableau.slots[i][j].face = True
                    print(b.tableau.slots[i][j].face)
                    print(b.tableau.slots[i][j].suite)
                    print(b.tableau.slots[i][j].value)
                    print(b.tableau.slots[i][j].face)

    # handle mouse click for deck

    if(pos[0] > 100 and pos[0] < 100 + CARD_DIM[0] and pos[1] > 50 and pos[1] < 50 + CARD_DIM[1]):
        print("clicked on deck")
        d_card = deck[0]
        return d_card


    # handle mouse click for 4 foundation slots
    
    if(pos[0] > 500 and pos[0] < 860 + CARD_DIM[0] and pos[1] > 50 and pos[1] < 50 + CARD_DIM[1]):
        print("clicked on foundation")

    




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 0, 0))
    draw_game(b,deck, event, stock_cards)
    pygame.display.flip()


pygame.quit()
