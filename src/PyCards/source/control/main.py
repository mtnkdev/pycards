import Tkinter
import ttk

import taskmenu as menu
from ..control import gamemanager as mgr
from ..model import assets
from ..view import progressbar as loader
from ..view import window


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
    root.geometry("900x600")
    root.title("PyCards")

    menu.create_menu(root)
    app = App(root)
    mainloop()
