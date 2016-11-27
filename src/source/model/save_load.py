_data = ""


def _write(*args):
    global _data
    if args is not None:
        _data += ''.join(args)


def _flush():
    global _data
    print _data


"""To represent and recreate the top level of a game I need:
* name
* stacks

To represent and recreate the state of a game I need:
from stacks:
* card.cardset
* cards
 * card.rank
 * card.suit
 * card.visible
"""


def save_game(self):
    print self
    _write(self.name, '_', str(len(self.stacks)), '_', self.cardset)
    for i in range(len(self.stacks)):
        _write("{:02x}".format(len(self.stacks[i].cards)))

    for i in range(len(self.stacks)):
        stack = self.stacks[i]
        for j in range(len(stack.cards)):        
            card = stack.cards[j]
            _write("{:02}".format(card.rank), card.suit, str(int(card.visible)))


def _read(data=_data):
    import re
    data = data.split("_")
    game_name = data[0]
    numrows = int(data[1])
    cardset = re.split("\d+", data[2])[0]
    offset = len(cardset)
    stack_data = data[2][offset:]
    print game_name
    print numrows
    print cardset

    size = []
    for i in range(numrows):
        size.append(int("0x" + stack_data[2*i:2*i+2], 16))
    print size
    offset += 2*numrows
    print data[2][offset:]

    stacks = []
    for i in range(numrows):
        stacks.append([])
        for j in range(size[i]):
            rank = int("0x" + data[2][offset:offset+2], 16)
            suit = data[2][offset+2]
            visible = data[2][offset+3]
            stacks[i].append([rank, suit, visible])
            offset += 4
            print "rank: ", rank, "  suit: ", suit, "  visible: ", visible
        
# _read()
    
def load_game(game_name, cardset, stacks):
    destroy()
    game = DB.get_game(game_name)
    _game = game()
    _game.cardset = Cardset.cardsets[cardset]
    _game.stacks = []
    
    for i in range(len(stacks)):
        _game.stacks.append([])
        for j in range(len(stacks[i])):
            _game.stacks[i].append(StandardCard(_game.cardset, stacks[i][j][0], stacks[i][j][1]))
            _game.stacks[i][j].visible = stacks[i][j][2]
    draw_game()
