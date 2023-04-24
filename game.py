import board
import scoreTable
import simpleCardFactory

class Game:

    def __init__(self):
        deck = simpleCardFactory.createDeck()

        self.board = board.Board(deck)
        self.score_table = scoreTable.ScoreTable()


    def deal(self):
        # TODO
        pass



