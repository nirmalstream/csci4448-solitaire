import foundation
import tableau
import stock
class Board:
    def __init__(self, deck):
        self.foundation = foundation.Foundation()

        self.tableau = tableau.Tableau()

        # deal cards to tableau
        for i in range(1, 8):
            for _ in range(i):
                card = deck.pop(0)
                self.tableau.add_card(card, i)

        # last card in each tableau is face up
        for i in range(1, 8):
            self.tableau.slots[i][-1].face_up = True

        # now create the stock with the remaining cards
        # all cards are face up in the stock
        for card in deck:
            card.face_up = True
        self.stock = stock.Stock(deck)


        
    def move_card(self, source, dest, card, slot_from = None, slot_to = None):
        if source == "stock":
            card = self.stock.get_card()
        elif source == "foundation":
            self.foundation.remove_card(card, slot_from)
        elif source == "tableau":
            self.tableau.remove_card(card, slot_from)
            
        if dest == "stock":
            # can't move to stock
            return "error"
        elif dest == "foundation":
            self.foundation.add_card(card, slot_to)
        elif dest == "tableau":
            self.tableau.add_card(card, slot_to)