"""This module lets us create and use enumerated types in python

    State Variables: none

    Environment Variables: none

    Assumptions: none

"""

class Enum:
    """Implementation of an enumerated object type"""

    def __init__(self, name=None, value=None):
        """Initialize Enum object with starting attributes"""
        if name is not None:
            self.add(name, value)

    def add(self, name, value):
        """Adds attribute-value combinations to the object"""
        try:
            if not hasattr(name, '__iter__'):
                raise ValueError
            for key, val in name, value:
                setattr(self, key, val)
        except (TypeError,ValueError):
            if hasattr(name, '__iter__'):
                for key in name:
                    setattr(self, key, value)
            else:
                setattr(self, name, value)

    def addAll(self, fields):
        """Adds a sequence of attribute-value pairs to the object"""
        for i in range(0, len(fields), 2):
            setattr(self, fields[i], fields[i+1])
