"""This module is responsible for storing the set of registered games

    State Variables:
    DB: collection of games

    Environment Variables: none

    Assumptions:
    The Zen of Python: 'Flat is better than nested',
    hence database.DB is preferred to database.Database.DB
"""


class Database:
    """Storage for all the game types and associated game

    Database be used as singleton through public instance DB
    Games are added using unique names or identifiers
    """
    
    def __init__(self):
        """Initialize Database with no games to start"""
        self.games = {}

    def add_game(self, name, game_class):
        """Add games to the database

        :param name: name and unique identifier of the game
        :param game_class: the class that defines the game
        """
        self.games[name] = game_class

    def get_games(self):
        """Return a sequence of game classes

        :rtype collection of games
        """
        return self.games.values()

# System-wide game database
DB = Database()
