import random
from ..model.card import StandardCard


class Dealer:

    def __init__(self, game, cardset):
        self.deck = []
        self.cardset = cardset
        self.game = game

    def cardgen(self):
        assert self.game.type == self.cardset.ctype
        assert self.game.numcards % len(self.cardset.cards) == 0

        for i in range(self.game.numcards / len(self.cardset.cards)):
            for rank in self.cardset.ranks:
                for suit in self.cardset.suits:
                    self.deck.append(StandardCard(self.cardset, rank, suit))
        assert len(self.deck) == self.game.numcards
        shuffle(self.deck)

    def dealCards(self):
        stacks = self.game.stacks

        index = 0
        for i in range(len(stacks)):
            pos = stacks[i].positions
            # print len(pos)
            # print len(stacks[i].cards)
            for c in range(len(pos)):
                stacks[i].cards[c] = self.deck[index % len(self.cardset.cards)]
                index += 1
                if pos[c] == 1:
                    stacks[i].cards[c].show()


def shuffle(cards):
    random.shuffle(cards)