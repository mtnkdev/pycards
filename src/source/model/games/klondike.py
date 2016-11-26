"""Defines the rules and properties of the klondike varient of solitaire

    State Variables: none

    Environment Variables: none

    Assumptions: none

"""

from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..stack import Stack
from ..database import DB


class Klondike(CardGame):

    name = "Klondike"

    def __init__(self):
        """Initialize standard properties of a Klondike game

        Klondike solitaire is your typical single-player solitaire card game
        """
        self.type = TYPE.STANDARD
        self.name = "Klondike"
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 7
        self.numcards = 52
        self.foundations = 4

    def create(self):
        """Create the stacks for the Klondike game"""

        # Create deck and waste stacks
        self.deckID = 0
        self.wasteID = 1
        self.stacks.append(Stack(0, 50, 50, -1, False, 0, [-1]*24, False, deck=True)) # Deck
        self.stacks.append(Stack(1, 100 + 50, 50, -1, False, 0, [], False))  # Waste

        # Create foundation stacks
        stackCount = 2
        for num in range(self.foundations):
            _x = (self.numrows - num + 1) * 80 + 10
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, 1, False, 1, [], True, sameSuit=True)) # create foundation stacks
            stackCount += 1

        # Create alternating-suit stacks
        for num in range(self.numrows):
            _x = num * 100 + 50
            _y = 250

            def cards():
                if num == 0:
                    return [1]
                else:
                    return [-1]*num + [1]

            self.stacks.append(Stack(stackCount, _x, _y, 13, True, -1, cards(),offset=15))  # create normal stacks
            stackCount += 1
        self._init_bindings()

    def _init_bindings(self):
        """Initialize mouse bindings"""
        from ..mouse_handler import Bindings
        self._bindings = Bindings(self)
        self._bindings.add("<B1-Motion>", lambda event: Bindings.default_drag(self._bindings, event))
        self._bindings.add("<ButtonRelease-1>", lambda event: Bindings.default_move(self._bindings, event))

    # FIXME extract card moving functionality from this method
    def deal(self):
        """Perform an in-game deal"""

        deck = self.stacks[self.deckID]
        waste = self.stacks[self.wasteID]

        if len(deck.cards) == 0:
            if len(waste.cards) != 0:
                for i in range(len(waste.cards)):
                    card = waste.cards.pop()
                    cardImg = waste.cardWidgets.pop()
                    deck.cards.append(card)
                    deck.cards[i].hide()
                    cardImg.configure(image=card.get_image())
                    cardImg.place(x=deck.x,
                                  y=deck.y + cardImg.cardNum * deck.offset)
                    deck.cardWidgets.append(cardImg)
                    cardImg.stackID = deck.ID
                    cardImg.cardNum = len(deck.cards) - 1
                return None

        if len(deck.cards) > 3:
            num = 4
        else:
            num = len(deck.cards) + 1

        for i in range(1, num):
            card = deck.cards[-1]
            cardImg = deck.cardWidgets[-1]
            deck.cards.pop()
            waste.cards.append(card)
            deck.cardWidgets.pop()
            waste.cardWidgets.append(cardImg)
            cardImg.cardNum = len(waste.cardWidgets) - 1
            cardImg.stackID = waste.ID

        for i in range(len(waste.cardWidgets)):
            cardImg = waste.cardWidgets[i]
            cardImg.place(x=waste.x,
                y=waste.y + cardImg.cardNum * waste.offset)
            card = waste.cards[i]
            card.show()
            cardImg.configure(image=card.get_image())

        if len(deck.cards) > 0:
            card = deck.cardWidgets[-1]
            card.place(x=deck.x,
                y=deck.y + card.cardNum * deck.offset)

    def update(self):
        for i in range(self.foundations + 2, len(self.stacks)):
            try:
                card = self.stacks[i].cards[-1]
                card.show()
                self.stacks[i].cardWidgets[-1].configure(image=card.get_image())
            except IndexError:
                pass

        return self.check_win()

    def check_win(self):
        for i in range(2, self.foundations + 2):
            if len(self.stacks[i].cards) < 13:
                return False
        return True

    def bindings(self):
        """defines mouse bindings for game"""
        return self._bindings.value()

DB.add_game("Klondike", Klondike)
