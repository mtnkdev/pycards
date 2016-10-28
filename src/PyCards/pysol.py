from Tkinter import *
from ttk import *

from pysollib.widgets import ProgressBar, TaskMenu, window
from pysollib.control import gameManager as mgr


class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        ProgressBar.createProgressbar(root, 0.5)

    def mainloop(self):
        # Starts mainloop
        # hides main window
        # renders loading progress bar then makes main window visible

        root.deiconify()
        window.setBackground(root)
        mgr.drawGame(root)

        root.canvas.update_idletasks()

        root.mainloop()

from utilities import util
util.localize()

root = Tk()
root.geometry("800x600")
root.title("PyCards")
TaskMenu.createMenu(root)
app = App(root)
app.mainloop()

