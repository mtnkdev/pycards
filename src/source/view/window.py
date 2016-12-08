"""This module is responsible for rendering the
root window and enforcing its associated attributes and items

    State Variables:
    root: the application window

    Environment Variables:
    system display: array of pixels used for graphical output

    **Semantics**

    :func:`bind_card`:

    * transition: binds the mouse actions to the card

    :func:`create_card`:

    * transition: creates a card in the proper location and predefined attributes

    :func:`draw_card`:

    * transition: renders the card to the main window

    :func:`setBackground`:

    * transition: renders the background for the main window


    **Exported Access Programs**

    ==================   =====================================  ============
    Routine                  In                                     Out
    ==================   =====================================  ============
    bind_card               label, bindings
    create_card             canvas, stackID, cards, num, hide
    draw_card               label, x, y
    setBackground()         root
    ==================   =====================================  ============
|
|


"""

import Tkinter
import ttk
import os


def setBackground(root, path=None):
    """Draw the window background

    Exceptions thrown and handled

    * TclError

     * Missing tiles directory/files
     * Adapt by using solid color background

    """
    height = root.winfo_height()
    width = root.winfo_width()
    if hasattr(root, 'canvas'):
        root.canvas.destroy()
    root.canvas = Tkinter.Canvas(root, height=height, width=width)

    try:
        if path is None:
            tile = Tkinter.PhotoImage(file=os.path.join(os.getcwd(), "tiles/Nostalgy.gif"))
        elif os.path.isfile(path):
            tile = Tkinter.PhotoImage(file=path)
    except Tkinter.TclError:
        tile = root.canvas.create_rectangle(0, 0, width, height, fill="darkgreen")
        root.canvas.pack(fill=Tkinter.BOTH, expand=Tkinter.YES)
        root.canvas.update()
        return None
                
    root.back = tile
    for x in range(0, width, tile.width()):
        for y in range(0, height, tile.height()):
            label = Tkinter.Label(root.canvas, image=tile, borderwidth=0)
            label.place(x=x,y=y)
    root.canvas.pack(fill=Tkinter.BOTH, expand=Tkinter.YES)
    root.canvas.update()


def create_card(canvas, stackID, cards, num, hide):
    """Create a card with the desired properties"""
    if hide:
        img = cards[num].back_image()
    else:
        img = cards[num].get_image()

    label = ttk.Label(canvas, image=img, borderwidth=0)
    setattr(label, "rank", cards[num].rank)
    setattr(label, "suit", cards[num].suit)
    setattr(label, "color", cards[num].color)
    setattr(label, "stackID", stackID)
    setattr(label, "cardNum", num)
    return label


def draw_card(label, x, y):
    """Renders the card to the main window"""
    label.place(x=x, y=y)


def bind_card(label, bindings):
    """Add mouse binding(s) to the card widget"""
    if bindings is not None:
        for binding, callback in bindings.iteritems():
            label.bind(binding, callback)
