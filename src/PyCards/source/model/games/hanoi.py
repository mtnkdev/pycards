from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..stack import Stack


class Hanoi(CardGame):

    def __init__(self):
        """Initialize standard properties of a 4-card Hanoi game"""
        self.type = TYPE.FRENCH
        self.name = Hanoi4
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 3
        self.numcards = 4
        self.foundations = 3

     # Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def create(self):
        """Docstring"""
        self.stack.append(Stack(0, 100, 100, -1, False, -1, [-1]*4, True))
        self.stack.append(Stack(0, 200, 100, -1, False, -1, [], True))
        self.stack.append(Stack(0, 300, 100, -1, False, -1, [], True))
                          


    def deal(self):
        """Docstring"""
        pass
