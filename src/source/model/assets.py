"""This module is responsible for loading and parsing the
cardset configurations available to the program

cardsets must be located in the 'cardsets' directory in the root of the
source directory
"""

import os
import Tkinter

from cardsets import TYPE, Cardset
from card import StandardCard as Card


def set_rank_and_suit(cardset):
    """Set rank and suit based on cardset type"""
    card_type = cardset.ctype

    if card_type == TYPE.STANDARD:
        cardset.ranks = range(13)
        cardset.suits = "cshd"


def load_cardsets():
    """Load and parse the various cardset configurations
    Store the cardsets but avoid loading the images until the
    cardset is in use for a game
    """
    import re
    _digit = re.compile('\d')

    # Limit scope to avoid propagation and prevent module-level import
    class ConfigError:
            pass

    def getTypeInfo(info):
        raise ConfigError

    # Compile path to cardsets
    path = os.getcwd()
    path = os.path.join(path, "cardsets")

    # Enumerate available cardsets
    cardsets = os.listdir(path)    

    # Parse, verify then attempt to load cardsets
    for folder in cardsets:
        config = os.path.join(path, folder)
        if not os.path.isdir(config):
            continue
        config = os.path.join(config, "config.txt")
        f = open(config, "r")
        text = f.readlines()
        assert len(text) >= 6
        info = text[0].split(';')

        try:
            extension = info[2]            
        except IndexError:
            extension = ".gif"

        ID = text[1]        

        try:
            ctype = int(info[3])
        except IndexError:
            ctype = TYPE.STANDARD

        try:
            if len(info) < 3:
                version = 1
                style = []
                nationality = []
                year = []
            else:
                version = info[3]
                try:
                    style, nationality, year = getTypeInfo(info)
                except ConfigError:
                    style = []
                    nationality = []
                    year = []

            name = (text[1].split(';'))[1].strip()
            width, height, depth = text[2].replace('\n', '').split(" ")
            CARD_XOFFSET, CARD_YOFFSET, SHADOW_XOFFSET, SHADOW_YOFFSET = [int(x) for x in text[3].replace('\n', '').split(" ")]
            background = text[4]
            alt_backs = text[5].replace('\n', '').split(';')
            if background in alt_backs:
                back_index = alt_backs.index(background)
            else:
                alt_backs.insert(0, background)
            version = info[1]

            # Create cardset
            currCardset = Cardset(folder, name, ctype, width, height, style, nationality, year, extension)            

            # bottom02 looks better so try that first
            imgpath = os.path.join(path, folder)
            bottom_img = os.path.join(imgpath, "bottom02" + extension)
            if not os.path.isfile(bottom_img):                    
                bottom_img = os.path.join(imgpath, "bottom01" + extension)

            # Set placeholder image for cardset
            for img in os.listdir(imgpath):
                if img.count("back"):
                    currCardset.backimage.append(os.path.join(imgpath, img))
            currCardset.holder = Tkinter.PhotoImage(file=bottom_img)
            Cardset.cardsets[name] = currCardset
            set_rank_and_suit(currCardset)

            # Enumerate and add cards to the cardset
            for rank in currCardset.ranks:
                for suit in currCardset.suits:
                    currCardset.cards.append(Card(currCardset, rank + 1, suit))

        except IndexError:
            print "Invalid cardset configuration for " + folder

