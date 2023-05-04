# OBSERVER PATTERN
class observer:
    def __init__(self):
        self.score = 0

    def updateScore(self,points):
        self.score += points
