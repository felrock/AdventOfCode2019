from intcode import *
import random
import sys

grid = {}

if __name__ == '__main__':

    machine = IntCode(sys.argv[1])
    start = (0, 0)
    queue = [(start, machine.getState())]

    while len(queue) > 0:

        pos, state = queue.pop()
        machine.setState(state)
        north = machine.run(1)
        n_state = machine.getState()
        n_pos = (pos[0], pos[1]+1)

        machine.setState(state)
        south = machine.run(2)
        s_state = machine.getState()
        s_pos = (pos[0], pos[1]-1)

        machine.setState(state)
        west  = machine.run(3)
        w_state = machine.getState()
        w_pos = (pos[0]-1, pos[1])

        machine.setState(state)
        east  = machine.run(4)
        e_state = machine.getState()
        e_pos = (pos[0]+1, pos[1])

        machine.setState(state)
        print('poses', n_pos, s_pos, w_pos, e_pos)
        print('outs', north, south, west, east)

        if not n_pos in grid and north != 0:
            print(n_pos, 'n added')
            grid[n_pos] = north
            machine.run(1)
            queue.append((n_pos, n_state))

        if not s_pos in grid and south != 0:
            print(s_pos, 's added')
            grid[s_pos] = south
            machine.run(2)
            queue.append((s_pos, s_state))

        if not w_pos in grid and west != 0:
            print(w_pos, 'w added')
            grid[w_pos] = west
            machine.run(3)
            queue.append((w_pos, w_state))

        if not e_pos in grid and east != 0:
            print(e_pos, 'e added')

            grid[e_pos] = east
            machine.run(4)
            queue.append((e_pos, e_state))

        print(len(queue))
        x = input()
