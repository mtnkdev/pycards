class database:

    def __init__(self):
        self.games = {}

    def add_game(self, name, game_class):
        self.games[name] = game_class

    def get_games(self):
        return self.games.keys()

##a = database()
##a.add_game("fish", "go")
##a.add_game("water", "down")
##print a.get_games()
##print type(a.get_games())
##print __name__
