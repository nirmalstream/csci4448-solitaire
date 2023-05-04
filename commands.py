from abc import ABC, abstractmethod

# COMMAND PATTERN
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass




class MoveCard(Command):
    def __init__(self, board, source, dest, card, slot_from = None, slot_to = None):
        self.board = board
        self.source = source
        self.dest = dest
        self.card = card
        self.slot_from = slot_from
        self.slot_to = slot_to


    def execute(self):
        self.board.move_card(self.source, self.dest, self.card, self.slot_from, self.slot_to)


class EndGame(Command):
    def __init__(self, board):
        self.board = board

    def execute(self):
        self.board.end_game()

class ResetGame(Command):
    def __init__(self, board):
        self.board = board

    def execute(self):
        self.board.reset_game()