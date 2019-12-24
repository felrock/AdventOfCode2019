import sys
from intcode import *
from collections import defaultdict

grid = defaultdict(lambda:0)
cleaned = {}
right = (1, 0)
left = (-1, 0)
up = (0, -1)
down = (0, 1)

"""
    The initial idea is that in-order clean efficienly, it is costly to turn,
    so at each intersection turning should only be considered if it is a must.
"""

def startDir(start):

    if grid[(start[0]+1, start[1])] == 1:
        return right, 'R'

    if grid[(start[0]-1, start[1])] == 1:
        return left, 'L'

def changeDir(pos, vec):

    if vec == left:

        if grid[(pos[0]+up[0], pos[1]+up[1])] == 1:
            return up, 'R'
        else:
            return down, 'L'

    elif vec == right:

        if grid[(pos[0]+down[0], pos[1]+down[1])] == 1:
            return down, 'R'
        else:
            return up, 'L'

    elif vec == up:

        if grid[(pos[0]+right[0], pos[1]+right[1])] == 1:
            return right, 'R'
        else:
            return left, 'L'

    elif vec == down:

        if grid[(pos[0]+left[0], pos[1]+left[1])] == 1:
            return left, 'R'
        else:
            return right, 'L'


if __name__ == '__main__':

    machine = IntCode(sys.argv[1])
    x, y = 0, 0
    start = (0, 0)
    while not machine.halt:

        out = machine.run()
        if out == 35:
            grid[(x, y)] = 1
            x += 1
        elif out == 46:
            x += 1
        elif out == 10:
            y += 1
            x = 0
        elif out == 94:
            start = (x, y)
            x += 1

    # this only should only be one way to start.
    vec, dir = startDir(start)
    pos = start
    path = []
    steps = 0
    cleaned[start] = 1
    it = 0
    length = len(grid.keys())
    while len(cleaned.keys()) != length:
        # walk one direction as long as possible, turn, repeat

        # test walk
        t_pos = (pos[0]+vec[0], pos[1]+vec[1])
        while grid[t_pos] == 1:
            pos = t_pos
            cleaned[pos] = 1
            steps += 1
            t_pos = (t_pos[0]+vec[0], t_pos[1]+vec[1])

        # new direction needed
        path.append((dir, steps))
        steps = 0
        vec, dir = changeDir(pos, vec)

    # here we have a non-optimized path
    print(path)

    uncompressed = []
    for p in path:
        uncompressed.append(p[0] + str(p[1]))
    # LZW encoding
    print(uncompressed)
