class Tableau:
    def __init__(self):
        self.slots = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

    def add_card(self, card, slot):
        self.slots[slot].append(card)


    def remove_card(self, card, slot):
        self.slots[slot].remove(card)
