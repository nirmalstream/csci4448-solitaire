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
