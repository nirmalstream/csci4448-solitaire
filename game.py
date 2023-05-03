import board
import scoreTable
import pygame
import os
from constants import *
import random
from board import *
from simpleCardFactory import *

class Game:

    def __init__(self):
        deck = simpleCardFactory().createDeck()
        self.board = board.Board(deck)
        self.score_table = scoreTable.ScoreTable()

        self.my_path = os.path.dirname(os.path.realpath(__file__))

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.init()
        pygame.display.set_caption("Solitaire")

        self.event = None

        self.drag = False
        self.drag_size = 0
        self.mouse_down = False
        self.mouse_up = False
        self.start_drag_pos = None
        self.end_drag_pos = None




    def draw_card(self, card, x, y):
        if card != None:
            if card.face == False:
                img = pygame.transform.scale(pygame.image.load(self.my_path+f'/cardPics/{str(card.value)}_of_{card.suite}.png'),CARD_DIM)
            else:
                c=""
                if card.value == 1:
                    c = "ace"
                elif card.value == 11:
                    c = "jack"
                elif card.value == 12:
                    c = "queen"
                elif card.value == 13:
                    c = "king"
                else:
                    # error
                    print("error")
                img = pygame.transform.scale(pygame.image.load(self.my_path+f'/cardPics/{c}_of_{card.suite}.png'),CARD_DIM)
        else:
            img = pygame.transform.scale(pygame.image.load(self.my_path+'/cardPics/empty_holder.png'),CARD_DIM)

        self.screen.blit(img, (x, y))


    def draw_game(self):
        self.screen.fill((255, 0, 0))

        for i in range(1,len(self.board.tableau.slots)+1):
            for j in range(len(self.board.tableau.slots[i])):
                if j == len(self.board.tableau.slots[i]) - 1:
                    self.draw_card(self.board.tableau.slots[i][j], i * 120 + 100, j * 30 + 250)
                else:
                    img = pygame.transform.scale(pygame.image.load(self.my_path+'/cardPics/card_back.jpg'),CARD_DIM)
                    self.screen.blit(img, (i * 120 + 100, j * 30 + 250))

        # draw the stock
        img = pygame.transform.scale(pygame.image.load(self.my_path+'/cardPics/card_back.jpg'),CARD_DIM)
        self.screen.blit(img, (100, 50))

        # now draw the last flipped cards
        # get the card to draw from flipped_cards
        if len(self.board.stock.flipped_cards) > 0:
            self.draw_card(self.board.stock.flipped_cards[-1], 110 + CARD_DIM[0] , 50)

        # draw the foundation
        for i in range(0,4):
            if self.board.foundation.slots[i] == []:
                self.draw_card(None, i * 120 + 500, 50)
            else:
                self.draw_card(self.board.foundation.slots[i][-1], i * 120 + 500, 50)



        pygame.display.flip()




    def check_mouse(self):
        # check mouse click
        if self.event != None:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
                self.start_drag_pos = pygame.mouse.get_pos()

            # check drag
            if self.event.type == pygame.MOUSEMOTION:
                self.drag = True
                self.drag_size += 1

            # check mouse release
            if self.event.type == pygame.MOUSEBUTTONUP:
                self.mouse_up = True
                self.end_drag_pos = pygame.mouse.get_pos()

            if self.mouse_down and self.mouse_up:
                if(self.drag == False or self.drag_size < 20):
                    self.handle_mouse_click(pygame.mouse.get_pos())
                else:
                    self.handle_mouse_drag()

                self.mouse_down = False
                self.mouse_up = False
                self.drag = False
                self.drag_size = 0
                self.start_drag_pos = None
                self.end_drag_pos = None







    def handle_mouse_drag(self):
        # check if start drag position is on the flipped cards of the stock
        if self.start_drag_pos[0] > 110 + CARD_DIM[0] and self.start_drag_pos[0] < 110 + CARD_DIM[0] + CARD_DIM[0] and self.start_drag_pos[1] > 50 and self.start_drag_pos[1] < 50 + CARD_DIM[1]:
            # check if end drag position is on the tableau
            if self.end_drag_pos[0] > 220 and self.end_drag_pos[0] < 1040 and self.end_drag_pos[1] > 250 and self.end_drag_pos[1] < 650:
                # get the card from the stock
                card = self.board.stock.get_flipped_cards()
                self.board.stock.get_card()
                # get the slot to move to
                slot = int((self.end_drag_pos[0] - 100) / 120)
                # add the card to the tableau
                self.board.tableau.add_card(card, slot)
            # check if end drag position is on the foundation
            elif self.end_drag_pos[0] > 500 and self.end_drag_pos[0] < 960 and self.end_drag_pos[1] > 50 and self.end_drag_pos[1] < 50 + CARD_DIM[1]:
                # get the card from the stock
                card = self.board.stock.get_flipped_cards()
                self.board.stock.get_card()
                # get the slot to move to
                slot = int((self.end_drag_pos[0] - 500) / 120)
                # add the card to the foundation
                self.board.foundation.add_card(card, slot)

        # check if start drag position is on the tableau
        elif self.start_drag_pos[0] > 220 and self.start_drag_pos[0] < 1040 and self.start_drag_pos[1] > 250 and self.start_drag_pos[1] < 650:
            # check if end drag is the foundation
            if self.end_drag_pos[0] > 500 and self.end_drag_pos[0] < 960 and self.end_drag_pos[1] > 50 and self.end_drag_pos[1] < 50 + CARD_DIM[1]:
                # get the card from the tableau
                slot_from = int((self.start_drag_pos[0] - 100) / 120)
                slot_to = int((self.end_drag_pos[0] - 500) / 120)
                card = self.board.tableau.remove_ending_card(slot_from)
                # add the card to the foundation
                self.board.foundation.add_card(card, slot_to)

        # check if start drag position is on the foundation
        elif self.start_drag_pos[0] > 500 and self.start_drag_pos[0] < 960 and self.start_drag_pos[1] > 50 and self.start_drag_pos[1] < 50 + CARD_DIM[1]:
            # check if end drag is the tableau
            if self.end_drag_pos[0] > 220 and self.end_drag_pos[0] < 1040 and self.end_drag_pos[1] > 250 and self.end_drag_pos[1] < 650:
                # get the card from the foundation
                slot_from = int((self.start_drag_pos[0] - 500) / 120)
                slot_to = int((self.end_drag_pos[0] - 100) / 120)
                card = self.board.foundation.remove_ending_card(slot_from)
                # add the card to the tableau
                self.board.tableau.add_card(card, slot_to)

    def handle_mouse_click(self, pos):
        print(pos)
        # for i in range(1,len(self.board.tableau.slots)+1):
        #     for j in range(len(self.board.tableau.slots[i])):
        #         if j == len(self.board.tableau.slots[i]) - 1:
        #             if pos[0] > i * 120 + 100 and pos[0] < i * 120 + 100 + CARD_DIM[0] and pos[1] > j * 30 + 250 and pos[1] < j * 30 + 250 + CARD_DIM[1]:
        #                 self.board.tableau.slots[i][j].face = True


        # handle mouse click for deck

        if(pos[0] > 100 and pos[0] < 100 + CARD_DIM[0] and pos[1] > 50 and pos[1] < 50 + CARD_DIM[1]):
            print("clicked on deck")
            self.board.stock.get_card()



        # handle mouse click for 4 foundation slots

        # if(pos[0] > 500 and pos[0] < 860 + CARD_DIM[0] and pos[1] > 50 and pos[1] < 50 + CARD_DIM[1]):
        #     print("clicked on foundation")







    def run(self):
        running = True
        while running:
            self.draw_game()
            # update event
            self.event = pygame.event.poll()

            # check for mouse click
            self.check_mouse()

            # check for quit
            if self.event.type == pygame.QUIT:
                running = False
                self.quit()




    def quit(self):
        pygame.quit()


game = Game()
game.run()
