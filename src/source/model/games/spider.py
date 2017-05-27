"""Defines the rules and properties of the game spider solitaire 

    State Variables: none

    Environment Variables: none

    Assumptions: none

"""


from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..stack import Stack, move_cards
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

    def create(self):
        """Create the stacks for the spider solitaire game"""

        # Create deck stack
        self.deckID = 0
        self.stacks.append(Stack(0, 50, 50, -1, False, 0, [-1]*50, False, deck=True)) # Deck

        # Create foundation stacks
        stackCount = 1
        for num in range(self.foundations):
            _x = (self.numrows - num - 1) * 85 + 20
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, 1, False, 1, [], accept=False, remove=False, sameSuit=True)) # create foundation stacks
            stackCount += 1

        # Create any-suit stacks
        for num in range(self.numrows):
            _x = num * 85 + 20
            _y = 200

            def cards():
                stack = [-1]*4
                if num < 4:
                    stack.append(-1)
                stack.append(1)
                return stack

            self.stacks.append(Stack(stackCount, _x, _y, -1, False, -1, cards(),offset=15))  # create normal stacks
            stackCount += 1
        self._init_bindings()

    def _init_bindings(self):
        """Initialize mouse bindings"""
        from ..mouse_handler import Bindings
        self._bindings = Bindings(self)
        self._bindings.add("<B1-Motion>", lambda event: Bindings.default_drag(self._bindings, event))
        self._bindings.add("<ButtonRelease-1>", lambda event: Bindings.default_move(self._bindings, event))

    def deal(self):
        """Perform an in-game deal for spider solitaire"""

        deck = self.stacks[self.deckID]

        for i in range(self.foundations + 1, self.numrows):
            if len(self.stacks[i].cards) == 0:
                return None # all stacks must have at least one card before dealing

        for i in range(self.foundations + 1, self.foundations+self.numrows + 1):
            if len(deck.cards) == 0:
                return None # break because we can't deal anymore cards
            card = deck.cards[-1]
            cardImg = deck.cardWidgets[-1]
            deck.cards.pop()
            self.stacks[i].cards.append(card)
            deck.cardWidgets.pop()
            self.stacks[i].cardWidgets.append(cardImg)
            cardImg.stackID = self.stacks[i].ID
            cardImg.cardNum = len(self.stacks[i].cardWidgets) - 1
            cardImg.place(x=self.stacks[i].x,
                y=self.stacks[i].y + cardImg.cardNum * self.stacks[i].offset)

    def update(self):
        """Perform post-move automatic updates to the game"""
        for i in range(self.foundations + 1, len(self.stacks)):
            try:
                card = self.stacks[i].cards[-1]
                card.show()
                self.stacks[i].cardWidgets[-1].configure(image=card.get_image())
            except IndexError:
                pass

        for i in range(self.foundations+1, len(self.stacks)):
            stack = self.stacks[i]
            if len(stack.cards) == 0:
                continue
            num = 0
            while num + 13 <= len(stack.cards):
                if stack.cards[num].rank == 13 and stack.cards[num+12].rank == 1:
                    straight = True
                    for card in stack.cards[num:num+13]:
                        if card.suit != stack.cards[0].suit or card.visible is False:
                            straight = False
                    for c in range(num, num+12):
                        if stack.cards[c].rank < stack.cards[c+1].rank:
                            straight = False
                    if straight:
                        stackID = -1
                        for j in range(1, self.foundations+1):
                            if len(self.stacks[j].cards) == 0:
                                stackID = j
                                break
                        if stackID != -1:
                            move_cards(self, i, stackID, 0)
                        else:
                            raise ValueError("Invalid card positions")
                num += 1
        return self.check_win()

    def check_win(self):
        for i in range(1, self.foundations + 1):
            if len(self.stacks[i].cards) < 13:
                return False
        return True

    def valid_selection(self, stackID, cardNum):
        """Indicate whether the selected cards can be moved"""
        stack = self.stacks[stackID]

        if stack.isdeck:
            self.deal()
            for stack in self.stacks:
                for card in stack.cardWidgets:
                    card.lift()
            return False

        if not stack.removeCards:
            return False

        if cardNum == len(stack.cards) - 1:
            return True

        prev = stack.cards[cardNum]
        for i in range(cardNum+1, len(stack.cards)):
            if stack.cards[i].rank >= prev.rank or \
                            stack.cards[i].suit != prev.suit:
                return False
            prev = stack.cards[i]
        return True

    def bindings(self):
        """binds mouse to game"""
        return self._bindings.value()

DB.add_game("Spider", Spider)
