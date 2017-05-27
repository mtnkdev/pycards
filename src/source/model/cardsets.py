"""This module is responsible for establishing the different
 types of cardsets available to the program

cardset: A set of locally-stored images to be used when rendering the cards
"""

from ..model.enum import Enum


class Cardset:
    """This class contains the identifying properties of a cardset
    At minimum path, name, type, width, and height must be defined

    .. automethod:: __init__

    """
    cardsets = {}

    def __init__(self, folder, name, _type, width, height, style, nationality, year, extension):
        """Initializer for cardset
        non-None values expected for folder, name, _type, width and height

        See :mod:`source.model.assets` for implementation details
        """
        self.extension = extension
        self.path = folder
        self.name = name

        self.backimage = []
        self.holder = None

        self.ranks = ()
        self.suits = ()
        self.ncards = 52

        self.ctype = _type
        self.width = width
        self.height = height

        self.style = style
        self.nation = nationality
        self.year = year

        self.cards = []


SIZE = Enum()

SIZE.addAll(("TINY",1, "SMALL",2, "MEDIUM",3, "LARGE",4, "XLARGE",5,))

TYPE = Enum()
TYPE.addAll(("STANDARD", 1))

# _(str) is conventionally used to allow localization

TYPEDEF = {
    1:  _("French type (52 cards)"),
    9:  _("Trumps only type (variable cards)"),
}

# Additional cardset information
# can be used for filtering in future versions

STYLE = {
    1:  _("Adult"),                #
    2:  _("Animals"),              #
    3:  _("Anime"),                #
    4:  _("Art"),                  #
    5:  _("Cartoons"),             #
    6:  _("Children"),             #
    7:  _("Classic look"),         #
    8:  _("Collectors"),           # scanned collectors cardsets
    9:  _("Computers"),            #
   10:  _("Engines"),              #
   11:  _("Fantasy"),              #
   13:  _("Holiday"),              #
   14:  _("Movies"),               #
   31:  _("Matrix"),               #
   15:  _("Music"),                #
   16:  _("Nature"),               #
   17:  _("Operating Systems"),    # e.g. cards with Linux logos
   19:  _("People"),               # famous people
   20:  _("Places"),               #
   21:  _("Plain"),                #
   22:  _("Products"),             #
   18:  _("Round cardsets"),       #
   23:  _("Science Fiction"),      #
   24:  _("Sports"),               #
   25:  _("Vehicles"),             #
   26:  _("Video Games"),          #
}

# nationality (suit and rank symbols)
NATIONALITY = {
    1021:  _("Australia"),         #
    1001:  _("Austria"),           #
    1019:  _("Belgium"),           #
    1010:  _("Canada"),            #
    1011:  _("China"),             #
    1012:  _("Czech Republic"),    #
    1013:  _("Denmark"),           #
    1003:  _("England"),           #
    1004:  _("France"),            #
    1006:  _("Germany"),           #
    1014:  _("Great Britain"),     #
    1015:  _("Hungary"),           #
    1020:  _("India"),             #
    1005:  _("Italy"),             #
    1016:  _("Japan"),             #
    1002:  _("Netherlands"),       #
    1007:  _("Russia"),            #
    1008:  _("Spain"),             #
    1017:  _("Sweden"),            #
    1009:  _("Switzerland"),       #
    1018:  _("USA"),               #
}

# creation date
DATE = {
    10:  "1000 - 1099",
    11:  "1100 - 1199",
    12:  "1200 - 1299",
    13:  "1300 - 1399",
    14:  "1400 - 1499",
    15:  "1500 - 1599",
    16:  "1600 - 1699",
    17:  "1700 - 1799",
    18:  "1800 - 1899",
    19:  "1900 - 1999",
    20:  "2000 - 2099",
    21:  "2100 - 2199",
    22:  "2200 - 2299",
}
