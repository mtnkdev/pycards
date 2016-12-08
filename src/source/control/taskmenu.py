"""This module contains the implementation of widgets that
the user interacts with to trigger events

    State variables:
    root: the main application window

    Environment variables: None

    Assumptions: None

    **Semantics**

    :func:`create_menu`:

    * transition: creates the menubar for the application


    **Exported Access Programs**

    ==================   ============   ============
    Routine                  In             Out
    ==================   ============   ============
    create_menu             root
    ==================   ============   ============

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
    _create_selectmenu(menubar)
    _create_assistmenu(menubar)
    _create_optionmenu(menubar)
    _create_helpmenu(menubar)


def _add_games(menu, games, command=None):
    """Add games by type to the cascading game type menu"""
    for game in sorted(games, key=lambda game : game.name):
        cmd = lambda args=game: action.start_game(args)
        menu.add_command(label=game.name, command=cmd)


def _add_game_type(menu, label, gameSet=None):
    """Add game types to the Menu"""
    if (gameSet is None) or (gameSet is not None and len(gameSet) > 0):
        submenu = Menu(menu, tearoff=0)
        menu.add_cascade(label=label, menu=submenu)

        if gameSet is None:
            return submenu      # Child is another cascading menu
        elif len(gameSet) > 0:
            _add_games(submenu, gameSet) # Adds games belonging to type


def _create_filemenu(menubar):
    """Create the cascading File menu"""
    fileMenu = Menu(menubar, tearoff=0)

    # Adds dropdown menu
    menubar.add_cascade(label="File", menu=fileMenu)

    # Adds selectable dropdown items
    # command is a pointer to function
    fileMenu.add_command(label="New", command=action.restart)
    fileMenu.add_command(label="Load...", command=action.loadGame)
    fileMenu.add_command(label="Save...", command=action.saveGame)
    fileMenu.add_command(label="Exit", command=action.quitGame)


def _create_selectmenu(menubar):
    """Create the cascading Select menu"""
    selectMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Select", menu=selectMenu)

    #selectMenu.add_command(label="All Games...", command=action.showGames)

    _add_game_type(selectMenu, "FreeCell", get_games("FreeCell"))
    _add_game_type(selectMenu, "Hanoi", get_games("Hanoi"))
    _add_game_type(selectMenu, "Klondike", get_games("Klondike"))
    _add_game_type(selectMenu, "Memory", get_games("Memory"))
    _add_game_type(selectMenu, "Spider", get_games("Spider"))


def get_games(gametype):
    """Retrieve games belonging to the specified type"""
    return [game for game in DB.get_games() if game.name.count(gametype) > 0]


def _create_assistmenu(menubar):
    """Create the cascading Assist menu"""
    assistMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Assist", menu=assistMenu)
    assistMenu.add_command(label="Solve", command=action.solve_game)


def _create_optionmenu(menubar):
    """Create the cascading Option menu"""
    optionMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Cardset", command=action.select_cardset)
    optionMenu.add_command(label="Background", command=lambda args=menubar.master: action.select_tile(args))



def _create_helpmenu(menubar):
    """Create the cascading Help menu"""
    helpMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help",menu=helpMenu)
    helpMenu.add_command(label="License", command=action.showLicense)
