from intcode import *
import random
import sys
import copy


NORTH = 1
SOUTH = 2
WEST  = 3
EAST  = 4
PATH  = 1
END   = 2

if __name__ == '__main__':
    """
        tuple, (state, actions_left)
    """
    machine = IntCode(sys.argv[1])
    pos = (0, 0)
    end = (0, 0)
    actions = [(NORTH, (0, 1)), (SOUTH, (0,-1)), (EAST, (1, 0)), (WEST, (-1, 0))]

    grid = {}
    queue = [(pos, machine.getState(), [])]
    paths = []
    while len(queue) > 0:

        # try this state
        c_pos, c_machine_state, c_actions = queue[0]
        del queue[0]

        for ta, tv in actions:

            machine_state_copy  = copy.deepcopy(c_machine_state)
            actions_copy        = copy.deepcopy(c_actions)

            machine.setState(machine_state_copy)
            out = machine.run(ta)

            t_pos = (c_pos[0]+tv[0], c_pos[1]+tv[1])

            if out == 1 and not t_pos in grid:
                actions_copy.append(ta)
                queue.append((t_pos, machine.getState(), actions_copy))
                grid[t_pos] = out

            elif out == 2:
                actions_copy.append(ta)
                path = actions_copy
                end = t_pos

    print(len(path), end)
