from abc import ABCMeta, abstractmethod


class CardGame():
    """Abstract base class to be used as specification for all games"""
    __metaclass__ =  ABCMeta

    @classmethod
    def __subclasshook__(cls, subclass):
        pass

    @abstractmethod
    def create(self):
        """
        Define the initial layout of the game including
        the number and positioning of cards

        Also place restriction on the allowed actions based
        on the rules of the game
        """

    @abstractmethod
    def deal(self):
        """
        If in-game dealing is allowed this performs
        a single deal action
        """