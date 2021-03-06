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

    :func:`start`:

    * transition: creates application window

"""

import sys

if sys.version_info[0] < 3:
    import Tkinter
    import ttk
else:
    import tkinter as Tkinter
    import tkinter.ttk as ttk


from ..control import taskmenu as menu
from ..control import gamemanager as mgr
from ..model import assets
from ..view import progressbar as loader
from ..view import window

__all__ = ["App", "start"]


class App:
    """This class encapsulates the main program

    This initializer takes in a Tk instance and binds it

    State variables:
    master: parent Tk instance

    Environment variables: none

    Assumptions:
    Only one instance is created per program execution

    .. automethod:: __init__

    """

    def __init__(self, master):
        """Organize Tk instance into Frame then create progress bar

        Attempt to load cardsets and their respective cards

        Exceptions thrown and caught:

        * WindowsError

         * 'cardsets' directory is missing
         * user is prompted to verify their installation and re-download
           the application
         * application terminates gracefully (instead of corrupted execution)

        """
        self.frame = ttk.Frame(master)
        self.frame.pack()
        loader.create(root, 0.5)

        try:
            assets.load_cardsets()
        except WindowsError:
            import sys
            import tkinter
            import tkMessageBox
            if tkMessageBox.showerror("Corrupt or missing files detected",
                message="The cardsets directory is missing from your installation. "
                "Please redownload and verify the integrity of your copy of the program"):
                sys.exit(-1)


def mainloop():
    """Render root window and draw first game. Then enter Tk mainloop"""
    root.deiconify()
    window.setBackground(root)
    mgr.dealgame(root)
    mgr.drawgame(root)
    root.canvas.update_idletasks()
    root.mainloop()


def start():
    """Create Tk instance and trigger the main execution loop"""
    global root
    root = Tkinter.Tk()
    root.geometry("900x600")
    root.title("PyCards")

    menu.create_menu(root)
    app = App(root)
    mainloop()

