

class Enum:
    """Docstring"""

    def __init__(self, name=None, value=None):
        if name is not None:
            self.add(name, value)

    def add(self, name, value):
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
        for i in range(0, len(fields), 2):
            setattr(self, fields[i], fields[i+1])