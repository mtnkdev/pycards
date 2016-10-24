
def _(msg):
    return msg

# ************************************************************************
# * Cardset
# ************************************************************************

# CardsetInfo constants
class CSI:
    # cardset size
    SIZE_TINY   = 1
    SIZE_SMALL  = 2
    SIZE_MEDIUM = 3
    SIZE_LARGE  = 4
    SIZE_XLARGE = 5

    # cardset types
    TYPE_FRENCH   = 1
    TYPE_HANAFUDA = 2
    TYPE_TAROCK   = 3
    TYPE_MAHJONGG = 4
    TYPE_HEXADECK = 5
    TYPE_MUGHAL_GANJIFA = 6
    TYPE_NAVAGRAHA_GANJIFA = 7
    TYPE_DASHAVATARA_GANJIFA = 8
    TYPE_TRUMP_ONLY = 9

    TYPE = {
        1:  _("French type (52 cards)"),
        2:  _("Hanafuda type (48 cards)"),
        3:  _("Tarock type (78 cards)"),
        4:  _("Mahjongg type (42 tiles)"),
        5:  _("Hex A Deck type (68 cards)"),
        6:  _("Mughal Ganjifa type (96 cards)"),
        7:  _("Navagraha Ganjifa type (108 cards)"),
        8:  _("Dashavatara Ganjifa type (120 cards)"),
        9:  _("Trumps only type (variable cards)"),
    }

    TYPE_NAME = {
        1:  _("French"),
        2:  _("Hanafuda"),
        3:  _("Tarock"),
        4:  _("Mahjongg"),
        5:  _("Hex A Deck"),
        6:  _("Mughal Ganjifa"),
        7:  _("Navagraha Ganjifa"),
        8:  _("Dashavatara Ganjifa"),
        9:  _("Trumps only"),
    }

    TYPE_ID = {
        1: "french",
        2: "hanafuda",
        3: "tarock",
        4: "mahjongg",
        5: "hex-a-deck",
        6: "mughal-ganjifa",
        7: "navagraha-ganjifa",
        8: "dashavatara-ganjifa",
        9: "trumps-only",
    }

    # cardset styles
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
       30:  _("Ganjifa"),              #
       12:  _("Hanafuda"),             #
       29:  _("Hex A Deck"),           #
       13:  _("Holiday"),              #
       28:  _("Mahjongg"),             #
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
       27:  _("Tarock"),               #
       25:  _("Vehicels"),             #
       26:  _("Video Games"),          #
    }

    # cardset nationality (suit and rank symbols)
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

    # cardset creation date
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
