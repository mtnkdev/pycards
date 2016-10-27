import os

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

    def __init__(self, folder, name, ctype, width, height, style, nationality, year):
        self.path = folder
        self.name = name
        self.ctype = ctype
        self.width = width
        self.height = height

        self.style = style
        self.nation = nationality
        self.year = year

#print os.getcwd()

path = os.getcwd()
path = os.path.join(path, "cardsets")


#cardsets = tuple(os.walk(path, topdown=True))
cardsets = os.listdir(path)
#print len(cardsets)

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
    # keys = cs.styles[:]
    # cs.si.styles = tuple([s for s in keys if s in CSI.STYLE])
    # for s in cs.si.styles:
    #     self.registered_styles[s] = self.registered_styles.get(s, 0) + 1
    # cs.si.nationalities = tuple([s for s in keys if s in CSI.NATIONALITY])
    # for s in cs.si.nationalities:
    #     self.registered_nationalities[s] = self.registered_nationalities.get(s, 0) + 1
    # keys = (cs.year / 100,)
    # cs.si.dates = tuple([s for s in keys if s in CSI.DATE])
    # for s in cs.si.dates:
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
        ctype = info[3] #cardset type (int value)
    except IndexError:
        ctype = 'French'

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

        cards = Cardset(folder, name, ctype, width, height, style, nationality, year)

        # for attr in dir(cards):
        #     print attr, getattr(cards, attr)

    except IndexError:
        print "Invalid cardset configuration for " + folder
    #break


