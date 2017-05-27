"""This module is responsible for loading and parsing the
cardset configurations available to the program

cardsets must be located in the 'cardsets' directory in the root of the
source directory
"""

import os

import sys
if sys.version_info[0] < 3:
    import Tkinter
else:
    import tkinter as Tkinter

from ..model.cardsets import TYPE, Cardset#from cardsets import TYPE, Cardset
from ..model.card import StandardCard as Card#from card import StandardCard as Card

CARDSET_DIR = "cardsets"
CONFIG_FILE = "config.txt"
DEFAULT_EXTENSION = ".gif"
PLACEHOLDER_PREFIX = "bottom02"
ALT_PLACEHOLDER_PREFIX = "bottom01"
REVERSE_IMG_PREFIX = "back"
DEFAULT_CARD_TYPE = TYPE.STANDARD
DEFAULT_SUITS = "cshd"
DEFAULT_RANKS = range(13)


def set_rank_and_suit(cardset):
    """Set rank and suit based on cardset type"""
    card_type = cardset.ctype

    # Allows for easier addition of additional types
    if card_type == TYPE.STANDARD:
        cardset.ranks = DEFAULT_RANKS
        cardset.suits = DEFAULT_SUITS


def load_cardsets():
    """Load and parse the various cardset configurations

    Store the cardsets but avoid loading the images until the
    cardset is in use for a game

    """

    # Limit scope to avoid propagation and prevent module-level import
    class ConfigError(Exception):
            pass

    def getTypeInfo(info):
        raise ConfigError

    # Compile path to cardsets
    path = os.getcwd()
    path = os.path.join(path, CARDSET_DIR)

    # Enumerate available cardsets
    cardsets = os.listdir(path)    

    # Parse, verify then attempt to load cardsets
    for folder in cardsets:
        config = os.path.join(path, folder)
        if not os.path.isdir(config):
            continue
        config = os.path.join(config, CONFIG_FILE)
        f = open(config, "r")
        text = f.readlines()
        assert len(text) >= 6
        info = text[0].split(';')

        # Load image extension type
        try:
            extension = info[2]            
        except IndexError:
            extension = DEFAULT_EXTENSION

        # Load card type
        try:
            ctype = int(info[3])
        except IndexError:
            ctype = DEFAULT_CARD_TYPE

        # Parse additional properties and create cardset
        try:
            if len(info) < 3:
                style = []
                nationality = []
                year = []
            else:
                try:
                    style, nationality, year = getTypeInfo(info)
                except ConfigError:
                    style = []
                    nationality = []
                    year = []

            name = (text[1].split(';'))[1].strip()
            width, height, depth = text[2].replace('\n', '').split(" ")

            # Create cardset
            currCardset = Cardset(folder, name, ctype, width, height, style, nationality, year, extension)            

            # Set stack placeholder img
            # bottom02 looks better so try that first
            imgpath = os.path.join(path, folder)
            bottom_img = os.path.join(imgpath, PLACEHOLDER_PREFIX + extension)
            if not os.path.isfile(bottom_img):                    
                bottom_img = os.path.join(imgpath, ALT_PLACEHOLDER_PREFIX + extension)

            # Set card reverse image for cardset
            for img in os.listdir(imgpath):
                if img.count(REVERSE_IMG_PREFIX):
                    currCardset.backimage.append(os.path.join(imgpath, img))
            currCardset.holder = Tkinter.PhotoImage(file=bottom_img)
            Cardset.cardsets[name] = currCardset
            set_rank_and_suit(currCardset)

            # Enumerate and add cards to the cardset
            # Overrule zero-indexing of ranks
            for rank in currCardset.ranks:
                for suit in currCardset.suits:
                    currCardset.cards.append(Card(currCardset, rank + 1, suit))

        except IndexError:
            pass
            #print "Invalid cardset configuration for " + folder

