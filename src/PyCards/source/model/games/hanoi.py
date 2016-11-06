from ..gamelayout import CardGame
from ..card import StandardCard
from ..cardsets import TYPE
from ..stack import Stack


class Hanoi(CardGame):

    def __init__(self):
        """Initialize standard properties of a 4-card Hanoi game"""
        self.type = TYPE.STANDARD
        self.name = "Hanoi4"
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 3
        self.numcards = 4
        self.foundations = 3

     # Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def create(self):
        """Docstring"""
        self.stacks.append(Stack(0, 150, 250, -1, False, -1, [-1]*4, True, offset=15))
        self.stacks.append(Stack(0, 350, 250, -1, False, -1, [], True, offset=15))
        self.stacks.append(Stack(0, 550, 250, -1, False, -1, [], True, offset=15))


    def startDeal(self, cardset):
        """Initial dealing of cards"""
        for rank in range(0,4):
            self.stacks[0].cards[rank] = (StandardCard(cardset, rank, "h"))

                          


    def deal(self):
        """Docstring"""
        pass
