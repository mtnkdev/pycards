from ..gamelayout import CardGame
from ..card import StandardCard
from ..cardsets import TYPE
from ..stack import Stack
from ..database import DB


class Hanoi(CardGame):

    name = "Hanoi"

    def __init__(self, num_cards):
        """Initialize standard properties of a 4-card Hanoi game

        Hanoi games are card-based representations of the well-known
        Tower of Hanoi logic puzzle
        """
        self.type = TYPE.STANDARD
        self.name = "Hanoi" + str(num_cards)
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 3
        self.numcards = num_cards
        self.foundations = 0

     # Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def create(self):
        """Create the stacks (left, middle, right) for the Hanoi game"""
        self.stacks.append(Stack(0, 150, 250, -1, False, -1, [-1]*self.numcards, True, offset=15))
        self.stacks.append(Stack(0, 350, 250, -1, False, -1, [], True, offset=15))
        self.stacks.append(Stack(0, 550, 250, -1, False, -1, [], True, offset=15))


    def startDeal(self, cardset):
        """Initial dealing of cards"""
        for rank in range(0,self.numcards):
            self.stacks[0].cards[rank] = (StandardCard(cardset, rank, "h"))

                          


    def deal(self):
        """No in-game deals present in Hanoi games"""
        pass

DB.add_game("Hanoi", Hanoi) 
