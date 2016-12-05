import unittest

from src.model.games import spider


class SpiderTest(unittest.TestCase):

    def setUp(self):
        self.game = spider.Spider()

    def test_create(self):

        # Precondition
        self.failUnlessEqual(len(self.game.stacks), 0)

        # Execute
        self.game.create()

        # Postcondition
        self.failUnlessEqual(len(self.game.stacks), 1 + self.game.foundations + self.game.numrows)

        for i in range(len(self.game.stacks)):
            stack = self.game.stacks[i]
            if i == 0:
                assert stack.isdeck and not stack.acceptCards and stack.offset == 0
            elif 1 <= i <= self.game.foundations:
                assert not stack.isdeck and not stack.acceptCards and stack.offset == 0
            else:
                assert not stack.isdeck and stack.acceptCards and stack.direction == -1 and stack.offset == 15

    def tearDown(self):
        pass

