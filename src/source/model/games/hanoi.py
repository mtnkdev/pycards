"""Defines the rules and properties of the hanoi game

	State Variables: none

    Environment Variables: none

    Assumptions: none

"""

from ..gamelayout import CardGame
from ..cardsets import TYPE
from ..card import StandardCard
from ..stack import Stack
from ..database import DB


class Hanoi(CardGame):

    name = "Hanoi"

    def __init__(self, num_cards=4):
        """Initialize standard properties of a 4-card Hanoi game

        Hanoi games are card-based representations of the well-known
        Tower of Hanoi logic puzzle
        """
        self.type = TYPE.STANDARD
        self.name = "Hanoi" + str(num_cards)
        self.deckID = -1
        self.wasteID = -1
        self.stacks = []
        self.numrows = 3
        self.numcards = num_cards
        self.foundations = 0

     # Stack(id, x, y, base, alternate, direction, pos, accept = True)
    def create(self):
        """Create the stacks (left, middle, right) for the Hanoi game"""
        self.stacks.append(Stack(0, 150, 250, -1, False, -1, [1]*self.numcards, True, offset=15))
        self.stacks.append(Stack(0, 350, 250, -1, False, -1, [], True, offset=15))
        self.stacks.append(Stack(0, 550, 250, -1, False, -1, [], True, offset=15))
        self._init_bindings()

    def _init_bindings(self):
        """Initialize mouse bindings"""
        from ..mouse_handler import Bindings
        self._bindings = Bindings(self)
        self._bindings.add("<B1-Motion>", lambda event: Bindings.default_drag(self._bindings, event))
        self._bindings.add("<ButtonRelease-1>", lambda event: Bindings.default_move(self._bindings, event))

    def startDeal(self, cardset):
        """Perform initial deal of cards"""
        for rank in range(0,self.numcards):
            self.stacks[0].cards[rank] = (StandardCard(cardset, 4-rank-1, "h"))
            self.stacks[0].cards[rank].show()

    def valid_drop(self, stackID, destID, cardNum):
        """Indicate whether the selected cards can be moved to the destination stack"""
        if len(self.stacks[destID].cards) == 0:
            return True
        card = self.stacks[stackID].cards[cardNum]
        if self.stacks[destID].cards[-1].rank < card.rank:
            return False
        return True

    def solve(self):
        return None
        from ..stack import move_cards
        _start = ("start", self.stacks[0].cards)
        _spare = ("spare", self.stacks[1].cards)
        _dest = ("dest", self.stacks[2].cards)

        def move(self, start, end, card):
            if start == "start":
                startID = 0
            elif start == "spare":
                startID = 1
            else:
                startID = 2
            if end == "start":
                endID = 0
            elif end == "spare":
                endID = 1
            else:
                endID = 2
            move_cards(self, startID, endID, card)
            print('Moved disk', card, ' from ', startID, ' to ', endID)  # Move the N disk

        def h1(disk, start=_start, end=_spare, middle=_dest):
            if disk > 0:
                h1(disk - 1, start, middle, end)
                print('Move disk' + str(disk) + ' from ' + start[0] + ' to ' + end[0])  # Move the N disk
                move(self, start[0], end[0], disk)
                h1(disk - 1, middle, end, start)

        def doH(n=self.numcards, start=_start, dest=_dest, spare=_spare):

            if n == 1:
                if len(_dest[1]) == 1:
                    print "done"
                else:
                    if len(_start[1]) == 1:
                        h1(1)
                    else:
                        h1(1, _spare, _dest, _start)
            elif n > 1:
                i = 1
                j = 2
                while i < n and j <= n:
                    start = ""
                    for tower in [_start, _spare, _dest]:
                        for t in tower[1]:
                            print t.rank
                            if i == t.rank:
                                start = tower
                                break
                        if start != "":
                            break
                    if start == "":
                        continue
                    else:
                        while j <= n:
                            dest = ""
                            for tower1 in [_start, _spare, _dest]:
                                for t in tower1[1]:
                                    if j == t.rank:
                                        if tower1[0] == start[0]:
                                            j += 1
                                            break
                                        else:
                                            dest = tower1
                                            for pole in [_start, _spare, _dest]:
                                                if pole[0] != start[0] and pole[0] != dest[0]:
                                                    spare = pole
                                if tower1[0] == start[0]:
                                    break
                            if dest != "" or (j == n and tower1[0] == start[0]):
                                if j != n:
                                    h1(j, start, dest, spare)
                                    start = []
                                    for each in dest:
                                        start.append(each)
                                if j == n:
                                    if start[0] == "start":
                                        h1(j, _start, _dest, _spare)
                                    elif start[0] == "spare":
                                        h1(j, _spare, _dest, _start)
                                    else:
                                        print "Tower of Hanoi Complete"
                                        break
                                j += 1
                    if j == n:
                        if start[0] == "start":
                            h1(j, _start, _dest, _spare)
                        elif start[0] == "spare":
                            h1(j, _spare, _dest, _start)
                        else:
                            print "Tower of Hanoi Complete"
                            break
        doH()

    def update(self):
        return self.check_win()

    def check_win(self):
        if len(self.stacks[2].cards) < self.numcards:
            return False
        return True


    def bindings(self):
        """defines mouse bindings for game"""
        return self._bindings.value()

    def deal(self):
        """No in-game deals present in Hanoi games"""
        pass

DB.add_game("Hanoi4", Hanoi)
