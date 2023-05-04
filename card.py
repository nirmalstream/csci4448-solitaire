from abc import ABC, abstractmethod

# ABSTACT FACTORY PATTERN
class card(ABC):

    @abstractmethod
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


    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_suite(self):
        pass

    @abstractmethod
    def get_face(self):
        pass

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def get_face_up(self):
        pass

    @abstractmethod
    def set_face_up(self):
        pass

class hearts(card):
    def __init__(self,val):
        super().__init__(val,"hearts")

    def get_value(self):
        return self.value

    def get_suite(self):
        return self.suite

    def get_face(self):
        return self.face

    def get_color(self):
        return self.color

    def get_face_up(self):
        return self.face_up

    def set_face_up(self):
        self.face_up = not self.face_up

class spades(card):
    def __init__(self,val):
        super().__init__(val,"spades")

    def get_value(self):
        return self.value

    def get_suite(self):
        return self.suite

    def get_face(self):
        return self.face

    def get_color(self):
        return self.color

    def get_face_up(self):
        return self.face_up

    def set_face_up(self):
        self.face_up =  not self.face_up

class clubs(card):
    def __init__(self,val):
        super().__init__(val,"clubs")

    def get_value(self):
        return self.value

    def get_suite(self):
        return self.suite

    def get_face(self):
        return self.face

    def get_color(self):
        return self.color

    def get_face_up(self):
        return self.face_up

    def set_face_up(self):
        self.face_up =  not self.face_up

class diamonds(card):
    def __init__(self,val):
        super().__init__(val,"diamonds")

    def get_value(self):
        return self.value

    def get_suite(self):
        return self.suite

    def get_face(self):
        return self.face

    def get_color(self):
        return self.color

    def get_face_up(self):
        return self.face_up

    def set_face_up(self):
        self.face_up = not self.face_up
