import os

path = os.getcwd()
#print path

path = os.path.join(path, "cardsets")

#print len(os.listdir(path))
count = 0
for folder in os.listdir(path):
    if os.path.isdir(os.path.join(path,folder)):
        print folder
        cardset = tuple(os.walk(os.path.join(path,folder)))

        #[0][0] is path, [0,1] is empty, [1,2] is filenames as list

        print cardset[0][2]
        count += 1
        if count == 2: break

# print tuple(os.walk(path, topdown=True))
#
# for root, dirnames, filenames in os.walk(path, topdown=True):
#     if not dirnames.count("cardsets-"):
#         pass
#     else:
#         print dirnames

class Cardset:

    def __init__(self):
        self.TYPE = [][0]

SUITS = {"FRENCH": ["a", "c", "h", "s"],
         "HANAFUDA": ["a", "c", "h", "s"],
         "TAROCK": ["a", "c", "h", "s"],
         "MAHJONGG": ["a", "c", "h", "s"],

         }

#return suit tuple
def getSuits(cardType):
    return cardType.suits

#return ranks tuple
def getRanks(cardType):
    return cardType.ranks

