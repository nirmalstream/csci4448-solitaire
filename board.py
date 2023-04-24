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

        # now create the stock with the remaining cards
        self.stock = stock.Stock(deck)


        
    def move_card(self, source, dest, card, slot = None):
        if source == "stock":
            card = self.stock.get_card()
        elif source == "foundation":
            self.foundation.remove_card(card, slot)
        elif source == "tableau":
            self.tableau.remove_card(card, slot)
            
        if dest == "stock":
            # can't move to stock
            return "error"
        elif dest == "foundation":
            self.foundation.add_card(card, slot)
        elif dest == "tableau":
            self.tableau.add_card(card, slot)