"""This module is the secondary entry point of the application

    State Variables: 
    root: the application window

    Environment Variables: 
    system display: array of pixels used for graphical output

    Assumptions: 
    The program was launched from pysol.py in the parent directory
    Only the start method should be called from outside

    **Exported Access Programs**

    ==================   ============   ============
    Routine                  In             Out
    ==================   ============   ============
    start()
    ==================   ============   ============

    **Semantics**

    start() :
    * transition: creates application window
"""

import Tkinter
import ttk

import taskmenu as menu
from ..control import gamemanager as mgr
from ..model import assets
from ..view import progressbar as loader
from ..view import window

__all__ = ["start"]


class App:
    """This class encapsulates the main program

    This initializer takes in a Tk instance and binds it

    State variables:
    master: parent Tk instance

    Environment variables: none

    Assumptions:
    Only one instance is created per program execution

    """

    def __init__(self, master):
        """Organize Tk instance into Frame then create progress bar"""
        self.frame = ttk.Frame(master)
        self.frame.pack()
        loader.create(root, 0.5)
        assets.load_cardsets()


def mainloop():
    """Render root window and draw first game. Then enter Tk mainloop"""
    root.deiconify()
    window.setBackground(root)
    mgr.dealgame(root)
    mgr.drawgame(root)
    root.canvas.update_idletasks()
    root.mainloop()


def start():
    """Start the main execution loop"""
    global root
    root = Tkinter.Tk()
    root.geometry("900x600")
    root.title("PyCards")

    menu.create_menu(root)
    app = App(root)
    mainloop()