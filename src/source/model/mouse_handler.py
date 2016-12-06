"""This module is responsible for dealing with mouse input
    
    State Variables: none

    Environment Variables: none

    Assumptions: none

"""

from stack import move_cards
from ..control.gamemanager import destroy, dealgame, drawgame

class Bindings:

    def __init__(self, game):
        """initializes mouse handler and binds it to a game"""
        self._game = game
        self.bindings = {}

    def add(self, event, callback):
        """Adds mouse handler to a game"""
        self.bindings[event] = callback

    @classmethod
    def _valid_drop(cls, obj, event, destID):
        """checks if card can be dropped"""
        stack = obj._game.stacks[destID]

        try:
            return obj._game.valid_drop(event.widget.stackID, destID, event.widget.cardNum)
        except AttributeError:
            pass

        if not stack.acceptCards:
            return False

        if stack.base > -1:
            if len(stack.cards) == 0 and event.widget.rank == stack.base:
                return True

            if len(stack.cards) == 0 and event.widget.rank != stack.base:
                return False

        if len(stack.cards) == 0:
            return True

        bottom = stack.cards[-1]

        if stack.alternates and bottom.color == event.widget.color:
            return False

        if stack.sameSuit:
            for card in obj._game.stacks[event.widget.stackID].cards[event.widget.cardNum:]:
                if card.suit != bottom.suit:
                    return False

        if event.widget.rank - bottom.rank != stack.direction:
            return False

        return True

    @classmethod
    def default_drag(cls, obj, event):
        """Defines how dragging a card in the game works"""
        if not cls.default_selection(obj, event):
            return None

        ID = event.widget.stackID
        if event.widget.cardNum == len(obj._game.stacks[ID].cards) - 1:
            x = event.widget.winfo_x() + event.x - event.widget.winfo_width()/2
            y = event.widget.winfo_y() + event.y - event.widget.winfo_height()/2
            event.widget.place(x=x, y=y)
            event.widget.lift()
        else:
            cardID = event.widget.cardNum
            for cardImg in obj._game.stacks[ID].cardWidgets[cardID:]:
                x = cardImg.winfo_x() + event.x - cardImg.winfo_width() / 2
                y = cardImg.winfo_y() + event.y - cardImg.winfo_height() / 2
                cardImg.place(x=x, y=y)
                cardImg.lift()
        return None

    @classmethod
    def default_selection(cls, obj, event):
        """Allows user to select cards"""
        stackID = event.widget.stackID
        cardNum = event.widget.cardNum

        try:
            return obj._game.valid_selection(stackID, cardNum)
        except AttributeError:
            pass

        stack = obj._game.stacks[stackID]
        if stack.isdeck:
            obj._game.deal()
            for stack in obj._game.stacks:
                for card in stack.cardWidgets:
                    card.lift()
            return False

        if cardNum == len(stack.cards) - 1:
            return True

        if stack.alternates:
            prev = stack.cards[cardNum]
            for i in range(cardNum + 1, len(stack.cards)):
                if stack.cards[i].rank >= prev.rank or \
                    stack.cards[i].color == prev.color:
                    return False
                prev = stack.cards[i]
            return True
        return False

    @classmethod
    def default_move(cls, obj, event):
        """Moves cards from one stack to another"""
        ID = event.widget.stackID
        x = event.widget.winfo_x() + event.x - event.widget.winfo_width() / 2
        y = event.widget.winfo_y() + event.y - event.widget.winfo_height() / 2
        destID = _nearest(obj._game, x, y)

        if destID == -1:
            cardID = event.widget.cardNum
            for cardImg in obj._game.stacks[ID].cardWidgets[cardID:]:
                cardImg.place(x=obj._game.stacks[ID].x, y=obj._game.stacks[ID].y + cardImg.cardNum * obj._game.stacks[ID].offset)
            return None

        select = cls.default_selection(obj, event)
        drop = cls._valid_drop(obj, event, destID)

        if select and drop:
            move_cards(obj._game, ID, destID, event.widget.cardNum)
        else:
            cardID = event.widget.cardNum
            for cardImg in obj._game.stacks[ID].cardWidgets[cardID:]:
                cardImg.place(x=obj._game.stacks[ID].x, y=obj._game.stacks[ID].y + cardImg.cardNum * obj._game.stacks[ID].offset)

        try:
            if obj._game.update():
                restart(obj._game)
        except AttributeError:
            pass
        update(obj._game)

    def value(self):
        return self.bindings


def restart(obj):
    """Start a new instance of the same game type"""
    import tkMessageBox
    if tkMessageBox.askyesno("", 'Congratulations you win!!! Do you want to start a new game?', default="yes"):
       destroy()
       dealgame(game=obj.__class__)
       drawgame()


def _nearest(game, x, y):
    """Finds which stack the mouse is overtop of (if any)"""
    for i in range(len(game.stacks)):
        stack = game.stacks[i]
        if abs(stack.x - x) < 30 and abs(stack.y + stack.offset * len(stack.cards) - y) < 30:
            return i
    return -1


def update(game):
    """updates game"""
    pass
