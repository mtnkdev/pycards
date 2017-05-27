"""This module contains the event-driven logic for the program

    State variables: None

    Environment variables:
    system display: array of pixels used for graphical output

    Assumptions: None

    **Exported Access Programs**

    ==================   ============   ============
    Routine                  In             Out
    ==================   ============   ============
    restart
    start_game             gameclass
    select_cardset
    select_tile
    showLicense
    showInfo
    ==================   ============   ============

    **Semantics**

    :func:`restart`:

    * transition:

     * destroys the game in progress
     * creates a new instance of the same game type
     * updates application window

    :func:`start_game` :

    * input: the class of the game to be created
    * transition:

     * destroys the game in progress
     * creates a new instance of the specified game type
     * updates application window

    :func:`select_cardset`:

    transition: Prompt the user to select a cardset

    :func:`select_tile`:

    transition: Prompt the user to select a background image

    :func:`showLicense`:

    output: display the license information in a new window

    :func:`showInfo`:

    output: display basic information about the program in a new window

"""

import os
import sys

if sys.version_info[0] < 3:
    import Tkinter
    import tkMessageBox
    import tkFileDialog
else:
    import tkinter
    import tkinter.messagebox as tkMessageBox
    import tkinter.filedialog as tkFileDialog

from ..control.gamemanager import dealgame, drawgame, destroy, solve
from ..model.cardsets import Cardset
from ..control.gamemanager import save_game, load
from ..view.window import setBackground


def restart():
    """Start a new instance of the same game type"""
    if tkMessageBox.askyesno("", 'Do you want to start a new game?', default="yes"):
        destroy()
        dealgame()
        drawgame()


def start_game(gameclass):
    """Start a new instance of the specified game type"""
    if tkMessageBox.askyesno("", "Do you want to start a new %(game)s game?" % \
            {"game":gameclass.name}, default="yes"):
        destroy()
        dealgame(game=gameclass)
        drawgame()


def saveGame():
    save_game()


def loadGame():
    try:
        load()
    except:
        tkMessageBox.showwarning(message="Invalid save file")


def quitGame():
    import sys
    destroy()
    sys.exit(0)
    pass

    
#####   End file commands   #####

def select_cardset():
    """Prompt the user to select the directory containing the desired cardset"""
    cardset = tkFileDialog.askdirectory(initialdir="./cardsets",title="Choose a cardset", mustexist=True)
    if os.path.isdir(cardset):
        try:
            if tkMessageBox.askyesno("", "Are you sure? This will cause you to lose all progress "
                                     "in the current game"):
                config = os.path.join(cardset, "config.txt")
                f = open(config, "r")
                text = f.readlines()
                name = (text[1].split(';'))[1].strip()
                destroy()
                dealgame(new_cardset=Cardset.cardsets[name])
                drawgame()
            else:
                tkMessageBox.showwarning(message="Invalid cardset directory")
        except IOError:
            tkMessageBox.showwarning(message="Invalid cardset directory")


def select_tile(root):
    """Prompt the user to select the desired background image"""
    tile = tkFileDialog.askopenfilename(initialdir="./tiles",title="Choose a background", multiple=False)
    if os.path.isfile(tile):
        if tkMessageBox.askyesno("", "Are you sure? This will cause you to lose all progress "
                                     "in the current game"):
            setBackground(root, path=tile)
            dealgame()
            drawgame()


def solve_game():
    solve()

#####   Help commands   #####


def showLicense():
    """Display the license information in a new window"""
    window = Tkinter.Toplevel(width=400, height=500, padx=10, pady=30, background="darkblue")
    window.canvas = Tkinter.Canvas(window, background="darkblue")
    window.canvas.pack()

    window.title("License")
    scroll = Tkinter.Scrollbar(window.canvas, takefocus=1)
    scroll.pack(side=Tkinter.RIGHT, fill=tkinter.Y)
    file = open("LICENSE","r")
    licenses = file.read()
    file.close()
    window.msg = Tkinter.Text(window.canvas, background="darkgray", relief="raised", pady=10)
    window.msg.insert(Tkinter.END, licenses)
    window.msg.tag_add("indent", 0.0, tkinter.END)
    window.msg.tag_configure("indent", lmargin1=20, lmargin2=20, background="darkgray")
    window.msg.configure(state=Tkinter.DISABLED)
    window.msg.pack()
    scroll.config(command=window.msg.yview)
    window.msg.config(yscrollcommand=scroll.set)
    window.update()


def showInfo():
    """Display a window with basic info about the application"""
    window = Tkinter.Toplevel(width=400, height=400)
    window.title("About")
