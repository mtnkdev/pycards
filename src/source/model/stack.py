"""This class represents a stack of cards in the game
	
    State Variables: none
	
    Environment Variables: none

    Assumptions: none

"""


class Stack:

    def __init__(self, _id, x, y, base, alternate, direction, pos, accept=True, offset=0, deck=False, sameSuit=False, remove=True, capacity=-1):
        """Initialize a stack - the placeholder for cards in a game

        :param _id: index of the stack relative to the game layout
        :param x: horizontal coordinate of upper left corner
        :param y: vertical coordinate of upper left corner
        :param base: base suit for the stack - see SRS for restrictions
        :param alternate: whether or not the card colour must alternate
        :param direction: the direction the stack builds in
        :param pos: sequence for mapping cards to face-up or face-down status

        Keyword arguments
        :param accept: whether cards can be added to the stack (default True)
        :param offset: amount of visual staggering of drawn cards (default 0)
        :param deck: whether the stack is a deck (default False)
        :param sameSuit: if stack only allows same suit cards (default False)
        :param remove: whether cards can be removed from the stack (default True)
        :param capacity: how many cards the stack can hold (default -1 -> no restriction)
        """

        self.ID = _id
        self.x = int (round(x))        # stack's x coordinate (upper left corner)
        self.y = int (round(y))        # stack's y coordinate (upper left corner)

        self.positions = pos
        self.cards = [0]*len(self.positions)  # cards in stack
        self.cardWidgets = [0]*len(self.positions)

        #   Rules for building stack    #
        self.offset = offset
        self.base = base
        self.alternates = alternate
        self.sameSuit = sameSuit
        self.acceptCards = accept
        self.direction = direction
        self.removeCards = remove
        self.isdeck = deck
        self.capacity = capacity


def move_cards(game, stackID, destID, cardID):
    """Move cards and their associated label image to the destination stack"""

    for cardImg in game.stacks[stackID].cardWidgets[cardID:]:
        cardImg.stackID = destID
        game.stacks[stackID].cardWidgets.remove(cardImg)
        game.stacks[destID].cardWidgets.append(cardImg)
        cardImg.cardNum = len(game.stacks[destID].cardWidgets)-1
        cardImg.place(x=game.stacks[destID].x,
            y=game.stacks[destID].y + cardImg.cardNum * game.stacks[destID].offset)

    # Assert the proper stacking of widgets in the destination stack
    for card in game.stacks[destID].cardWidgets:
        card.lift()

    for card in game.stacks[stackID].cards[cardID:]:
        game.stacks[destID].cards.append(card)
        game.stacks[stackID].cards.remove(card)

    # Any module-level code is run upon first import hence
    # the need to carefully place import statements to
    # decrease overhead and prevent side-effects
    from ..control.gamemanager import update
    update()
