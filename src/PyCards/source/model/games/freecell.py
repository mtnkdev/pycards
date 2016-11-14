"""This module defines the rules and properties of the game freecell

	State Variables: none

    Environment Variables: none

    Assumptions: none

"""

import math

from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..stack import Stack
from ..database import DB


class FreeCell(CardGame):

    name = "FreeCell"

    def __init__(self):
        """Initialize standard properties of a FreeCell game"""
        self.type = TYPE.STANDARD
        self.name = "FreeCell"
        self.stacks = []
        self.numrows = 8
        self.numcards = 52
        self.cells = 4
        self.foundations = 4

    def _init_bindings(self):
        """Initialize mouse bindings"""
        from mouse_handler import Bindings
        self._bindings = Bindings(self)
        self._bindings.add("<B1-Motion>", lambda event: Bindings.default_drag(self._bindings, event))
        self._bindings.add("<ButtonRelease-1>", lambda event: Bindings.default_move(self._bindings, event))

    def create(self):
        """Create game board"""

        stackCount = 0
        for num in range(self.cells):
            _x = stackCount * 80 + 10
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, -1, False, 0, [], capacity=1)) # create freecell stacks
            stackCount += 1

        # Create foundation stacks
        for num in range(self.foundations):
            _x = (self.numrows - num + 1) * 80 + 10
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, 1, False, 1, [], True, sameSuit=True, remove=False)) # create foundation stacks
            stackCount += 1

        # Create alternating-suit stacks
        for num in range(self.numrows):
            _x = num * 100 + 50
            _y = 250

            def cards():
                if 0 <= num <= 3:
                    return [1]*7
                else:
                    return [1]*6

            self.stacks.append(Stack(stackCount, _x, _y, -1, True, -1, cards(), offset=15))  # create normal stacks
            stackCount += 1
        self._init_bindings()
            
    # Moving cards.
    def valid_selection (self, stackID, cardNum):
        """Check if cards can be moved"""
        empty_cells = 0
        for i in range(self.cells):
            if len(self.stacks[i].cards) == 0:
                empty_cells += 1

        empty_stacks = 0
        for i in range(self.cells + self.foundations + 1, len(self.stacks)):
            if len(self.stacks[i].cards) == 0:
                empty_stacks += 1

        # Raising AttributeError allows this to be used in conjunction with
        # default behaviour
        num_cards = len(self.stacks[stackID].cards) - cardNum
        if num_cards <= ((1 + empty_cells) * math.pow(2, empty_stacks)):
            raise AttributeError

        return None

        # free_move = 1
        # for num in range(len(self.stacks)):
        #     if !((self.cells <= num and num < self.cells + self.foundations)) and stack[num].cards == 0:
        #         free_cells += 1
        # return len(cards) > free_cells

    def bindings(self):
        """defines mouse bindings for game"""
        return self._bindings.value()

    def deal(self):
        """No in-game deals for FreeCell games"""
        pass

DB.add_game("FreeCell", FreeCell)