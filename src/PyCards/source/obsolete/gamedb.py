#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-
##---------------------------------------------------------------------------##
##
## Copyright (C) 1998-2003 Markus Franz Xaver Johannes Oberhumer
## Copyright (C) 2003 Mt. Hood Playing Card Co.
## Copyright (C) 2005-2009 Skomoroh
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##---------------------------------------------------------------------------##


# imports
import imp

from src.PyCards.source.obsolete import gametype
from src.PyCards.source.obsolete.gametype import *
from src.PyCards.source import settings


def _(msg):
    return msg


class GameInfoException(Exception):
    pass

class GameInfo:
    def __init__(self, ID, classname, name, game_type,
                 decks, redeals, skill=None,  # info={},
                 category=0, short_name=None, altnames=(),
                 suits=range(4), ranks=range(13), trumps=(),
                 numcards=None, rules_filename = None):

        self.ID = ID
        self.gameclass = classname
        self.rules_filename = rules_filename

        if category not in range(1, 9):
            self.category = _getCategory(category, game_type)
        else:
            self.category = category

        self.game_flags = game_type & ~1023
        self.game_type = game_type & 1023

        if not isinstance(altnames, tuple):
            altnames = (altnames,)

        self.en_name = name.encode('utf-8', 'ignore')

        if settings.TRANSLATE_GAME_NAMES:
            altnames = [_(n) for n in altnames]
            if not short_name:
                short_name = name
            name = _(name)
            short_name = _(short_name)

        altnames = [name.encode('utf-8', 'ignore') for name in altnames]
        self.altnames = tuple(altnames)

        self.decks = decks
        self.name = name.encode('utf-8', 'ignore')

        if not numcards:
            self.numcards = decks * len(suits) * len(ranks)

        self.ranks = tuple(ranks)
        self.suits = tuple(suits)
        self.redeals = redeals
        self.trumps = tuple(trumps)
        self.skill = skill
        self.short_name = short_name.encode('utf-8', 'ignore')

        if not (1 <= ID <= 999999):
            raise GameInfoException(name + ": invalID game ID " + str(ID))
        if category == CATEGORY.MAHJONGG:
            if decks % 4:
                raise GameInfoException(name + ": invalID number of decks " + str(ID))
        else:
            if not (1 <= decks <= 4):
                raise GameInfoException(name + ": invalID number of decks " + str(ID))
        if not name:
            raise GameInfoException(name + ": invalID game name")
        if gametype.PROTECTED_GAMES.get(ID):
            raise GameInfoException(name + ": protected game ID " + str(ID))

        for flag, game_set in ((STYLE.CHILDREN, gametype._CHILDREN_GAMES),
                     (STYLE.OPEN, gametype._OPEN_GAMES),
                     (STYLE.POPULAR, gametype._POPULAR_GAMES)):

            if (self.game_flags & flag) and (ID not in game_set):
                game_set.append(ID)
            elif not (self.game_flags & flag) and (ID in game_set):
                self.game_flags = self.game_flags | flag


def _getCategory(category, game_type):
    if game_type == STYLE.HANAFUDA:
        category = CATEGORY.HANAFUDA
    elif game_type == STYLE.TAROCK:
        category = CATEGORY.TAROCK
    elif game_type == STYLE.MAHJONGG:
        category = CATEGORY.MAHJONGG
    elif game_type == STYLE.HEXADECK:
        category = CATEGORY.HEXADECK
    elif game_type == STYLE.MUGHAL_GANJIFA:
        category = CATEGORY.MUGHAL_GANJIFA
    elif game_type == STYLE.NAVAGRAHA_GANJIFA:
        category = CATEGORY.NAVAGRAHA_GANJIFA
    elif game_type == STYLE.DASHAVATARA_GANJIFA:
        category = CATEGORY.DASHAVATARA_GANJIFA
    else:
        category = CATEGORY.FRENCH

    return category


class GameManager:

    def __init__(self):
        self.__selection = -1  # selected game
        self._num_games = 0

        self.__public_games = {}  # will be populated later
        self.__public_gamenames = {}

        # Allow for game betas, insider games, etc.
        self.__hidden_games = {}
        self.__hidden_gamenames = {}

        self.__games_by_altname = None
        self.__games_by_short_name = None

        self.__games_for_solver = []
        self.callback = None
        self.current_filename = None

    #for progress bar
    def setCallback(self, fcn):
        self.callback = fcn

    def getSelectedGame(self):
        return self.__selection

    def setSelected(self, gameID):
        assert gameID in self.__public_games
        self.__selected_key = gameID

    def get(self, key):
        return self.__public_games.get(key)

    def _check_game(self, gameinfo):

        # Check for duplicate game class (ID and name)
        for ID, game in self.__public_games.items():
            if gameinfo.gameclass is game.gameclass:  # note this eq does not include subclass
                raise GameInfoException(
                    "Duplicate game class, ID=%s, name=%s" %
                    (gameinfo.ID, str(game.gameclass)))

        # Check for duplicate game ID
        if gameinfo.ID in self.__public_games:
            raise GameInfoException(
                "Duplicate game IDS present%s: %s and %s" %
                (gameinfo.ID, str(gameinfo.gameclass),
                 str(self.__public_games[gameinfo.ID].gameclass)))

        # Check for duplicate game name
        if gameinfo.game in self.__public_gamenames:
            gameclass = self.__public_gamenames[gameinfo.name].gameclass
            raise GameInfoException(
                "duplicate game name %s: %s and %s" %
                (gameinfo.name, str(gameinfo.gameclass),
                 str(gameclass)))

    def register(self, gamedata):
        assert isinstance(gamedata, GameInfo)

        if settings.CHECK_GAMES:
            self._check_game(gamedata)

        if not (gamedata.game_flags & STYLE.HIDDEN):
            self.__public_games[gamedata.ID] = gamedata
            self.__public_gamenames[gamedata.name] = gamedata

            for othername in gamedata.altnames:
                self.__public_gamenames[othername] = gamedata
        else:
            self.__hidden_games[gamedata.ID] = gamedata
            self.__hidden_gamenames[gamedata.name] = gamedata

            for othername in gamedata.altnames:
                self.__hidden_gamenames[othername] = gamedata

        # Delete sorted game lists so they will be updated
        self.__games_by_ID = None
        self.__games_by_name = None

        # Solver, module name, callback
        if hasattr(gamedata.gameclass, 'Solver_Class') and \
                        gamedata.gameclass.Solver_Class is not None:
            self.__games_for_solver.append(gamedata.ID)
        if self.current_filename is not None:
            gamedata.gameclass.MODULE_FILENAME = self.current_filename

        if self.callback and self._num_games % 10 == 0:
            self.callback()
        self._num_games += 1

    #
    # Public accessors to games
    #

    def clear(self):
        self.__init__()

    def getAllGames(self):
        return self.__public_games.values()

    def gamesIdSorted(self):
        if self.__games_by_ID is not None:
            return self.__games_by_ID
        else:
            gameList = self.__public_games.keys()
            gameList.sort()
            self.__games_by_ID = tuple(gameList)
        return self.__games_by_ID


    def gamesNameSorted(self):
        if self.__games_by_name is not None:
            return self.__games_by_name
        else:
            gameList = sorted(self.__public_games.values(), key=lambda game: game.name)
            gameList = [gameinfo.ID for gameinfo in gameList]
            self.__games_by_name = tuple(gameList)
        return self.__games_by_name

    def gamesShortNameSorted(self):
        if self.__games_by_short_name is not None:
            return self.__games_by_short_name
        else:
            gameList = sorted(self.__public_games.values(),
                              key=lambda game: game.short_name if game.name != game.short_name else game.name)
            gameList = [gameinfo.ID for gameinfo in gameList]
            self.__games_by_short_name = tuple(gameList)
        return self.__games_by_short_name

    # elements are as (ID, altname)
    def gamesAltNameSorted(self):
        if self.__games_by_altname is not None:
            return self.__games_by_altname
        else:
            gameList = []
            for game in self.__public_games.values():
                for name in game.altnames:
                    gameList.append((game.ID, name))
            gameList = sorted(gameList, key=lambda info: info[1])
            self.__games_by_altname = tuple(gameList)
        return self.__games_by_altname

    # find game by name
    def getGame(self, name):
        game = self.__public_gamenames.get(name)
        if game is not None:
            return game #.ID
        return None

    def getGamesForSolver(self):
        return self.__games_for_solver


# ************************************************************************
# *
# ************************************************************************

#Module-level statements, methods
GAME_DB = GameManager()

def registerGame(gameinfo):
    GAME_DB.register(gameinfo)
    return gameinfo

#To be traced still
def loadGame(modname, filename, check_game=False):
    GAME_DB.check_game = check_game
    GAME_DB.current_filename = filename
    module = imp.load_source(modname, filename)
    GAME_DB.current_filename = None

