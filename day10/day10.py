import re

#INPUT_FILE="example.txt"
INPUT_FILE="input.txt"

pos = []
vel = []
with open(INPUT_FILE) as f:
    for line in f:
        p, v = re.findall("<[\d\s-]\d*,\s[\d\s-]\d*>", line)
        x, y = list(map(int, p.strip('<>').split(', ')))
        vx, vy = list(map(int, v.strip('<>').split(', ')))
        pos.append((x, y))
        vel.append((vx, vy))

# get the bounds of the grid that should be printed
def bounds(pos):
    xmax = max(pos)[0] + 1
    xmin = min(pos)[0]
    ymax = max(pos, key=lambda x: x[1])[1] + 1
    ymin = min(pos, key=lambda x: x[1])[1]
    return xmax, xmin, ymax, ymin

# print the grid with the points marked as '#'
def print_grid(pos):
    xmax, xmin, ymax, ymin = bounds(pos)
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            if (x, y) in pos:
                print('#', end='')
            else:
                print('.', end='')
        print()

# update pos array with velocity of points
def update_pos(pos, vel):
    for i in range(len(pos)):
        pos[i] = (pos[i][0] + vel[i][0], pos[i][1] + vel[i][1])

# keep track of time spent for part Two
time = 0

# get fast at the time when points are close to each other
xmax, xmin, *_ = bounds(pos)
while (xmax - xmin) > 100:
    update_pos(pos, vel)
    time += 1
    xmax, xmin, *_ = bounds(pos)

# main loop, press enter to advance of 1 second
print_grid(pos)
print("Time:", time, "seconds")
while(not input()):
    update_pos(pos, vel)
    time += 1
    print_grid(pos)
    print("Time:", time, "seconds")
