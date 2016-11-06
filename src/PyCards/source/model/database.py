class Database:
    """Storage for all the game types. To be used as singleton with
    global instance DB"""
    
    def __init__(self):
        """Initialize Database with no games"""
        self.games = {}

    def add_game(self, name, game_class):
        """Add games to the database"""
        self.games[name] = game_class

    def get_games(self):
        """Return a sequence of game classes"""
        return self.games.values()

# System-wide game database
DB = Database()
