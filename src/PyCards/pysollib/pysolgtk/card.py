#!/usr/bin/env python

import gtk
from pysollib.AbstractCard import AbstractCard
from tkcanvas import MfxCanvasGroup, MfxCanavasImage

# cards that can be hidden
class _HidableCard(AbstractCard):
	def hide(self,stack):			
		if stack is self.stack_hidden_in:
			return 0
		self.item.hide()
		self.stack_hidden_in = stack
		
	def unhide (self):
		if self.hideStack is None:
			return 0
		self.item.show()
		self.hideStack = None
		return 1

		
		
# cards with a uniform back image and different face images
class _OneImageCard(_HidableCard):
	def __init__(self, id, deck, suit, rank, game, x=x, y=y):
		_HidableCard.__init__(self, id, deck, suit, rank, game, x=x, y=y)
		images = game.app.images
		self.__face_image = images.getFace(deck, suit,rank)
		self.__back_image = images.getBack()
		self.__image = MfxCanavasImage(game.canvas, self.x, self.y, images=self.__back_image, anchor=gtk.ANCHOR_NW)
		
		if 0:
			self.item = MfxCanvasGroup(game.canvas)
			self.__image.addtag(self.item)
		else:
			self.item = self.__image
			
	def showFace (self, unhide=True):
		if not self.face_up:
			self.__image.config(image = self.__face_image)
			self.tkraise(unhide)
			self.face_up = True
			
	def showBack (self, unhide=True):
		if self.face_up:
			self.__image.config(image=self.__back_image)
			self.tkraise(unhide)
			self.face_up=False
			
	def updateCardBackground(self, image):
		self.__back_image = image
		if not self.face_up:
			self.__image.config(image=image)
		

		
#cards with different back images and different front images
class _TwoImageCard(_HidableCard):
	def __init__(self, id, deck, suit, rank, game, x=0, y=0):
		_HidableCard().__init__(self, id, deck, suit, rank, game, x=x, y=y)
		images = game.app.images
		self.item=MfxCanvasGroup(game.canvas, self.x, self.y, image=image.getFace(deck, suit, rank), anchor='nw')
		self.__back = MfxCanavasImage(game.canvas, self.x, self.y, image=images.getBack(),anchor='nw')
		self.__face.addtag(self.item)
		self.__back.addtag(self.item)
		self.__face.hide()
		
	def showFace (self, unhide=True):
		if not self.face_up:
			self.__back.hide()
			self.__face.show()
			self.face_up = True
			
	def showBack (self, unhide = True):
		if self.face_up:
			self.__face.hide()
			self.__back.show()
			self.face_up = False
			
	def updateCardBackground(self,image):
		self.__back.config(image=image)
		

		
Card = _TwoImageCard