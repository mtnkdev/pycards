from Tkinter import *
from ttk import *

from pysollib.widgets import ProgressBar, TaskMenu
from pysollib import dataloader

class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        #Style().theme_use("xpnative")

    def mainloop(self):
        # Starts mainloop
        # hides main window
        # renders loading progress bar then makes main window visible
        root.after(0, root.withdraw)
        root.after(0, ProgressBar.createProgressbar(root, 0.5))
        root.mainloop()


root = Tk()
root.geometry("800x600")
root.title("PyCards")
TaskMenu.createMenu(root)
app = App(root)
app.mainloop()

