"""This module is the main controller and is responsible
    for the responding to events and dictating the state of the
    application

    State Variables: 
    * _root: the main window
    * _game: the game in progress

    Environment Variables: 
    system display: array of pixels used for graphical output

    Assumptions: None

    **Exported Access Programs**

    ==================   ============   ============
    Routine                  In             Out
    ==================   ============   ============
    dealgame()            root, game        None
    drawgame()              root            None
    ==================   ============   ============

    **Semantics**

    dealgame(root, game) :
    * transition: 
    a) creates a new game
    b) updates the main window
    c) triggers the dealing of cards

    drawgame(root) :
    * transition: renders the visual state of the game
"""

import os
import ttk
import tkFileDialog
import tkMessageBox

from ..control.dealer import Dealer
from ..model import cardsets
from ..model.cardsets import Cardset
from ..view.window import bind_card, create_card, draw_card

# Game imports
from ..model.games.klondike import *
from ..model.games.hanoi import *
from ..model.games.spider import *
from ..model.games.freecell import *

__all__ = ['dealgame', 'drawgame']

_game = None
_root = None


def solve():
    global _game
    global _root

    try:
        _game.solve()
    except AttributeError:
        pass
    _root.canvas.update()
    return None

def dealgame(root=None, game=None, new_cardset=None):
    """Create and setup a new game"""
    global _game
    global _root

    if root is None:
        assert _root is not None
    else:
        _root = root

    if game is None:
#        _game = Klondike()
#        _game = Hanoi(4)
        _game = Spider()
#        _game = FreeCell()
    else:
        _game = None
        _game = game()
        _root.canvas.update()

    if new_cardset is None:
        new_cardset = cardsets.Cardset.cardsets["Standard"]
    _game.cardset = new_cardset
    dealer = Dealer(_game, _game.cardset)

    _game.create()
    if hasattr(_game, 'startDeal'):
        _game.startDeal(new_cardset)
        return None

    dealer.cardgen()
    dealer.dealCards()


def drawgame(root=None):
    """Render the state of the newly created game to the system display"""
    global _game
    global _root
    if root is None:
        root = _root
    stackID = 0
    for stack in _game.stacks:
        stack.holder = ttk.Label(root.canvas, image=_game.cardset.holder, borderwidth=0)
        if stack.isdeck:
            setattr(stack.holder, "stackID", stack.ID)
            setattr(stack.holder, "cardNum", -1)
            from ..model.mouse_handler import Bindings
            bind_card(stack.holder, {"<ButtonRelease-1>": lambda event: Bindings.default_move(_game._bindings, event)})
        stack.holder.place(x=stack.x,y=stack.y)
        for num in range(len(stack.cards)):
            hide = False
            try:
                if stack.positions[num] < 0:
                    hide = True
            except IndexError:
                pass
            label = create_card(root.canvas, stackID, stack.cards, num, hide)
            draw_card(label, stack.x, stack.y + stack.offset*num)
            bind_card(label, _game.bindings())
            stack.cardWidgets[num] = label
        stackID += 1
    return None


def destroy():
    """De-allocate widgets and destroy the current game"""
    global _root
    global _game
    for stack in _game.stacks:
        for card in stack.cardWidgets:
            card.destroy()
        stack.holder.destroy()
    _game.stacks = []
    _game = None
    _root.update()


_data = ""

def _write(*args):
    global _data
    if args is not None:
        _data += ''.join(args)

def _flush():
    global _data
    tile = tkFileDialog.asksaveasfilename(initialdir="./saves",title="Choose a filename")
    f = open(tile, 'w')
    f.write(_data)
    f.close()
        

def save_game():
    global _game
    self = _game
    _write(self.name, '_', str(len(self.stacks)), '_', self.cardset.name)
    for i in range(len(self.stacks)):
        _write("{:02x}".format(len(self.stacks[i].cards)))

    for i in range(len(self.stacks)):
        stack = self.stacks[i]
        for j in range(len(stack.cards)):        
            card = stack.cards[j]
            _write("{:02x}".format(card.rank), card.suit, str(int(card.visible)))
    _flush()

def load():
    import re
    filename = tkFileDialog.askopenfilename(initialdir="./saves",title="Choose a save file", multiple=False)
    if not os.path.isfile(filename):
        return

    f = open(filename, 'r')
    data = f.read()
    f.close()
    
    data = data.split("_")
    game_name = data[0]
    numrows = int(data[1])
    cardset = re.split("\d+", data[2])[0]
    offset = len(cardset)
    stack_data = data[2][offset:]

    size = []
    for i in range(numrows):
        size.append(int("0x" + stack_data[2*i:2*i+2], 16))
    offset += 2*numrows

    stacks = []
    for i in range(numrows):
        stacks.append([])
        for j in range(size[i]):
            rank = int("0x" + data[2][offset:offset+2], 16) - 1
            suit = data[2][offset+2]
            visible = data[2][offset+3]
            stacks[i].append([rank, suit, visible])
            offset += 4
    if tkMessageBox.askyesno("Continue", "Are you sure? This will cause you to lose all progress "
                         "in the current game"):
        load_game(game_name, cardset, stacks)
            
    
def load_game(game_name, cardset, stacks):
    global _game
    destroy()
    game = DB.get_game(game_name)
    _game = game()
    _game.create()
    _game.cardset = Cardset.cardsets[cardset]

    for i in range(len(_game.stacks)):
        _game.stacks[i].cards = []
        for j in range(len(stacks[i])):
            _game.stacks[i].cards.append(StandardCard(_game.cardset, stacks[i][j][0], stacks[i][j][1]))
            _game.stacks[i].cards[j].visible = stacks[i][j][2]
        _game.stacks[i].cardWidgets = [0] * len(stacks[i])
    drawgame()
    _game.update()
