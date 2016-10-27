from Tkinter import *
from ttk import *

import __builtin__
import gettext


def ugettext(message):
    # unicoded gettext
    if not isinstance(message, unicode):
        message = unicode(message, 'utf-8')
    domain = gettext._current_domain
    try:
        t = gettext.translation(domain,
                                gettext._localedirs.get(domain, None))
    except IOError:
        return message
    return t.ugettext(message)
gettext.ugettext = ugettext


def ungettext(msgid1, msgid2, n):
    # unicoded ngettext
    if not isinstance(msgid1, unicode):
        msgid1 = unicode(msgid1, 'utf-8')
    if not isinstance(msgid2, unicode):
        msgid2 = unicode(msgid2, 'utf-8')
    domain = gettext._current_domain
    try:
        t = gettext.translation(domain,
                                gettext._localedirs.get(domain, None))
    except IOError:
        if n == 1:
            return msgid1
        else:
            return msgid2
    return t.ungettext(msgid1, msgid2, n)


gettext.ungettext = ungettext

__builtin__._ = gettext.ugettext    # use unicode
__builtin__.n_ = lambda x: x

from pysollib.widgets import ProgressBar, TaskMenu, window
from pysollib import gameplay
import pysollib.games
from pysollib import dataloader
from pysollib import gamelayout
from pysollib.gamelayout import k

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
        #dataloader.Card.TEST.setImage()
        #root.image = image = PhotoImage(file=dataloader.Card.TEST.image_path)
        ###print dataloader.Cardset.cardsets.keys()
        img = dataloader.Cardset.cardsets["Standard"].cards[0].setImage()
        root.cardimage = img #= PhotoImage(file=dataloader.Cardset.cardsets['standard'].cards[0].image_path)
        print root.cardimage
        #root.canvas.create_image(10, 10, image=image)
        ##label = Label(root.canvas, image=root.cardimage, borderwidth=0)
        ##label.place(x=20,y=20)

        for stack in k.piles:
            label = Label(root.canvas, image=root.cardimage, borderwidth=0)
            label.place(x=stack.x, y=stack.y)

        root.canvas.update_idletasks()

        root.mainloop()


root = Tk()
root.geometry("800x600")
root.title("PyCards")
TaskMenu.createMenu(root)
app = App(root)
app.mainloop()

