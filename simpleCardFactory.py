import card.py
import numpy as np

class simpleCardFactory:
    def __init__(self):

    def create(self, suite, val):
        if suite == "hearts":
            return hearts(val = val)
        elif suite == "clubs":
            return clubs(val = val)
        elif suite == "diamonds":
            return diamonds(val = val)
        elif suite == "spades":
            return spades(val = val)
