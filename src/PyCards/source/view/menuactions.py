import Tkinter
import tkMessageBox

from ..control.gamemanager import dealgame

#####   File menu commands #####

def startGame(gameclass):
    if tkMessageBox.askyesno("", "Do you want to start a new game?", default="yes"):
        dealgame(game=gameclass)

def saveGame():
    pass

def loadGame():
    pass

def quitGame():
    pass

def showGames():
    pass
    
    
def cardset():
    import tkFileDialog
    tkFileDialog.askdirectory(initiadir="./cardsets",title="Choose a cardset", mustexist=True)

#####   End file commands   #####


#####   Help commands   #####

def showContents():
    pass

def showGuide():
    pass

def showRules():
    pass

def showLicense():
    window = Tkinter.Toplevel(width=400, height=500, padx=10, pady=30, background="darkblue")
    window.canvas = Tkinter.Canvas(window, background="darkblue")
    window.canvas.pack()

    window.title("License")
    scroll = Tkinter.Scrollbar(window.canvas, takefocus=1)
    scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
    file = open("LICENSE","r")
    licenses = file.read()
    file.close()
    window.msg = Tkinter.Text(window.canvas, background="darkgray", relief="raised", pady=10)
    window.msg.insert(Tkinter.END, licenses)
    window.msg.tag_add("indent", 0.0, Tkinter.END)
    window.msg.tag_configure("indent", lmargin1=20, lmargin2=20, background="darkgray")
    window.msg.configure(state=Tkinter.DISABLED)
    window.msg.pack()
    scroll.config(command=window.msg.yview)
    window.msg.config(yscrollcommand=scroll.set)
    window.update()

def showInfo():
    window = Tkinter.Toplevel(width=400, height=400)
    window.title("About")
