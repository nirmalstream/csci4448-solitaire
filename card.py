class card:
    def __init__(self, val, suite):
        self.value = val
        self.suite = suite
        self.face_up = False
        if (val == 1 or val>= 11):
            self.face = True
        else:
            self.face = False
        if suite == "hearts" or suite == "diamonds":
            self.color = "red"
        else :
            self.color = "black"

class hearts(card):
    def __init__(self,val):
        super().__init__(val,"hearts")

class spades(card):
    def __init__(self,val):
        super().__init__(val,"spades")

class clubs(card):
    def __init__(self,val):
        super().__init__(val,"clubs")

class diamonds(card):
    def __init__(self,val):
        super().__init__(val,"diamonds")
