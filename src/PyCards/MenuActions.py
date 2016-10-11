import Tkinter

#####   File menu commands #####

def startNew():
    pass


def listRecent():
    pass


def listGames():
    pass


def listFavorite():
    pass


def addFavorite():
    pass


def delFavorite():
    pass


def saveGame():
    pass


def loadGame():
    pass


def quitGame():
    pass


def showGames():
    pass

#####   End file commands   #####


#####   Help commands   #####

def showContents():
    pass

def showGuide():
    pass

def showRules():
    pass

def showLicense():
    window = Tkinter.Toplevel()
    ### window.title = "License"
    file = open("LICENSE.txt","r")
    license = file.read()
    pass

def showInfo():
    window = Tkinter.Toplevel()
    ### window.title = "About"
    pass