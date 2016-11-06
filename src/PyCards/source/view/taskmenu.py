from Tkinter import Menu

import menuactions as Action
from ..model.database import DB


def createMenu(root):
    # Create menubar widget
    menubar = Menu(root)

    # Add menubar to root window
    root.config(menu=menubar)

    _createFileMenu(menubar)
    _createSelectMenu(menubar)  ##Look at _addSelectGameMenu in menubar.py
    _createEditMenu(menubar)
    _createGameMenu(menubar)
    _createAssistMenu(menubar)
    _createOptionMenu(menubar)
    _createHelpMenu(menubar)

def _addMenuGames(menu, games, command=None):
    for game in sorted(games, key=lambda game : game.name):
        cmd = lambda args=game: Action.startGame(game)
        menu.add_command(label=game.name, command=cmd)

def _addMenuGameType(menu, label, gameSet=None):

    if (gameSet == None) or (gameSet != None and len(gameSet) > 0):
        submenu = Menu(menu, tearoff=0)
        menu.add_cascade(label=label, menu=submenu)

        if gameSet == None:
            return submenu      # Child is another cascading menu
        elif len(gameSet) > 0:
            _addMenuGames(submenu, gameSet) # Adds games belonging to type

def _createFileMenu(menubar):
    # Creates a submenu (another Menu instance)
    # tearoff stops menu floating
    fileMenu = Menu(menubar, tearoff=0)

    # Adds dropdown menu
    menubar.add_cascade(label="File", menu=fileMenu)

    # Adds selectable dropdown items
    # @command is a pointer to function
    fileMenu.add_command(label="New", command=lambda: Action.startGame())
    fileMenu.add_command(label="Load...", command=Action.loadGame)
    fileMenu.add_command(label="Save...", command=Action.saveGame)
    fileMenu.add_command(label="Exit", command=Action.quitGame)


def _createSelectMenu(menubar):
    # Creates a submenu (another Menu instance)
    # tearoff stops menu floating
    selectMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Select", menu=selectMenu)

    selectMenu.add_command(label="All Games...", command=Action.showGames)

    _addMenuGameType(selectMenu, "Freecell", get_games("Freecell"))
    _addMenuGameType(selectMenu, "Hanoi", get_games("Hanoi"))
    _addMenuGameType(selectMenu, "Klondike", get_games("Klondike"))
    _addMenuGameType(selectMenu, "Memory", get_games("Memory"))
    _addMenuGameType(selectMenu, "Spider", get_games("Spider"))
##    freecell = Menu(selectMenu, tearoff=0)
##    selectMenu.add_cascade(label="Freecell", menu=freecell)
##    for game in get_games("Freecell"):
##        freecell.add_command(label=game.name, command=lambda args=game: Action.startGame(game))
##    
##    
##    hanoi = Menu(selectMenu, tearoff=0)
##    selectMenu.add_cascade(label="Hanoi", menu=hanoi)
##    for game in get_games("Hanoi"):
##        hanoi.add_command(label=game, command=lambda args=game: Action.startGame(game))
##    
##    klondike = Menu(selectMenu, tearoff=0)
##    selectMenu.add_cascade(label="Klondike", menu=klondike)
##    for game in get_games("Klondike"):
##        klondike.add_command(label=game, command=lambda args=game: Action.startGame(game))
##    
##    memory = Menu(selectMenu, tearoff=0)
##    selectMenu.add_cascade(label="Memory", menu=memory)
##    for game in get_games("Memory"):
##        memory.add_command(label=game, command=lambda args=game: Action.startGame(game))
##    
##    spider = Menu(selectMenu, tearoff=0)
##    selectMenu.add_cascade(label="Spider", menu=spider)
##    for game in get_games("Spider"):
##        spider.add_command(label=game, command=lambda args=game: Action.startGame(game))


def get_games(gametype):
    return [game for game in DB.get_games() if game.name.count(gametype) > 0]



def _createEditMenu(menubar):
    editMenu = Menu(menubar, tearoff=0)
    editMenu.add_command(label="Undo", command=None)
    editMenu.add_command(label="Redo", command=None)
    editMenu.add_command(label="Redo All", command=None)
    editMenu.add_command(label="Restart", command=None)
    pass


def _createGameMenu(menubar):
    gameMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Game", menu=gameMenu)
    gameMenu.add_command(label="Deal Cards", command=None)
    gameMenu.add_command(label="Auto Drop", command=None)
    gameMenu.add_command(label="Pause", command=None)
    gameMenu.add_command(label="Status", command=None)
    gameMenu.add_command(label="Statistics", command=None)
    pass


def _createAssistMenu(menubar):
    assistMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Assist", menu=assistMenu)
    assistMenu.add_command(label="Hint", command=None)
    assistMenu.add_command(label="Highlight piles", command=None)
    assistMenu.add_command(label="Find Card", command=None)
    pass


def _createOptionMenu(menubar):
    optionMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Sound", command=None)
    optionMenu.add_command(label="Cardset", command=Action.select_cardset)
    optionMenu.add_command(label="Table Tile", command=None)
    optionMenu.add_cascade(label="Card Background", command=None)
    optionMenu.add_cascade(label="Card View", command=None)
    optionMenu.add_cascade(label="Animations", command=None)
    optionMenu.add_cascade(label="Mouse", command=None)
    optionMenu.add_command(label="Fonts", command=None)
    optionMenu.add_command(label="Colors", command=None)
    optionMenu.add_cascade(label="Set Theme", command=None)
    optionMenu.add_cascade(label="Toolbar", command=None)
    
    
    pass


def _createHelpMenu(menubar):
    helpMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help",menu=helpMenu)

    helpMenu.add_command(label="Contents",command=Action.showContents)
    helpMenu.add_command(label="How this works",command=Action.showGuide)
    helpMenu.add_command(label="Gameplay rules",command=Action.showRules)
    helpMenu.add_command(label="License",command=Action.showLicense)
    helpMenu.add_command(label="About",command=Action.showInfo)
