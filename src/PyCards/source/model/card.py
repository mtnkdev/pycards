#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-

import Tkinter
import os

from abc import ABCMeta, abstractmethod


class AbstractCard:
    """This is your basic template for creating cards"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, cardset, rank, suit):
        self.cardset = cardset
        self.suit = suit
        self.rank = rank
        self.show = False

    @classmethod
    def __subclasshook__(cls, subclass):
        assert hasattr(subclass, 'cardset')
        assert hasattr(subclass, 'suit')
        assert hasattr(subclass, 'rank')

    def __str__ (self):
        return "Card (%d, %d, %d)" % (self.cardset.name, self.suit, self.rank)


class StandardCard(AbstractCard):
    """This is your standard playing card.
    Each card has a cardset it belongs to, a rank and a suit
    """

    def __init__(self, cardset, rank, suit):
        """Initialize the core properties of the card"""
        self.rank = rank + 1
        self.suit = suit
        self.cardset = cardset
        self.image = None
        self.visible = False

        if self.suit in "hd":
            self.color = "red"
        else:
            self.color = "black"

    def get_image(self):
        """Return the (newly instantiated) PhotoImage for the card"""
        if self.visible:
            if self.image is None:
                self._set_image()
                return self.image
        else:
            return self.back_image()

    def _rankstr(self):
        string = str(self.rank)
        if len(string) == 1:
            string = "0" + string
        return string + self.suit

    def _set_image(self):
        """Set the image for the card"""
        path = os.path.join(os.getcwd(), "cardsets")
        path = os.path.join(path, self.cardset.path)
        path = os.path.join(path, self._rankstr())
        self.image_path = path + self.cardset.extension
        self.image = Tkinter.PhotoImage(file=self.image_path)

    def back_image(self):
        if not hasattr(self, 'back'):
            self.back = Tkinter.PhotoImage(file=self.cardset.backimage[0])
        return self.back

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True