"""
    To find the shortest path to collect all the keys, we need to
    find the shortest path between keys. When we know all the paths
    we can solve the problem by summing over key combinations, which
    hopefully results in the shortest path.
"""

import sys
from collections import defaultdict
from itertools import permutations

def getMoveOpt(grid, pos, previous):

    opt = []
    p1 = (pos[0]+1, pos[1])
    if p1 in grid and not p1 in previous:
        opt.append(p1)
    p1 = (pos[0]-1, pos[1])
    if p1 in grid and not p1 in previous:
        opt.append(p1)

    p1 = (pos[0], pos[1]+1)
    if p1 in grid and not p1 in previous:
        opt.append(p1)

    p1 = (pos[0], pos[1]-1)
    if p1 in grid and not p1 in previous:
        opt.append(p1)


    return opt

def shortestPath(grid, start, end, steps, previous):

    if start == end:
        return steps

    previous[start] = 1
    options = getMoveOpt(grid, start, previous)
    t = 10**10
    for opt in options:
        t = min(t, shortestPath(grid, opt, end, steps+1, previous))
    return t

def findSmallestPath(node, paths, prev, steps):

    if len(paths) == len(prev):
        return steps

    path_list = list(paths[node].items())
    path_list.sort(key=lambda x:x[1])
    for k, s in path_list[:1]:

        if not k in prev:

            prv = prev.copy()
            prv.append(k)
            return findSmallestPath(k, paths, prv, steps+s)


with open(sys.argv[1], 'r') as f:

    grid = defaultdict(lambda:0)
    keys = defaultdict(lambda:0)
    x, y = 0, 0
    for line in f:
        # remove newline
        line = line[:-1]
        for item in line:
            if item == '.':
                grid[(x, y)] = 1
            elif item != '#':
                grid[(x, y)] = 2
                keys[item] = (x, y)
            x += 1

        x = 0
        y += 1

    start = keys['@']
    paths = defaultdict(lambda:0)

    # list of dicts with shortest paths between nodes
    for key1, item1 in keys.items():

        paths[key1] = defaultdict(lambda:0)
        for key2, item2 in keys.items():

            if key1 == key2:
                continue
            previous = defaultdict(lambda:0)
            paths[key1][key2] = shortestPath(grid,
                                             item1,
                                             item2,
                                             0,
                                             previous)

    # find a path with least amount of steps
    print(findSmallestPath('@', paths, ['@'], 0))
