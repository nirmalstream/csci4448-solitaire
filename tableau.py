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
