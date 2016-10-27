import os
from cardsets import CSI

import Tkinter
class Card:

    TEST = None

    def __init__(self, cardset, rank, suit):
        self.rank = rank
        self.suit = suit
        self.cardset = cardset

    def setImage(self):
        self.image_path = os.path.join(os.getcwd(),"cardsets")
        self.image_path = os.path.join(self.image_path, self.cardset.path)
        self.image_path = os.path.join(self.image_path, self._rankstr())
        self.image = Tkinter.PhotoImage(file=self.image_path)
        return self.image

    def _rankstr(self):
        string = str(self.rank)
        if len(string) == 1:
            string = "0" + string
        return string +self.suit+".gif"

def setRanksandSuits(cardset):
    card_type = cardset.ctype
    if card_type == CSI.TYPE_FRENCH:
        cardset.ranks = range(13)
        cardset.suits = "cshd"
    elif card_type == CSI.TYPE_HANAFUDA:
        cardset.nbottoms = 15
        cardset.ranks = range(4)
        cardset.suits = "abcdefghijkl"
    elif card_type == CSI.TYPE_TAROCK:
        cardset.nbottoms = 8
        cardset.ranks = range(14)
        cardset.suits = "cshd"
        cardset.trumps = range(22)
    elif card_type == CSI.TYPE_MAHJONGG:
        cardset.ranks = range(10)
        cardset.suits = "abc"
        cardset.trumps = range(12)
        #
        cardset.nbottoms = 0
        cardset.nletters = 0
        cardset.nshadows = 0
    elif card_type == CSI.TYPE_HEXADECK:
        cardset.nbottoms = 8
        cardset.ranks = range(16)
        cardset.suits = "cshd"
        cardset.trumps = range(4)
    elif card_type == CSI.TYPE_MUGHAL_GANJIFA:
        cardset.nbottoms = 11
        cardset.ranks = range(12)
        cardset.suits = "abcdefgh"
    elif card_type == CSI.TYPE_NAVAGRAHA_GANJIFA:
        # ???return 0                            ## FIXME
        cardset.nbottoms = 12
        cardset.ranks = range(12)
        cardset.suits = "abcdefghi"
    elif card_type == CSI.TYPE_DASHAVATARA_GANJIFA:
        cardset.nbottoms = 13
        cardset.ranks = range(12)
        cardset.suits = "abcdefghij"
    cardset.ncards = len(cardset.ranks) * len(cardset.suits)
    # elif card_type == CSI.TYPE_TRUMP_ONLY:
    #     # ???return 0                            ## FIXME
    #     # cardset.nbottoms = 7
    #     # cardset.ranks = ()
    #     # cardset.suits = ""
    #     # cardset.trumps = range(cardset.ncards)
    #     cardset.nbottoms = 1
    #     cardset.nletters = 0
    #     cardset.nshadows = 0
    #     cardset.ranks = ()
    #     cardset.suits = ""
    #     cardset.trumps = range(cardset.ncards)

##path = os.getcwd()
###print path
##
##path = os.path.join(path, "cardsets")
##
###print len(os.listdir(path))
##count = 0
##for folder in os.listdir(path):
##    if os.path.isdir(os.path.join(path,folder)):
##        print folder
##        cardset = tuple(os.walk(os.path.join(path,folder)))
##
##        #[0][0] is path, [0,1] is empty, [1,2] is filenames as list
##
##        print cardset[0][2]
##        count += 1
##        if count == 2: break

# print tuple(os.walk(path, topdown=True))
#
# for root, dirnames, filenames in os.walk(path, topdown=True):
#     if not dirnames.count("cardsets-"):
#         pass
#     else:
#         print dirnames


class Cardset:

    cardsets = {}

    def __init__(self, folder, name, ctype, width, height, style, nationality, year):
        self.path = folder
        self.name = name

        self.ranks = ()
        self.suits = ()
        self.ncards = 52

        self.ctype = ctype
        self.width = width
        self.height = height

        self.style = style
        self.nation = nationality
        self.year = year

        self.cards = []

#print os.getcwd()

path = os.getcwd()
path = os.path.join(path, "cardsets")


#cardsets = tuple(os.walk(path, topdown=True))
cardsets = os.listdir(path)
#print len(cardsets)

import re
_digit = re.compile('\d')

for folder in cardsets:
    config = os.path.join(path, folder)
    config = os.path.join(config, "config.txt")
    f = open(config, "r")
    #print folder
    text = f.readlines()
    assert len(text) >= 6
    info = text[0].split(';')

    try:
        extension = info[2]
    except IndexError:
        extension = ".gif"

    ID = text[1]

    # import re
    # m = re.search(r"^(\d+)$", info[6])
    # year = int(m.group(1))
    # print year
    #
    # styles = info[5].split(",")
    # for s in styles:
    #     m = re.search(r"^\s*(\d+)\s*$", s)
    #     if not m:
    #         break
    #     print int(m.group(1))
    #
    # keys = cardset.styles[:]
    # cardset.si.styles = tuple([s for s in keys if s in CSI.STYLE])
    # for s in cardset.si.styles:
    #     self.registered_styles[s] = self.registered_styles.get(s, 0) + 1
    # cardset.si.nationalities = tuple([s for s in keys if s in CSI.NATIONALITY])
    # for s in cardset.si.nationalities:
    #     self.registered_nationalities[s] = self.registered_nationalities.get(s, 0) + 1
    # keys = (cardset.year / 100,)
    # cardset.si.dates = tuple([s for s in keys if s in CSI.DATE])
    # for s in cardset.si.dates:
    #     self.registered_dates[s] = self.registered_dates.get(s, 0) + 1


    # import re
    # fields = [f.strip() for f in text[0].split(';')]
    # if len(fields) >= 2:
    #     match = re.search(r"^(\d+)$", fields[1])
    #     if match:
    #         version = int(match.group(1))
    #         print "Version", version
    #     else:
    #         version = 1

        ##app.py _parseCardsetConfig
    class ConfigError:
        pass

    def getTypeInfo(info):
        raise ConfigError

    try:
        ctype = int(info[3]) #cardset type (int value)
    except IndexError:
        ctype = CSI.TYPE_FRENCH

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

        # width = int(text[2].split(' ')[0])
        # height = int(text[2].split(' ')[1])

        # ranks = set()
        # suits = set()
        # for cardFile in os.listdir(os.path.join(path, folder)):
        #     if _digit.search(cardFile[0]) and _digit.search(cardFile[1]):
        #         ranks.add(cardFile[0:2])
        #         suits.add(cardFile[2])

        currCardset = Cardset(folder, name, ctype, width, height, style, nationality, year)
        Cardset.cardsets[name] = currCardset
        #ranks = (int(rank) for rank in ranks)

        # print len(tuple(ranks))
        # print len(tuple(suits))
        #
        # cards.setRanks(ranks)
        # cards.setSuits(suits)
        setRanksandSuits(currCardset)

        for rank in currCardset.ranks:
            for suit in currCardset.suits:
                currCardset.cards.append(Card(currCardset, rank+1, suit))

        ## try:
        ##     getattr(currCardset, 'trumps')
        ##     for rank in currCardset.trumps:
        ##         currCardset.
        ## except AttributeError:
        ##     currCardset.trumps = ()
        ###print name, tuple(cards.ranks), tuple(cards.suits)

        # for attr in dir(cards):
        #     print attr, getattr(cards, attr)

    except IndexError:
        print "Invalid cardset configuration for " + folder

# print len(Cardset.cardsets.items())
#
# print sorted([Cardset.cardsets[sets].path for sets in Cardset.cardsets.keys()])#sorted(Cardset.cardsets.keys())
#
# for name in [Cardset.cardsets[sets].path for sets in Cardset.cardsets.keys()]:
#     found = False
#     for file in os.listdir(path):
#         if file.count(name) != 0:
#             found = True
#     if found == False:
#         print name
