from cardsets import CSI

#Klondike layout

class CardGame:
    pass
    #type
    #name
    #numcards
    #

    #numRows
    #row: position  base    alternate   direction

    #

from pile import Pile

class Klondike(CardGame):

    def __init__(self):
        self.type = CSI.TYPE_FRENCH
        self.name = Klondike
        self.base = 13
        self.numrows = 7
        self.numcards = 52
        self.foundations = 4
        self.alternate = True
        self.row_size = range(7)
        self.face_ups = tuple([1]*7)
        self.direction = tuple([-1]*7)


    def createPiles(self):
        self.piles = []
        self.piles.append(Pile((50, 50), -1, [], None, 24))
        self.piles.append(Pile((100 + 50, 50), -1, [], None, 0))
        for p in range(self.foundations):
            self.piles.append(Pile(((self.numrows-p+1) * 80 + 10, 50), self.base, self.direction, self.alternate, 0))
        for p in range(self.numrows):
            self.piles.append(Pile((p*100+50,250),self.base,self.direction,self.alternate,p))

k = Klondike()
k.createPiles()