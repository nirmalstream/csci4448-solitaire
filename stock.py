class Stock:
    def __init__(self, cards):
        self.cards = cards

    def turn(self):
        # get first card from stock
        card = self.cards.pop(0)

        # add to bottom of stock
        self.cards.append(card)

        return card
    
    def get_card(self):
        # remove first card from stock
        return self.cards.pop(0)    
    

