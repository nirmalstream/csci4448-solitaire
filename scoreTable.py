class ScoreTable:
    def __init__(self):
        self.score = 0

    
    def add_score(self, name, score):
        self.score_list[name] = score
        print(self.score_list)

    def save_score_to_csv(self, name):
        with open('score.csv', 'a') as f:
            f.write(name + "," + str(self.score) + "\n")

    def updateScore(self, score):
        self.score += score
        print(self.score)