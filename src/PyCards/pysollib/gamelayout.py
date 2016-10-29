from cardsets import CSI
from stack import Stack

class CardGame:
    def __init__(self):
        pass


class Klondike(CardGame):

    def __init__(self):
        self.type = CSI.TYPE_FRENCH
        self.name = Klondike
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 7
        self.numcards = 52
        self.foundations = 4

    # Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def createStacks(self):
        self.deckID = 0
        self.wasteID = 1
        self.stacks.append(Stack(0, 50, 50, -1, False, 0, [-1]*24, False, deck=True)) # Deck
        self.stacks.append(Stack(1, 100 + 50, 50, -1, False, 0, [], False))  # Waste

        stackCount = 2
        for num in range(self.foundations):
            _x = (self.numrows - num + 1) * 80 + 10
            _y = 50
            self.stacks.append(Stack(stackCount, _x, _y, 1, False, 1, [], True, sameSuit=True)) # create foundation stacks
            stackCount += 1

        for num in range(self.numrows):
            _x = num * 100 + 50
            _y = 250

            def cards():
                if num == 0:
                    return [1]
                else:
                    return [-1]*(num) + [1]

            self.stacks.append(Stack(stackCount, _x, _y, 13, True, -1, cards(),offset=15))  # create normal stacks
            stackCount += 1

    def deal(self):
        deck = self.stacks[self.deckID]
        waste = self.stacks[self.wasteID]
        for i in range(1, 4):
            card = deck.cards[-i]
            cardImg = deck.cardWidgets[-i]
            deck.cards.pop()
            waste.cards.append(card)
            deck.cardWidgets.pop()
            waste.cardWidgets.append(cardImg)
        for cardImg in waste.cardWidgets:
            cardImg.place(x=waste.x,
                y=waste.y + cardImg.cardNum * waste.offset)
        card = deck.cardWidgets[-1]
        card.place(x=deck.x,
            y=deck.y + card.cardNum * deck.offset)
        print len(deck.cards)
        print card.rank, card.suit