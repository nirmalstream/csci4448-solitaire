class Tableau:
    def __init__(self):
        self.slots = {}

    def move_card(self, slot_from, card, slot_to):
        self.slots[slot_from].remove(card)
        self.slots[slot_to].append(card)

    def add_card(self, slot, card):
        self.slots[slot].append(card)
    

    
