"""
        The simpler solution, treat all as a BFS problem, the solution
        with smallest amount of steps output.

"""
import sys
from collections import defaultdict

def move(pos):
    """
        return possble moves from position pos.
    """

    return [(pos[0]+1, pos[1]),
            (pos[0]-1, pos[1]),
            (pos[0], pos[1]+1),
            (pos[0], pos[1]-1)]

def run():

    with open(sys.argv[1], 'r') as f:

        grid  = defaultdict(lambda:0)
        x, y  = (0, 0)
        start = (0, 0)
        key_len = 0
        # read the grid

        for line in f:
            # remove newline
            line = line[:-1]
            for item in line:
                if item == '@':
                    start = (x, y)
                if item.islower():
                    key_len += 1
                grid[(x, y)] = item
                x += 1
            x = 0
            y += 1

        # walk the grid
        states = [(start, frozenset(), 0)]
        seen = {}
        depth = 0

        while True:

            new_states = []
            # pop into current state
            for cur_pos, cur_keys, cur_steps in states:

                for next_pos in move(cur_pos):

                    c = grid[next_pos]
                    if not c:
                        continue
                    elif c == '#':
                        continue
                    elif (next_pos, cur_keys) in seen:
                        continue
                    elif c.isupper() and not c.lower() in cur_keys:
                        continue

                    if c.islower() and not c in cur_keys:
                        new_keys = cur_keys | {c}
                        new_states.append((next_pos, new_keys, cur_steps+1))

                    else:
                        new_states.append((next_pos, cur_keys, cur_steps+1))

                    seen[(next_pos, cur_keys)] = 1
                    if len(cur_keys) == key_len:
                        return cur_steps

            # new states
            states = new_states

# task1
print(run())
