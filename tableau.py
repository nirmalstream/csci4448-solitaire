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
    
    def move_card(self, card, slot_from, slot_to):
        # get the card from the tableau
        card_index = self.slots[slot_from].index(card)
        card = self.slots[slot_from][card_index]
        # check to see if the card is the last card in the tableau
        if card == self.slots[slot_from][-1]:
            self.remove_card(card, slot_from)
            self.add_card(card, slot_to)

        else:
            # get the index of the card
            index = self.slots[slot_from].index(card)
            # get the cards after the card
            cards = self.slots[slot_from][index:]
            # remove the cards from the tableau
            for card in cards:
                self.remove_card(card, slot_from)
            # add the cards to the tableau
            for card in cards:
                self.add_card(card, slot_to)

            # make the last card face up
            self.slots[slot_from][-1].face_up = True
