from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..stack import Stack

class FreeCell(CardGame):
	
	def __init__(self):
        """Initialize standard properties of a FreeCell game"""
        self.type = TYPE.FRENCH
        self.name = FreeCell
        self.stacks = []
        self.numrows = 8
        self.numcards = 52
        self.foundations = 4

	# Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def create(self):
        """Docstring"""

		stackCount = 0
		
        # Initialize 
		for num in range(self.foundations):
            _x = stackCount * 80 + 10
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, -1, False, 0, [], capacity=1)) # create foundation stacks
            stackCount += 1
        # self.stacks.append(Stack(0, 50, 50, -1, False, 0, [-1]*24, False, deck=True)) # Deck
        # self.stacks.append(Stack(1, 100 + 50, 50, -1, False, 0, [], False))  # Waste

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
                if (0 <= num and num <= 3):
                    return [1]*7
                else:
                    return [1]*(6)

            self.stacks.append(Stack(stackCount, _x, _y, -1, True, -1, cards(), offset=15))  # create normal stacks
            stackCount += 1