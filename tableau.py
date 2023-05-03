class Tableau:
    def __init__(self):
        self.slots = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

    def add_card(self, card, slot):
        self.slots[slot].append(card)


    def remove_card(self, card, slot):
        self.slots[slot].remove(card)

    def remove_ending_card(self, slot):
        card = self.slots[slot][-1]
        self.slots[slot].remove(card)

        # make the last card face up
        if len(self.slots[slot]) > 0:
            self.slots[slot][-1].face_up = True
        return card

    def get_bottom_card(self,slot):
        card = self.slots[slot][-1]
        return card

    def check_valid_move(self,slot,card):
        value = card.get_value()
        color = card.get_color()

        tableu_card = self.get_bottom_card()
        tableau_value = tableu_card.get_value()
        tableau_color = tableu_card.get_color()

        if (tableau_value-value == 1):
            if (tableau_color == "red" and color == "black") or (tableau_color == "black" and color == "red"):
                return True
        return False
