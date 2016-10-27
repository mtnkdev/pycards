
# class Enum:
#     def __init__(self):
#         pass
#
#     def add(self, name, value):
#         if type(name) == tuple:
#             if type(value) == tuple:
#                 for key, val in name, value:
#                     setattr(self, key, val)
#             else:
#                 for key in name:
#                     setattr(self, key, value)
#         else:
#             setattr(self, name, value)
#
#     def addAll(self, fields):
#         for i in range(0, len(fields), 2):
#             setattr(self, fields[i], fields[i+1])


class Pile():

    def __init__(self, pos, base, alternate, direction, size):
        self.x, self.y = pos
        self.base = base
        self.direction = direction
        self.alternate = alternate
        self.size = size


# p1 = Pile((50,50),13,True,-1,1)
# p2 = Pile((60,50),13,True,-1,2)
# p3 = Pile((70,50),13,True,-1,3)
# p4 = Pile((80,50),13,True,-1,4)
# p5 = Pile((90,50),13,True,-1,5)
# p6 = Pile((100,50),13,True,-1,6)
# p7 = Pile((110,50),13,True,-1,7)
