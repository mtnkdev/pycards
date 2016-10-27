import Tkinter
import os


def setBackground(root):
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
