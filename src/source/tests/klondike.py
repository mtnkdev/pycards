import unittest

from src.source.model.games import klondike


class KlondikeTest(unittest.TestCase):

    def setUp(self):
        self.game = klondike.Klondike()

    def test_create(self):

        # Precondition
        self.failUnlessEqual(len(self.game.stacks), 0)

        # Execute
        self.game.create()

        # Postcondition
        self.failUnlessEqual(len(self.game.stacks), 2 + self.game.foundations + self.game.numrows)

        for i in range(len(self.game.stacks)):
            stack = self.game.stacks[i]
            if i == 0:
                assert stack.isdeck and not stack.acceptCards and stack.offset == 0
            elif i == 1:
                assert not stack.isdeck and not stack.acceptCards and stack.offset == 0
            elif 2 <= i < self.game.foundations + 2:
                assert not stack.isdeck and stack.acceptCards and stack.offset == 0 and not stack.alternates and stack.sameSuit and stack.direction == 1
            else:
                assert not stack.isdeck and stack.acceptCards and stack.alternates \
                       and not stack.sameSuit and stack.direction == -1 and stack.offset == 15

    def tearDown(self):
        pass

