import unittest

from source import init
init.init()

from source.gamedb import GAME_DB
from tests import gameStub

class TestGameDb(unittest.TestCase):

    @staticmethod
    def isIDSorted():
        prev = -1
        for ID in GAME_DB.gamesIdSorted():
            if ID <= prev:
                print ID, prev
            assert ID > prev
            prev = ID

    @staticmethod
    def isNameSorted():
        prev = ""
        for ID in GAME_DB.gamesNameSorted():
            name = GAME_DB.get(ID).name
            if name <= prev:
                print name, prev
            assert name > prev
            prev = name

    def test_registerAll(self):
        assert len(GAME_DB.getAllGames()) == 0
        gameStub.registerAll()
        assert len(GAME_DB.getAllGames()) > 0
        TestGameDb.isIDSorted()
        TestGameDb.isNameSorted()

    def test_staggeredRegister(self):
        GAME_DB.clear()
        assert len(GAME_DB.getAllGames()) == 0
        gameStub.registerPegged()
        assert len(GAME_DB.getAllGames()) > 0
        TestGameDb.isIDSorted()
        TestGameDb.isNameSorted()
        gameStub.registerMatrix()
        assert len(GAME_DB.getAllGames()) > 0
        TestGameDb.isIDSorted()
        TestGameDb.isNameSorted()


    def test_registerInvalids(self):
        pass

    def tearDown(self):
        pass
