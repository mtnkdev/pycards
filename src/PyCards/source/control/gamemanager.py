"""This module is the main controller and is responsible
    for the responding to events and dictating the state of the
    application

    State Variables: |
    * _root: the main window
    * _game: the game in progress

    Environment Variables: |
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
    * transition: |
    a) creates a new game
    b) updates the main window
    c) triggers the dealing of cards

    drawgame(root) :
    * transition: renders the visual state of the game
"""

import ttk

from ..control.dealer import Dealer
from ..model import cardsets
from ..view.window import bind_card, create_card, draw_card

# Game imports
from ..model.games.klondike import *
from ..model.games.hanoi import *
from ..model.games.spider import *
from ..model.games.freecell import *

__all__ = ['dealgame', 'drawgame']

_game = None
_root = None


def dealgame(root=None, game=None):
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
#        _game = Spider()
        _game = FreeCell()
    else:
        _game = None
        _game = game()
        _root.canvas.update()

    cardset = cardsets.Cardset.cardsets["Standard"]
    _game.cardset = cardset
    dealer = Dealer(_game, cardset)
    _game.create()
    if hasattr(_game, 'startDeal'):
        _game.startDeal(cardset)
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