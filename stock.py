class Stock:
    def __init__(self, cards):
        self.cards = cards
        self.flipped_cards = []

    def turn(self):
        # get first card from stock
        card = self.cards.pop(0)

        # add to bottom of stock
        self.cards.append(card)

        return card
    
    def get_card(self):
        # remove first card from stock

        if self.cards == [] and self.flipped_cards == []:
            return None
        elif self.cards == []:
            self.cards = self.flipped_cards
            self.flipped_cards = []
            return self.get_card()
        
        card = self.cards.pop(0)
        self.flipped_cards.append(card)
        return card
    
    def get_flipped_cards(self):
        # get the last flipped cards
        card = self.flipped_cards[-1]
        # remove from flipped cards
        self.flipped_cards.remove(card)
        return card




    

