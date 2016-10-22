#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-

class AbstractCard:
	
	#init method, initializes state and variables
	def __init__(self, id, deck, suit, rank, game, x=0, y=0):
		self.id = id
		self.deck = deck
		self.suit = suit
		self.color = suit/2
		self.rank = rank
		self.game = game
		self.x = x
		self.y = y
		self.faceUp = False;
		
	#To Sting method for debugging
	def __str__ (self):
		return "Card (%d, %d, %d, %d)" % (self.id, self.deck, self.suit, self.rank)
		
	#change x and y position of card to new x and y
	def moveTo(self, x, y):
		self.x = x
		self.y = y
		
	#change x and y position of card by dx and dy
	def moveBy(self, x, y):
		self.x = x+dx
		self.y = y+dy
		
		
		
	def hide (self, stack):
		pass
	
	 def unhide(self):
        pass

    def setSelected(self, s, group=None):
        pass

    def showFace(self):
        # Turn the card's face up.
        raise SubclassResponsibility

    def showBack(self):
        # Turn the card's face down.
        raise SubclassResponsibility

    def updateCardBackground(self, image):
        raise SubclassResponsibility

    def close(self):
        pass

    def unclose(self):
        pass