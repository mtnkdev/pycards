"""This module is responsible for the logic related to dealing cards

    State Variables: None

    Environment Variables: None

    Assumptions: None

"""

import random
from ..model.card import StandardCard


class Dealer:
    """Controller for the dealing and automatic movement of cards

    State Variables: 
    deck: a sequence of cards
    cardset: images for the cards
    game: the application state - game in progress

    Assumptions: 
    A game is in progress and a valid cardset is defined

    **Semantics**

    :func:`cardgen`:

    * transition:

     * creates and instantiates the cards in the game
     * adds the sequence of the cards to the game deck


    :func:`dealCards`:

    * transition:

     * distributes the cards to the game stacks

    **Exported Access Programs**

    ==================   ============   ============
    Routine                  In             Out
    ==================   ============   ============
    cardgen()
    dealCards()
    ==================   ============   ============


"""

    def __init__(self, game, cardset):
        self.deck = []
        self.cardset = cardset
        self.game = game

    def cardgen(self):
        """Generate the cards for the current game

        Based upon the suit, type, and number of cards generate
        all the cards necessary for the current game and add them
        to the stack identified as the deck for the game
        """
        assert self.game.type == self.cardset.ctype
        assert self.game.numcards % len(self.cardset.cards) == 0

        for i in range(self.game.numcards / len(self.cardset.cards)):
            for rank in self.cardset.ranks:
                for suit in self.cardset.suits:
                    self.deck.append(StandardCard(self.cardset, rank, suit))
        assert len(self.deck) == self.game.numcards
        _shuffle(self.deck)

    def dealCards(self):
        """Distribute the cards to the stacks as defined by the game logic

        Assign cards from self.deck to the respective stack in self.game.stacks
        """
        stacks = self.game.stacks

        index = 0
        for i in range(len(stacks)):
            pos = stacks[i].positions
            for c in range(len(pos)):
                stacks[i].cards[c] = self.deck[index]
                index += 1
                if pos[c] == 1:
                    stacks[i].cards[c].show()


def _shuffle(cards):
    random.shuffle(cards)
