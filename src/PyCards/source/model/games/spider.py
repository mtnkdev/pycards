from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..stack import Stack
from ..database import DB


class Spider(CardGame):

    name = "Spider"

    def __init__(self):
        """Initialize standard properties of a Spider Solitaire game"""
        self.type = TYPE.STANDARD
        self.name = "Spider"
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 10
        self.numcards = 104
        self.foundations = 8

    # Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def create(self):
        """Create the stacks for the spider solitaire game"""

        # Create deck stack
        self.deckID = 0
        self.stacks.append(Stack(0, 50, 50, -1, False, 0, [-1]*50, False, deck=True)) # Deck

        # FIXME make conditional acceptance so that the stacks have
        # a minimum size that they accept
        # 
        # Create foundation stacks
        stackCount = 1
        for num in range(self.foundations):
            _x = (self.numrows - num - 1) * 85 + 20
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, 1, False, 1, [], accept=False, sameSuit=True)) # create foundation stacks
            stackCount += 1

        # Create any-suit stacks
        for num in range(self.numrows):
            _x = num * 85 + 20
            _y = 250

            def cards():
                stack = [-1]*4
                if num < 4:
                    stack.append(-1)
                stack.append(1)
                return stack

            self.stacks.append(Stack(stackCount, _x, _y, -1, False, -1, cards(),offset=15))  # create normal stacks
            stackCount += 1

    def deal(self):
        """Perform an in-game deal for spider solitaire"""

        deck = self.stacks[self.deckID]

        for i in range(self.numrows):
            if len(self.stacks[i].cards) == 0:
                pass # all stacks must have at least one card before dealing

        for i in range(self.foundations + 1, self.foundations+self.numrows + 1):
            if len(deck.cards) == 0:
                return None # break because we can't deal anymore cards
            card = deck.cards[-1]
            cardImg = deck.cardWidgets[-1]
            deck.cards.pop()
            self.stacks[i].cards.append(card)
            deck.cardWidgets.pop()
            self.stacks[i].cardWidgets.append(cardImg)
            cardImg.cardNum = len(self.stacks[i].cardWidgets) - 1
            cardImg.place(x=self.stacks[i].x,
                y=self.stacks[i].y + cardImg.cardNum * self.stacks[i].offset)


DB.add_game("Spider", Spider)
