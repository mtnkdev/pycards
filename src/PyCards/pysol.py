import Tkinter
import ttk

from pysollib.widgets import progressbar as loader
from pysollib.widgets import taskmenu, window
from pysollib.control import gamemanager as mgr

from utilities import util


class App:

    def __init__(self, master):
        """Organize Tk instance into Frame then create progress bar"""
        self.frame = ttk.Frame(master)
        self.frame.pack()
        loader.createProgressbar(root, 0.5)


def mainloop():
    """Render root window and draw first game. Then enter Tk mainloop"""
    root.deiconify()
    window.setBackground(root)
    mgr.dealgame(root)
    mgr.drawgame(root)
    root.canvas.update_idletasks()
    root.mainloop()

util.localize()
root = Tkinter.Tk()
root.geometry("800x600")
root.title("PyCards")

taskmenu.createMenu(root)
app = App(root)
mainloop()

