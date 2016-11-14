"""Defines the rules and properties of the hanoi game

	State Variables: none

    Environment Variables: none

    Assumptions: none

"""

from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..card import StandardCard
from ..stack import Stack
from ..database import DB


class Hanoi(CardGame):

    name = "Hanoi"

    def __init__(self, num_cards=4):
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
        self.stacks.append(Stack(0, 150, 250, -1, False, -1, [1]*self.numcards, True, offset=15))
        self.stacks.append(Stack(0, 350, 250, -1, False, -1, [], True, offset=15))
        self.stacks.append(Stack(0, 550, 250, -1, False, -1, [], True, offset=15))
        self._init_bindings()

    def _init_bindings(self):
        """Initialize mouse bindings"""
        from mouse_handler import Bindings
        self._bindings = Bindings(self)
        self._bindings.add("<B1-Motion>", lambda event: Bindings.default_drag(self._bindings, event))
        self._bindings.add("<ButtonRelease-1>", lambda event: Bindings.default_move(self._bindings, event))

    def startDeal(self, cardset):
        """Perform initial deal of cards"""
        for rank in range(0,self.numcards):
            self.stacks[0].cards[rank] = (StandardCard(cardset, rank, "h"))

    def valid_drop(self, stackID, destID, cardNum):
        """Indicate whether the selected cards can be moved to the destination stack"""
        if len(self.stacks[destID].cards) == 0:
            return True
        card = self.stacks[stackID].cards[cardNum]
        if self.stacks[destID].cards[-1].rank < card.rank:
            return False
        return True

    def bindings(self):
        """defines mouse bindings for game"""
        return self._bindings.value()

    def deal(self):
        """No in-game deals present in Hanoi games"""
        pass

DB.add_game("Hanoi", Hanoi) 
