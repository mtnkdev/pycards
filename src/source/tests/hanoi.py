import unittest

from src.source.model.games import hanoi


class HanoiTest(unittest.TestCase):

    def setUp(self):
        self.game = hanoi.Hanoi()

    def test_create(self):
        # Precondition
        self.failUnlessEqual(len(self.game.stacks), 0)
        
        # Execute
        self.game.create()

        # Postcondition
        self.failUnlessEqual(len(self.game.stacks),3)

        for i in range(len(self.game.stacks)):
            stack = self.game.stacks[i]
            assert not stack.isdeck and stack.acceptCards and stack.offset == 15 and stack.direction == -1
        

    def tearDown(self):
        pass

