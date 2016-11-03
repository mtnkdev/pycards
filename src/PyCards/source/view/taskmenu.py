from Tkinter import Menu

import menuactions as Action
from src.PyCards.source.obsolete import gamedb
from src.PyCards.source.obsolete.gametype import FILTER, STYLE


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
        menu.add_command(label=game.name, command=command)

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
    fileMenu.add_command(label="New", command=Action.startNew)
    fileMenu.add_command(label="Recents", command=Action.listRecent)
    fileMenu.add_command(label="Load...", command=Action.loadGame)
    fileMenu.add_command(label="Save...", command=Action.saveGame)
    fileMenu.add_command(label="Exit", command=Action.quitGame)


def _createSelectMenu(menubar):
    # Creates a submenu (another Menu instance)
    # tearoff stops menu floating
    selectMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Select", menu=selectMenu)

    selectMenu.add_command(label="All Games...", command=Action.showGames)

    def addPopular(parent):
        popStyle = Menu(parent, tearoff=0)
        selectMenu.add_cascade(label="Popular games", menu=popStyle)
        select_func = lambda gi: gi.game_flags & STYLE.POPULAR
        popularGames = filter(select_func, gamedb.GAME_DB.getAllGames())
        _addMenuGames(popStyle, popularGames)

    def addFrenchGames(parent):
        frenchStyle = _addMenuGameType(parent, "French games")
        for name, gameT in FILTER.FRENCH:
            gameList = []
            for game in gamedb.GAME_DB.getAllGames():
                if gameT(game):
                    gameList.append(game)
            _addMenuGameType(frenchStyle, name, gameList)

    def addOrientalGames(parent):
        orientalStyle = _addMenuGameType(parent, "Oriental games")
        for name, gameT in FILTER.ORIENTAL:
            gameList = []
            for game in gamedb.GAME_DB.getAllGames():
                if gameT(game):
                    gameList.append(game)
            _addMenuGameType(orientalStyle, name, gameList)

    def addSpecialGames(parent):
        specialStyle = _addMenuGameType(parent, "Special games")
        for name, gameT in FILTER.SPECIAL:
            gameList = []
            for game in gamedb.GAME_DB.getAllGames():
                if gameT(game):
                    gameList.append(game)
            _addMenuGameType(specialStyle, name, gameList)


    addPopular(selectMenu)
    addFrenchGames(selectMenu)
    addOrientalGames(selectMenu)
    addSpecialGames(selectMenu)

    # for name, gameSelector in gamedb.GI.SELECT_GAME_BY_TYPE:
    #     subMenu = Menu(gameStyle, tearoff=0)
    #     gameStyle.add_cascade(label=name,menu=subMenu)



    #for name in os.listdir(path):
    #    if name.endswith(".py") and not name.startswith("_"):
    #        gameStyle.add_command(label=name[:-3], command=None)

    # gameType = []
    # gameType.append(Menu(Menu, tearoff=0))
    # for gtype in gameType:
    #     ##gameStyle.add_cascade(gtype) fix type error
    #     for game in getGames(gtype):
    #         ##gtype.add(label="game.name", command=startGame(game.name)


def _createEditMenu(menubar):
    editMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=editMenu)
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
    gameMenu.add_command(label="Comments", command=None)
    gameMenu.add_command(label="Statistics", command=None)
    gameMenu.add_command(label="Log", command=None)
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
    optionMenu.add_command(label="Cardset", command=None)
    optionMenu.add_command(label="Table Tile", command=None)
    optionMenu.add_cascade(label="Card Background", command=None)
    optionMenu.add_cascade(label="Card View", command=None)
    optionMenu.add_cascade(label="Animations", command=None)
    optionMenu.add_cascade(label="Mouse", command=None)
    optionMenu.add_command(label="Fonts", command=None)
    optionMenu.add_command(label="Colors", command=None)
    optionMenu.add_cascade(label="Set Theme", command=None)
    optionMenu.add_cascade(label="Toolbar", command=None)
    optionMenu.add_cascade(label="Save Game Geometry", command=None)
    
    
    pass


def _createHelpMenu(menubar):
    helpMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help",menu=helpMenu)

    helpMenu.add_command(label="Contents",command=Action.showContents)
    helpMenu.add_command(label="How this works",command=Action.showGuide)
    helpMenu.add_command(label="Gameplay rules",command=Action.showRules)
    helpMenu.add_command(label="License",command=Action.showLicense)
    helpMenu.add_command(label="About",command=Action.showInfo)
