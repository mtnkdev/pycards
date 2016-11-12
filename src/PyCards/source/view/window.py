"""This module is responsible for rendering the
root window and enforcing its associated attributes and items"""

import Tkinter
import ttk
import os


def setBackground(root):
    """Draw the window background"""
    height = root.winfo_height()
    width = root.winfo_width()
    root.canvas = Tkinter.Canvas(root, height=height, width=width)

    tile = Tkinter.PhotoImage(file=os.path.join(os.getcwd(), "tiles/Nostalgy.gif"))
    root.back = tile

    for x in range(0, width, tile.width()):
        for y in range(0, height, tile.height()):
            label = Tkinter.Label(root.canvas, image=tile, borderwidth=0)
            label.place(x=x,y=y)
    root.canvas.pack(fill=Tkinter.BOTH, expand=Tkinter.YES)
    root.canvas.update()


def create_card(canvas, stackID, cards, num, hide):
    if hide:
        img = cards[num].back_image()
    else:
        img = cards[num].get_image()
    print hide
    print stackID
    label = ttk.Label(canvas, image=img, borderwidth=0)
    setattr(label, "rank", cards[num].rank)
    setattr(label, "suit", cards[num].suit)
    setattr(label, "color", cards[num].color)
    setattr(label, "stackID", stackID)
    setattr(label, "cardNum", num)
    return label


def draw_card(label, x, y):
    label.place(x = x, y = y)


def bind_card(label, bindings):
    if bindings is not None:
        for binding, callback in bindings.iteritems():
            label.bind(binding, callback)