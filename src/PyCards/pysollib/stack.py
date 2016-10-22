#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-

class Stack:
	
	#initialization method.  x and y are upper left position of stack, game is the game
	#game that the stack belongs to
	def __init__(self, x, y ,game):
		id = len(game.stacks) 	#stack's id what "number" stack it is in the game
		game.stacks.append(self)#add stack to game's array of stacks
		x = int (round(x))		#stack's x coordinate (upper left corner)
		y = int (round(y))		#stack's y coordinate (upper left corner)
		
		cards = []				#cards in stack
		isFilled = False		#if stack is at max
		
		#Card restricitons on stack (-1 is no restriction)
		suitRestrict	= -1 
		colourRestrict	= -1 
		rankRestrict	= -1
		baseSuit		= -1
		baseColour		= -1
		baseRank		= -1
		direction		= 0		#if stack builds up/down
		mod				= 8192	#modulo for wrap around (usually 13 or 8192)
		maxMove			= 0		#maximum number of cards that moved at a time
		maxAccept		= 0		#maximum number of cards the stack can accept at a time
		maxCards		= 999	#largest amount of cards that can be in a stack
		minMove			= 1		#least amount of cards that can be moved at a time
		minAccept		= 1		#minimum number of cards  that can be moved onto this stack
		minCards		= 0		#minumum number of cards this stack is allowed to have
		
	def setRestrictions(self, suit, colour, rank, baseSuit, baseColour, baseRank, direction, mod, maxMove, maxAccept, maxCards, minMove, minAccept, minCards):
		self.suitRestrict	= suit
		self.colourRestrict	= colour
		self.rankRestrict	= rank
		self.baseSuit		= baseSuit
		self.baseColour		= baseColour
		self.baseRank		= baseRank
		self.direction		= direction
		self.mod			= mod
		self.maxMove		= maxMove
		self.maxAccept		= maxAccept
		self.maxCards		= maxCards
		self.minMove		= minMove
		self.minAccept		= minAccept
		self.minCards		= minCards
	
	def addCard(self, card):
		self.cards.append(card)
		
	def insertCard(self, card, position):
		self.cards.insert(position, card)
	
	def removeCard (self, card=None):
		assert len(cards)>0
		if card is None:
			card=cards[-1]
			del self.cards[-1]
		else
			self.cards.remove(card)
		isFilled = False
		return card
		
	def getCard (self):
		if self.cards:
			return self.cards[-1]
		return None
		
	def getPile(self):
		if self.maxMove > 0:
			pile = self.cards[-self.maxMove:]
			while len(pile) >= self.minMove:
				if self.canMoveCards(cards):
					return cards
				del pile[0]
		return None
		
	def updateModel(self, undo, flags):
		pass
		
	def cloneModel (self, clone):
		clone.id = self.id
		clone.game = self.game
		clone.cap = self.cap
		
	def getRankDir (self, cards=None):
		