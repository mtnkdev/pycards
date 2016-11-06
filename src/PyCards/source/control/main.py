import Tkinter
import ttk

from ..view import progressbar as loader
from ..view import taskmenu as menu
from ..view import window
from ..control import gamemanager as mgr
from ..model import assets


class App:

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
    root.geometry("800x600")
    root.title("PyCards")

    menu.createMenu(root)
    app = App(root)
    mainloop()
