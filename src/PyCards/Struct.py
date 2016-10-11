# ************************************************************************
# *
# ************************************************************************

class Struct:
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __str__(self):
        return str(self.__dict__)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError(key)
        self.__dict__[key] = value

    def addattr(self, **kw):
        for key in kw.keys():
            if hasattr(self, key):
                raise AttributeError(key)
        self.__dict__.update(kw)

    def update(self, dict):
        for key in dict.keys():
            if key not in self.__dict__:
                raise AttributeError(key)
        self.__dict__.update(dict)

    def clear(self):
        for key in self.__dict__.keys():
            if isinstance(key, list):
                self.__dict__[key] = []
            elif isinstance(key, tuple):
                self.__dict__[key] = ()
            elif isinstance(key, dict):
                self.__dict__[key] = {}
            else:
                self.__dict__[key] = None

    def copy(self):
        c = self.__class__()
        c.__dict__.update(self.__dict__)
        return c

