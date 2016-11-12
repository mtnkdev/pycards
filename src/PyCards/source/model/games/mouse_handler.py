from ..stack import move_cards


class Bindings:

    def __init__(self, game):
        self._game = game
        self.bindings = {}

    def add(self, event, callback):
        self.bindings[event] = callback

    @classmethod
    def _valid_drop(cls, obj, event, destID):
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

        if stack.sameSuit and bottom.suit != event.widget.suit:
            return False

        if event.widget.rank - bottom.rank != stack.direction:
            return False

        return True

    @classmethod
    def default_drag(cls, obj, event):
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
        ID = event.widget.stackID
        x = event.widget.winfo_x() + event.x - event.widget.winfo_width() / 2
        y = event.widget.winfo_y() + event.y - event.widget.winfo_height() / 2
        destID = _nearest(obj._game, x, y)

        if destID == -1:
            cardID = event.widget.cardNum
            for cardImg in obj._game.stacks[ID].cardWidgets[cardID:]:
                cardImg.place(x=obj._game.stacks[ID].x, y=obj._game.stacks[ID].y + cardImg.cardNum * obj._game.stacks[ID].offset)
            # print "invalid dest"
            return None

        select = cls.default_selection(obj, event)
        drop = cls._valid_drop(obj, event, destID)
        # print "select", select
        # print "drop", drop
        if select and drop:
            move_cards(obj._game, ID, destID, event.widget.cardNum)
        else:
            cardID = event.widget.cardNum
            for cardImg in obj._game.stacks[ID].cardWidgets[cardID:]:
                cardImg.place(x=obj._game.stacks[ID].x, y=obj._game.stacks[ID].y + cardImg.cardNum * obj._game.stacks[ID].offset)
                # print "returned"

    def value(self):
        return self.bindings



def _nearest(game, x, y):
    for i in range(len(game.stacks)):
        stack = game.stacks[i]
        if abs(stack.x - x) < 20 and abs(stack.y + stack.offset * len(stack.cards) - y) < 20:
            return i
    return -1