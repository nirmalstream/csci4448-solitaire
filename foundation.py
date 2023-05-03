class Foundation:
    def __init__(self):
        self.slots = [[], [], [], []]
        self.observers = []

    def add_card(self, card, slot):
        self.slots[slot].append(card)

        self.notify_observers()

    def remove_card(self, card, slot):
        self.slots[slot].remove(card)

        self.notify_observers()


    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.updateScore(1)

    def remove_ending_card(self, slot):
        card = self.slots[slot][-1]
        self.slots[slot].remove(card)
        return card

    def get_displayed_card(self,slot):
        card = self.slots[slot][-1]
        return card

    def check_valid_move(self,slot,card):
        suite = card.get_suite()
        value = card.get_value()

        if len(self.slots[slot]>0):
            foundation_card = self.get_displayed_card(slot)
            foundation_suite = foundation_card.get_suite()
            foundation_value = foundation_card.get_value()

            if (value - foundation_value == 1) and (suite == foundation_suite):
                return True
        else:
            if value==1:
                return True
        return False
