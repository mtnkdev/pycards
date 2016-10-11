from Tkinter import *
#from Tkinter import ttk
from ttk import *

import TaskMenu

class App:

    def __init__(self, master):
        Style().theme_use("xpnative")

        frame = Frame(master)
        frame.pack()

        Style().theme_use("alt")

root = Tk()
root.geometry("600x680-300+0")
TaskMenu.createMenu(root)
app = App(root)

root.mainloop()
# root.destroy()
