class Foundation:
    def __init__(self):
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.slot4 = []
        self.observers = []
    
    def add_card(self, card, slot):
        if slot == 1:
            self.slot1.append(card)
        elif slot == 2:
            self.slot2.append(card)
        elif slot == 3:
            self.slot3.append(card)
        elif slot == 4:
            self.slot4.append(card)
        self.notify_observers()

    def remove_card(self, card, slot):
        if slot == 1:
            self.slot1.remove(card)
        elif slot == 2:
            self.slot2.remove(card)
        elif slot == 3:
            self.slot3.remove(card)
        elif slot == 4:
            self.slot4.remove(card)

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.updateScore(1)