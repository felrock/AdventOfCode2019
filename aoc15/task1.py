from intcode import *
import random
import sys
import copy

grid = {}

n = 0
s = 1
w = 2
e = 3

def runSequence(machine, sequence):
    pos = (0, 0)
    for mv in sequence:

        if mv == n:
            pos = (pos[0], pos[1]+1)
        elif mv == s:
            pos = (pos[0], pos[1]-1)
        elif mv == w:
            pos = (pos[0]-1, pos[1])
        else:
            pos = (pos[0]+1, pos[1])

        out = machine.run(mv)

    return pos, out

if __name__ == '__main__':

    machine = IntCode(sys.argv[1])
    seq   = [[n], [s], [w], [e]]

    while len(seq) > 0:

        tsq = seq[0]
        del seq[0]

        n_tsq = copy.deepcopy(tsq)
        s_tsq = copy.deepcopy(tsq)
        w_tsq = copy.deepcopy(tsq)
        e_tsq = copy.deepcopy(tsq)

        n_tsq.append(n)
        s_tsq.append(s)
        w_tsq.append(w)
        e_tsq.append(e)

        n_pos, n_out = runSequence(copy.deepcopy(machine), n_tsq)
        s_pos, s_out = runSequence(copy.deepcopy(machine), s_tsq)
        w_pos, w_out = runSequence(copy.deepcopy(machine), w_tsq)
        e_pos, e_out = runSequence(copy.deepcopy(machine), e_tsq)

        if not n_pos in grid and n_out != 0:
            grid[n_pos] = n_out
            seq.append(n_tsq)

        if not s_pos in grid and s_out != 0:
            grid[s_pos] = s_out
            seq.append(s_tsq)

        if not w_pos in grid and w_out != 0:
            grid[w_pos] = w_out
            seq.append(w_tsq)

        if not e_pos in grid and e_out != 0:
            grid[e_pos] = e_out
            seq.append(e_tsq)
        print(len(seq))
        print(seq[0])

