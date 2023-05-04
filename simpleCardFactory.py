import card
import random

# FACTORY PATTERN
class simpleCardFactory:
    def create(self, suite, val):
        if suite == "hearts":
            return card.hearts(val)
        elif suite == "clubs":
            return card.clubs(val)
        elif suite == "diamonds":
            return card.diamonds(val)
        elif suite == "spades":
            return card.spades(val)
        else:
            return "error"

    def createDeck(self):
        deck = []
        for i in range(1,14):
            deck.append(self.create("hearts", i))
            deck.append(self.create("clubs", i))
            deck.append(self.create("diamonds", i))
            deck.append(self.create("spades", i))

        # shuffle the deck
        random.shuffle(deck)

        return deck
