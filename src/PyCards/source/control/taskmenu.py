"""This module contains the implementation of widgets that
the user interacts with to trigger events

    State variables:
    root: the main application window

    Environment variables: None

    Assumptions: None

    **Exported Access Programs**

    ==================   ============   ============
    Routine                  In             Out
    ==================   ============   ============
    create_menu             root
    ==================   ============   ============

    **Semantics**

    create_menu(root) :
    * transition: creates the menubar for the application
"""

from Tkinter import Menu

import menuactions as action
from ..model.database import DB


def create_menu(root):
    """Create the application's menubar widget"""
    menubar = Menu(root)

    # Add menubar to root window
    root.config(menu=menubar)

    _create_filemenu(menubar)
    _create_selectmenu(menubar)  ##Look at _addSelectGameMenu in menubar.py
    _create_editmenu(menubar)
    _create_gamemenu(menubar)
    _create_assistmenu(menubar)
    _create_optionmenu(menubar)
    _create_helpmenu(menubar)


def _add_games(menu, games, command=None):
    """Add games by type to the cascading game type menu"""
    for game in sorted(games, key=lambda game : game.name):
        cmd = lambda args=game: action.start_game(game)
        menu.add_command(label=game.name, command=cmd)


def _add_game_type(menu, label, gameSet=None):
    """Add game types to the Menu"""
    if (gameSet == None) or (gameSet != None and len(gameSet) > 0):
        submenu = Menu(menu, tearoff=0)
        menu.add_cascade(label=label, menu=submenu)

        if gameSet == None:
            return submenu      # Child is another cascading menu
        elif len(gameSet) > 0:
            _add_games(submenu, gameSet) # Adds games belonging to type


def _create_filemenu(menubar):
    """Create the cascading File menu"""
    fileMenu = Menu(menubar, tearoff=0)

    # Adds dropdown menu
    menubar.add_cascade(label="File", menu=fileMenu)

    # Adds selectable dropdown items
    # @command is a pointer to function
    fileMenu.add_command(label="New", command=action.restart)
    fileMenu.add_command(label="Load...", command=lambda args=game: action.loadGame(args))
    fileMenu.add_command(label="Save...", command= lambda args=game: action.saveGame(args))
    fileMenu.add_command(label="Exit", command=action.quitGame)


def _create_selectmenu(menubar):
    """Create the cascading Select menu"""
    selectMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Select", menu=selectMenu)

    selectMenu.add_command(label="All Games...", command=action.showGames)

    _add_game_type(selectMenu, "FreeCell", get_games("FreeCell"))
    _add_game_type(selectMenu, "Hanoi", get_games("Hanoi"))
    _add_game_type(selectMenu, "Klondike", get_games("Klondike"))
    _add_game_type(selectMenu, "Memory", get_games("Memory"))
    _add_game_type(selectMenu, "Spider", get_games("Spider"))


def get_games(gametype):
    """Retrieve games belonging to the specified type"""
    return [game for game in DB.get_games() if game.name.count(gametype) > 0]


def _create_editmenu(menubar):
    """Create the cascading Edit menu"""
    editMenu = Menu(menubar, tearoff=0)
    editMenu.add_command(label="Undo", command=None)
    editMenu.add_command(label="Redo", command=None)
    editMenu.add_command(label="Redo All", command=None)
    editMenu.add_command(label="Restart", command=None)


def _create_gamemenu(menubar):
    """Create the cascading Game menu"""
    gameMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Game", menu=gameMenu)
    gameMenu.add_command(label="Deal Cards", command=None)
    gameMenu.add_command(label="Auto Drop", command=None)
    gameMenu.add_command(label="Pause", command=None)
    gameMenu.add_command(label="Status", command=None)
    gameMenu.add_command(label="Statistics", command=None)


def _create_assistmenu(menubar):
    """Create the cascading Assist menu"""
    assistMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Assist", menu=assistMenu)
    assistMenu.add_command(label="Hint", command=None)
    assistMenu.add_command(label="Highlight piles", command=None)
    assistMenu.add_command(label="Find Card", command=None)


def _create_optionmenu(menubar):
    """Create the cascading Option menu"""
    optionMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Sound", command=None)
    optionMenu.add_command(label="Cardset", command=action.select_cardset)
    optionMenu.add_command(label="Background", command=lambda args=menubar.master: action.select_tile(args))
    optionMenu.add_cascade(label="Card Background", command=None)
    optionMenu.add_cascade(label="Animations", command=None)
    optionMenu.add_cascade(label="Mouse", command=None)
    optionMenu.add_command(label="Fonts", command=None)
    optionMenu.add_command(label="Colors", command=None)
    optionMenu.add_cascade(label="Set Theme", command=None)
    optionMenu.add_cascade(label="Toolbar", command=None)


def _create_helpmenu(menubar):
    """Create the cascading Help menu"""
    helpMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help",menu=helpMenu)

    helpMenu.add_command(label="Contents", command=action.showContents)
    helpMenu.add_command(label="How this works", command=action.showGuide)
    helpMenu.add_command(label="Gameplay rules", command=action.showRules)
    helpMenu.add_command(label="License", command=action.showLicense)
    helpMenu.add_command(label="About", command=action.showInfo)
