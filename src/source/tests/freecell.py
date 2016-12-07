import unittest

from src.source.model.games import freecell


class FreeCellTest(unittest.TestCase):

    def setUp(self):
        self.game = freecell.FreeCell()

    def test_create(self):
        # Precondition
        self.failUnlessEqual(len(self.game.stacks), 0)
        
        # Execute
        self.game.create()
        
        # Postcondition
        self.failUnlessEqual(len(self.game.stacks), self.game.foundations + self.game.numrows + self.game.cells)
        
        for i in range(len(self.game.stacks)):
            stack = self.game.stacks[i]
            if i < self.game.cells:
                assert stack.capacity == 1 and not stack.isdeck and stack.acceptCards
            elif self.game.cells <= i < self.game.foundations + self.game.cells:
                assert not stack.isdeck and stack.acceptCards and stack.offset == 0 and not stack.alternates and stack.sameSuit and stack.direction == 1
            else:
                assert not stack.isdeck and stack.acceptCards and stack.alternates \
                    and not stack.sameSuit and stack.direction == -1 and stack.offset == 15



    def tearDown(self):
        pass

