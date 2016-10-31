import ttk

from .. import dataloader
from .. import gamelayout
from ..gamelayout import Klondike
from ..dealer import Dealer
from ..stack import moveCards

__all__ = ['dealgame', 'drawgame']

_game = None

def dealgame(root, game=None):
    global _game
    if game is None:
        _game = Klondike()
    else:
        _game = game

    cardset = dataloader.Cardset.cardsets["Standard"]
    dealer = Dealer(_game, cardset)
    _game.createStacks()
    dealer.cardgen()
    dealer.dealCards()


def drawgame(root):
    global _game
    stackID = 0
    for stack in _game.stacks:
        for num in range(len(stack.cards)):
            label = ttk.Label(root.canvas, image=stack.cards[num].setImage(), borderwidth=0)
            setattr(label, "rank", stack.cards[num].rank)
            setattr(label, "suit", stack.cards[num].suit)
            setattr(label, "color", stack.cards[num].color)
            setattr(label, "stackID", stackID)
            setattr(label, "cardNum", num)

            stack.cardWidgets[num] = label
            label.place(x=stack.x, y=stack.y + stack.offset*num)
            label.bind("<ButtonRelease-1>", _legalmove)
            label.bind("<B1-Motion>", _dragCard)
        stackID += 1
    return None

def _dragCard(event):
    global _game
    if not _valid_selection(event):
        return
    ID = event.widget.stackID
    if event.widget.cardNum == len(_game.stacks[ID].cards) - 1:
        # print "drag1"
        x = event.widget.winfo_x() + event.x - event.widget.winfo_width()/2
        y = event.widget.winfo_y() + event.y - event.widget.winfo_height()/2
        event.widget.place(x=x, y=y)
    else:
        # print "drag1+"
        cardID = event.widget.cardNum
        for cardImg in _game.stacks[ID].cardWidgets[cardID:]:
            x = cardImg.winfo_x() + event.x - cardImg.winfo_width() / 2
            y = cardImg.winfo_y() + event.y - cardImg.winfo_height() / 2
            cardImg.place(x=x, y=y)
    return None


def _nearest(x, y):
    for i in range(len(_game.stacks)):
        stack = _game.stacks[i]
        if abs(stack.x - x) < 20 and abs(stack.y + stack.offset*len(stack.cards) - y) < 20:
            return i
    return -1


def _legalmove(event):
    ID = event.widget.stackID
    x = event.widget.winfo_x() + event.x - event.widget.winfo_width() / 2
    y = event.widget.winfo_y() + event.y - event.widget.winfo_height() / 2
    destID = _nearest(x, y)

    if destID == -1:
        cardID = event.widget.cardNum
        for cardImg in _game.stacks[ID].cardWidgets[cardID:]:
            cardImg.place(x=_game.stacks[ID].x, y=_game.stacks[ID].y + cardImg.cardNum * _game.stacks[ID].offset)
        # print "invalid dest"
        return None

    select = _valid_selection(event)
    drop = _valid_drop(event, destID)
    # print "select", select
    # print "drop", drop
    if select and drop:
        moveCards(_game, ID, destID, event.widget.cardNum)
        # print "moved"
    else:
        cardID = event.widget.cardNum
        for cardImg in _game.stacks[ID].cardWidgets[cardID:]:
            cardImg.place(x=_game.stacks[ID].x, y=_game.stacks[ID].y + cardImg.cardNum * _game.stacks[ID].offset)
        # print "returned"


def _valid_selection(event):
    stackID = event.widget.stackID
    cardNum = event.widget.cardNum
    stack = _game.stacks[stackID]

    if stack.isdeck:
        _game.deal()
        return False

    if cardNum == len(stack.cards) - 1:
        return True

    if stack.alternates:
        prev = stack.cards[cardNum]
        for i in range(cardNum + 1, len(stack.cards)):
            if stack.cards[i].rank >= prev.rank or \
                stack.cards[i].color == prev.color:
                return False
        return True
    # print "Invalid selection"
    return False


def _valid_drop(event, destID):
    stack = _game.stacks[destID]

    if not stack.acceptCards:
        return False

    if len(stack.cards) == 0 and event.widget.rank == stack.base:
        return True

    if len(stack.cards) == 0 and event.widget.rank != stack.base:
        return False

    bottom = stack.cards[-1]

    if stack.alternates and bottom.color == event.widget.color:
        return False
    elif not stack.alternates and bottom.color != event.widget.color:
        return False

    if stack.sameSuit and bottom.suit != event.widget.suit:
        return False

    if event.widget.rank - bottom.rank != stack.direction:
        return False

    # print "valid selection"
    return True
