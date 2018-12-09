#############
# Common Code
#############

#INPUT_FILE = "example.txt"
#INPUT_FILE = "example1.txt"
#INPUT_FILE = "example2.txt"
#INPUT_FILE = "example3.txt"
#INPUT_FILE = "example4.txt"
#INPUT_FILE = "example5.txt"
INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    num_p, _, _, _, _, _, last, *_ = f.readline().split(' ')
    num_p = int(num_p)
    last = int(last)

##########
# Part One
##########

game = [0]
players = [0] * num_p
pos = 0
for i in range(1, last + 1):
    if i % 23 == 0:
        pos = ((len(game) + pos) - 7) % len(game)
        extra = game.pop(pos + 1)
        players[(i % num_p) - 1] += i + extra
    else:
        pos = (pos + 2) % len(game)
        game.insert(pos + 1, i)

print("Part One:", max(players))

##########
# Part Two
##########

class node:
    def __init__(self):
        self.data = None
        self.nxt = None
        self.prv = None

class linked_list:
    def __init__(self):
        self.cur = None
        self.size = 0

    def add(self, data):
        if self.size == 0:
            n = node()
            n.nxt = n
            n.prv = n
            n.data = data
            self.cur = n
            self.size += 1
        elif self.size == 1:
            n = node()
            n.nxt = self.cur
            n.prv = self.cur
            n.data = data
            self.cur.nxt = n
            self.cur.prv = n
            self.cur = n
            self.size += 1
        else:
            n = node()
            n.nxt = self.cur.nxt.nxt
            n.prv = self.cur.nxt
            n.data = data
            self.cur.nxt.nxt.prv = n
            self.cur.nxt.nxt = n
            self.cur = n
            self.size += 1

    def pop(self):
        rm = self.cur.prv.prv.prv.prv.prv.prv.prv
        rm.nxt.prv = rm.prv
        rm.prv.nxt = rm.nxt
        self.cur = rm.nxt
        self.size -= 1
        return rm.data

game = linked_list()
game.add(0)
players = [0] * num_p
for i in range(1, (last * 100) + 1):
    if i % 23 == 0:
        players[(i % num_p) - 1] += i + game.pop()
    else:
        game.add(i)

print("Part Two", max(players))
