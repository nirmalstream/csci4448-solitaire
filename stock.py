class Stock:
    def __init__(self):
        self.cards = []

    def turn(self):
        # get first card from stock
        card = self.cards.pop(0)

        # add to bottom of stock
        self.cards.append(card)

        return card
    
    

