from gamedb import GAME_DB
from games import klondike
from stack import WasteStack, WasteTalonStack
import Tkinter

def play(root):
    # creates klondike instance, passes GameInfo instance carrying details
    kl = klondike.Klondike(GAME_DB.getGame("Klondike"))

    talon = WasteTalonStack(50,50,kl,max_rounds=-1,num_deal=-1)
    waste = WasteStack(100,100, kl)

    # move type 1
    def moveMove(ncards, from_stack, to_stack, frames=-1, shadow=-1):
        assert from_stack and to_stack and from_stack is not to_stack
        assert 0 < ncards <= len(from_stack.cards)
        #am = AMoveMove(ncards, from_stack, to_stack, frames, shadow)

        #self.__storeMove(am)
        #am.do(self)

    moveMove(1, talon, waste)
    print "TEST"