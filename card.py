class card:
    def __init__(self, val, suite):
        self.value = val
        self.suite = suite
        if (val<= 11):
            self.face = True
        else:
            self.face = False

class hearts(card):
    def __init__(self,val):
        super().__init__(val,"Hearts")

class spades(card):
    def __init__(self,val,face):
        super().__init__(val,"Spades")

class clubs(card):
    def __init__(self,val,face):
        super().__init__(val,"Clubs")

class diamonds(card):
    def __init__(self,val,face):
        super().__init__(val,"Diamonds")
