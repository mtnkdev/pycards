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
		mapkey = (x,y)
		game.stackmap[mapkey] = id
		self.init_coord (x,y)
		
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
		
	def setRestrictions(self, restrictions):
		self.suitRestrict	= restricitons[0]
		self.colourRestrict	= restricitons[1]
		self.rankRestrict	= restricitons[2]
		self.baseSuit		= restricitons[3]
		self.baseColour		= restricitons[4]
		self.baseRank		= restricitons[5]
		self.direction		= restricitons[6]
		self.mod			= restricitons[7]
		self.maxMove		= restricitons[8]
		self.maxAccept		= restricitons[9]
		self.maxCards		= restricitons[10]
		self.minMove		= restricitons[11]
		self.minAccept		= restricitons[12]
		self.minCards		= restricitons[13]
		
	def getRestrictions(self):
		restrictions.append(self.suitRestrict)
		restrictions.append(self.colourRestrict)
		restrictions.append(self.rankRestrict)
		restrictions.append(self.baseSuit)
		restrictions.append(self.baseColour)
		restrictions.append(self.baseRank)
		restrictions.append(self.direction)
		restrictions.append(self.mod)
		restrictions.append(self.maxMove)
		restrictions.append(self.maxAccept)
		restrictions.append(self.maxCards)
		restrictions.append(self.minMove)
		restrictions.append(self.minAccept)
		restrictions.append(self.minCards)
	
	def addCard(self, card):
		self.cards.append(card)
		
	def insertCard(self, card, position):
		self.cards.insert(position, card)
	
	def removeCard (self, card=None):
		assert len(cards)>0
		if card is None:
			card=cards[-1]
			del self.cards[-1]
		else:
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
		clone.setRestrictions(self.getRestrictions)
		
	def getRankDir (self, cards=None):
		if cards is None:
			cards = self.cards[-2:]
		if len (cards) <2:
			return 0
		dir = (cards[-1].rank - cards [-2].rank) % self.mod
		if dir > self.mod / 2:
			return dir - self.mod
		return dir
		
	def basicIsBlocked (self):
		return False
	
	def basicAcceptCards(self, from_stack, cards):
		if from_stack is self or self.basicIsBlocked():
			return False
		l = len (cards)
		if l < self.minAccept or l > self.maxAccept:
			return False
		l = l+len(self.cards)
		if l > self.maxCards:
			return False
		for card in cards:
			if not card.faceUp:
				return False
			if self.suitRestrict >=0 and card.suit != self.suitRestrict:
				return False
			if self.colourRestrict >= 0 and card.colour != self.colourRestrict:
				return False
			if self.rankRestrict >= 0 and card.rank != self.rankRestrict:
				return False
		if self.cards:
			return self.cards[-1].faceUp #top cards of stack has to be face up
		else:
			topCard = cards[0]
			if self.baseSuit >= 0 and card.suit != self.baseSuit:
				return False
			if self.baseColour >= 0 and card.colour != self.baseColour:
				return False
			if self.baseRank >= 0 and card.rank != self.baseRank:
				return False
			return True
			
	def basicCanMoveCards (self, cards):
		if self.basicIsBlocked():
			return False
		l = len(cards)
		if l < self.minMove or l > self.maxMove:
			return False
		l - len (self.cards)-1
		if l < self.minCards:
			return False
		return cardsFaceUp(cards)
		
	def acceptCards(self, fromStack, cards):
		return False
	
	def canMoveCards(self,cards):
		return False
		
	def canFlipCard(self):
		return False
		
	def canDropCards (self,stacks):
		return (None, 0)
		
	def __repr__(self):
		return "%s(%d)" % (self.__class__.__name__, self.id)

	def flipMove(self, animation=False):
		if animation:
			self.game.singleFlipMove(self)
		else:
			self.game.flipMove(self)
			
	def moveMove(self, ncards, toStack, frames=-1, shadows=-1):
		self.game.moveMove(ncards, self, Stack, frames=frames, shadow=shadow)
		self.fillStack()
	
	def fillStack(self):
		self.game.fillStack(self)
		
	def closeStack(self):
		pass
	
	def playFlipMove(self, sound=True, animation=False):
		if sound:
			self.game.playSample("flip",5)
		self.flipMove(animation=animation)
		if not self.game.checkForWin():
			self.game.autoPlay()
		self.game.finishMove()
		
	def playMoveMove (self, ncards, toStack, frames=-1, shadow=-1, sound=True):
		if sound:
			if to_stack in self.game.s.foundations:
				pass