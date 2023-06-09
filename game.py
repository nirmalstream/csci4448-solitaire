import board
import scoreTable
import pygame
import os
from constants import *
import random
from board import *
from simpleCardFactory import *

# SINGLETON CLASS
class Game:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Game.__instance == None:
            Game()
        return Game.__instance
    

    def __init__(self):
        deck = simpleCardFactory().createDeck()
        self.board = board.Board(deck)

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
        self.game_done = False

        self.draw_score_table = False

    def check_game_over(self):
        count = 0
        for i in self.board.foundation.slots:
            if len(i)==14:
                count+=1
        if count == 4:
            self.game_done = True

    def get_game_done(self):
        return self.game_done
        self.draw_score_table = False
    
    def draw_score(self):
        # draw the score table

        # get scores from csv
        score_list = self.board.score_table.getScores()

        # sort scores
        sorted_score_list = sorted(score_list.items(), key=lambda x: x[1], reverse=True)

        # draw the score table
        pygame.draw.rect(self.screen, (0, 0, 0), (50, 500, 200, 200))

        # draw the scores
        font = pygame.font.SysFont('Arial', 20)
        for i in range(len(sorted_score_list)):
            name, score = sorted_score_list[i]
            text = font.render(name + ": " + str(score), True, (255, 255, 255))
            self.screen.blit(text, (50, 500 + 20 * i))

        


    def draw_card(self, card, x, y):
        if card != None:
            # normal card
            if card.face == False:
                if card.face_up:
                    img = pygame.transform.scale(pygame.image.load(self.my_path+f'/cardPics/{str(card.value)}_of_{card.suite}.png'),CARD_DIM)
                else:
                    img = pygame.transform.scale(pygame.image.load(self.my_path+'/cardPics/card_back.jpg'),CARD_DIM)

            # jack, queen, king, ace
            else:
                if card.face_up:
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
                    # card is face down
                    img = pygame.transform.scale(pygame.image.load(self.my_path+'/cardPics/card_back.jpg'),CARD_DIM)

        else:
            img = pygame.transform.scale(pygame.image.load(self.my_path+'/cardPics/empty_holder.png'),CARD_DIM)

        self.screen.blit(img, (x, y))


    def draw_game(self):
        self.screen.fill((255, 0, 0))

        if self.draw_score_table:
            self.draw_score()

        # quit game button to save score
        pygame.draw.rect(self.screen, (0, 0, 0), (WIDTH - 100, 0, 100, 50))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render("Quit", True, (255, 255, 255))
        self.screen.blit(text, (WIDTH - 100, 0))

        # button to show the score table   
        pygame.draw.rect(self.screen, (0, 0, 0), (WIDTH - 100, 50, 100, 50))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render("Score", True, (255, 255, 255))
        self.screen.blit(text, (WIDTH - 100, 50))


        # draw tableau
        for i in range(1,len(self.board.tableau.slots)+1):
            for j in range(len(self.board.tableau.slots[i])):
                    self.draw_card(self.board.tableau.slots[i][j], i * 120 + 100, j * 30 + 250)
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
                card = self.board.stock.get_dragged_card()
                # get the slot to move to
                slot = int((self.end_drag_pos[0] - 100) / 120)
                # check valid move
                if (self.board.tableau.check_valid_move(slot,card)):
                    print("True")
                    # get the card from the stock
                    card = self.board.stock.get_flipped_cards()
                    self.board.stock.get_card()
                    # add the card to the tableau
                    self.board.tableau.add_card(card, slot)
                else:
                    print(False)
            # check if end drag position is on the foundation
            elif self.end_drag_pos[0] > 500 and self.end_drag_pos[0] < 960 and self.end_drag_pos[1] > 50 and self.end_drag_pos[1] < 50 + CARD_DIM[1]:
                # get the card from the stock
                card = self.board.stock.get_dragged_card()
                # get the slot to move to
                slot = int((self.end_drag_pos[0] - 500) / 120)
                # check valid move
                if (self.board.foundation.check_valid_move(slot,card)):
                    print("True")
                    # get the card from the stock
                    card = self.board.stock.get_flipped_cards()
                    self.board.stock.get_card()
                    # add the card to the foundation
                    self.board.foundation.add_card(card, slot)
                else:
                    print(False)

        # check if start drag position is on the tableau
        elif self.start_drag_pos[0] > 220 and self.start_drag_pos[0] < 1040 and self.start_drag_pos[1] > 250 and self.start_drag_pos[1] < 650:
            # check if end drag is the foundation
            if self.end_drag_pos[0] > 500 and self.end_drag_pos[0] < 960 and self.end_drag_pos[1] > 50 and self.end_drag_pos[1] < 50 + CARD_DIM[1]:
                # get the card from the tableau
                slot_from = int((self.start_drag_pos[0] - 100) / 120)
                card = self.board.tableau.get_bottom_card(slot_from)
                slot_to = int((self.end_drag_pos[0] - 500) / 120)
                # check valid move
                if (self.board.foundation.check_valid_move(slot_to,card)):
                    print(True)
                    card = self.board.tableau.remove_ending_card(slot_from)
                    # add the card to the foundation
                    self.board.foundation.add_card(card, slot_to)
                else:
                    print(False)

            # check what card the the end drag is on in the tableau
            elif self.end_drag_pos[0] > 220 and self.end_drag_pos[0] < 1040 and self.end_drag_pos[1] > 250 and self.end_drag_pos[1] < 650:
                # get the card from the tableau
                slot_from = int((self.start_drag_pos[0] - 100) / 120)
                slot_to = int((self.end_drag_pos[0] - 100) / 120)
                # get the card that is clicked on the tableau
                # get the num of cards in slot_from
                num_cards = len(self.board.tableau.slots[slot_from])
                # check to see if the last card is clicked
                if self.start_drag_pos[1] > 250 + (num_cards - 1) * 30:
                    #get card
                    card = self.board.tableau.get_bottom_card(slot_from)
                    # check valid move
                    if (self.board.tableau.check_valid_move(slot_to,card)):
                        print(True)
                        # move last card
                        card = self.board.tableau.remove_ending_card(slot_from)
                        self.board.tableau.add_card(card, slot_to)
                    else:
                        print(False)

                else:
                    # get the card that is clicked
                    index = int((self.start_drag_pos[1] - 250) / 30)

                    # get the card
                    card = self.board.tableau.slots[slot_from][index]

                    # check that the card is face up
                    if card.face_up == False:
                        return
                    # check if valid move
                    if (self.board.tableau.check_valid_move(slot_to,card)):
                        print(True)
                        #move card
                        self.board.tableau.move_card(card, slot_from, slot_to)
                    else:
                        print(False)

        # check if start drag position is on the foundation
        elif self.start_drag_pos[0] > 500 and self.start_drag_pos[0] < 960 and self.start_drag_pos[1] > 50 and self.start_drag_pos[1] < 50 + CARD_DIM[1]:
            # check if end drag is the tableau
            if self.end_drag_pos[0] > 220 and self.end_drag_pos[0] < 1040 and self.end_drag_pos[1] > 250 and self.end_drag_pos[1] < 650:
                # get the card from the foundation
                slot_from = int((self.start_drag_pos[0] - 500) / 120)
                slot_to = int((self.end_drag_pos[0] - 100) / 120)
                card = self.board.foundation.get_displayed_card(slot_from)
                # check valid move
                if (self.board.tableau.check_valid_move(slot_to,card)):
                    print(True)
                    card = self.board.foundation.remove_ending_card(slot_from)
                    # add the card to the tableau
                    self.board.tableau.add_card(card, slot_to)
                else:
                    print(False)

    def handle_mouse_click(self, pos):
        print(pos)
        # handle mouse click for deck

        if(pos[0] > 100 and pos[0] < 100 + CARD_DIM[0] and pos[1] > 50 and pos[1] < 50 + CARD_DIM[1]):
            self.board.stock.get_card()

        # handle mouse click for quit button
        if(pos[0] > 1100 and pos[0] < 1200 and pos[1] > 0 and pos[1] < 50):

            self.board.save_score(self.get_user_name())
            self.quit()

        # handle mouse click for score
        if(pos[0] > 1100 and pos[0] < 1200 and pos[1] > 50 and pos[1] < 100):
            # flip draw_score_table
            if self.draw_score_table:
                self.draw_score_table = False
            else:
                self.draw_score_table = True


    def get_user_name(self):
        # get user name
        user_name = input("Enter your name: ")
        return user_name
    

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
