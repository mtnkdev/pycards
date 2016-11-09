# !/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-


class Stack:

    def __init__(self, _id, x, y, base, alternate, direction, pos, accept=True, offset=0, deck=False, sameSuit=False):
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

        self.isdeck = deck
        
    def clone (self, clone):
        clone.id = self.id
        clone.game = self.game
        # clone.setRestrictions(self.getRestrictions)

        #
        # def addCard(self, card):
        #     self.cards.append(card)
        #
        # ### Not sure if we need this - instead insert *cards* (add w tuple)
        # def insertCard(self, card, position):
        #     self.cards.insert(position, card)
        #
        # def removeCard (self, card=None):
        #     assert len(cards)>0
        #     if card is None:
        #         card=cards[-1]
        #         del self.cards[-1]
        #     else:
        #         self.cards.remove(card)
        #     isFilled = False
        #     return card
        #
        # def getCard (self):
        #     if self.cards:
        #         return self.cards[-1]
        #     return None
        #
        # def getPile(self):
        #     if self.maxMove > 0:
        #         pile = self.cards[-self.maxMove:]
        #         while len(pile) >= self.minMove:
        #             if self.canMoveCards(cards):
        #                 return cards
        #             del pile[0]
        #     return None
        #
        # def updateModel(self, undo, flags):
        #     pass

    # def getRankDir (self, cards=None):
    #     if cards is None:
    #         cards = self.cards[-2:]
    #     if len (cards) <2:
    #         return 0
    #     dir = (cards[-1].rank - cards [-2].rank) % self.mod
    #     if dir > self.mod / 2:
    #         return dir - self.mod
    #     return dir
    #
    # def basicIsBlocked (self):
    #     return False
    #
    # def basicAcceptCards(self, from_stack, cards):
    #     if from_stack is self or self.basicIsBlocked():
    #         return False
    #     l = len (cards)
    #     if l < self.minAccept or l > self.maxAccept:
    #         return False
    #     l = l+len(self.cards)
    #     if l > self.maxCards:
    #         return False
    #     for card in cards:
    #         if not card.faceUp:
    #             return False
    #         if self.suitRestrict >=0 and card.suit != self.suitRestrict:
    #             return False
    #         if self.colourRestrict >= 0 and card.colour != self.colourRestrict:
    #             return False
    #         if self.rankRestrict >= 0 and card.rank != self.rankRestrict:
    #             return False
    #     if self.cards:
    #         return self.cards[-1].faceUp # top cards of stack has to be face up
    #     else:
    #         topCard = cards[0]
    #         if self.baseSuit >= 0 and card.suit != self.baseSuit:
    #             return False
    #         if self.baseColour >= 0 and card.colour != self.baseColour:
    #             return False
    #         if self.baseRank >= 0 and card.rank != self.baseRank:
    #             return False
    #         return True
    #
    # def basicCanMoveCards (self, cards):
    #     if self.basicIsBlocked():
    #         return False
    #     l = len(cards)
    #     if l < self.minMove or l > self.maxMove:
    #         return False
    #     l - len (self.cards)-1
    #     if l < self.minCards:
    #         return False
    #     return cardsFaceUp(cards)
    #
    # def acceptCards(self, fromStack, cards):
    #     return False
    #
    # def canMoveCards(self,cards):
    #     return False
    #
    # def canFlipCard(self):
    #     return False
    #
    # def canDropCards (self,stacks):
    #     return (None, 0)
    #
    # def __repr__(self):
    #     return "%s(%d)" % (self.__class__.__name__, self.id)
    #
    # def flipMove(self, animation=False):
    #     if animation:
    #         self.game.singleFlipMove(self)
    #     else:
    #         self.game.flipMove(self)
    #
    # def moveMove(self, ncards, toStack, frames=-1, shadows=-1):
    #     self.game.moveMove(ncards, self, Stack, frames=frames, shadow=shadow)
    #     self.fillStack()
    #
    # def fillStack(self):
    #     self.game.fillStack(self)
    #
    # def closeStack(self):
    #     pass
    #
    # def playFlipMove(self, sound=True, animation=False):
    #     if sound:
    #         self.game.playSample("flip",5)
    #     self.flipMove(animation=animation)
    #     if not self.game.checkForWin():
    #         self.game.autoPlay()
    #     self.game.finishMove()
    #
    # def playMoveMove (self, ncards, toStack, frames=-1, shadow=-1, sound=True):
    #     if sound:
    #         if to_stack in self.game.s.foundations:
    #             pass


def move_cards(game, stackID, destID, cardID):
    """Move cards and their associated label image to the destination stack"""
    
    for cardImg in game.stacks[stackID].cardWidgets[cardID:]:
        cardImg.stackID = destID
        game.stacks[stackID].cardWidgets.remove(cardImg)
        game.stacks[destID].cardWidgets.append(cardImg)
        cardImg.cardNum = len(game.stacks[destID].cardWidgets)-1
        cardImg.place(x=game.stacks[destID].x,
            y=game.stacks[destID].y + cardImg.cardNum * game.stacks[destID].offset)

    for card in game.stacks[destID].cardWidgets:
        card.lift()

    for card in game.stacks[stackID].cards[cardID:]:
        game.stacks[destID].cards.append(card)
        game.stacks[stackID].cards.remove(card)
