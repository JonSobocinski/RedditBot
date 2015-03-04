__author__ = 'TexasLonghorns'


class TopCommenter:

    def __init__(self, user, score):
        self.user = user
        self.score = score

    def getUser(self):
        return self.user

    def getScore(self):
        return self.score
