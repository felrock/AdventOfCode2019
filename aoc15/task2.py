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

def changePosition(action, position):
    # update current position with a movement
    # chagnge if coord doesnt fix

    if action == NORTH:
        return (position[0], position[1]+1)
    elif action == SOUTH:
        return (position[0], position[1]-1)
    elif action == WEST:
        return (position[0]-1, position[1])
    else:
        return (position[0]+1, position[1])

def changePositionInv(action, position):
    # update current position with a movement
    # chagnge if coord doesnt fix

    # inverse

    if action == NORTH:
        return (position[0], position[1]-1)
    elif action == SOUTH:
        return (position[0], position[1]+1)
    elif action == WEST:
        return (position[0]+1, position[1])
    else:
        return (position[0]-1, position[1])


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

            # make copies
            machine_state_copy  = copy.deepcopy(c_machine_state)
            actions_copy        = copy.deepcopy(c_actions)

            # run with test configuration
            machine.setState(machine_state_copy)
            out = machine.run(ta)

            # update position vector
            t_pos = (c_pos[0]+tv[0], c_pos[1]+tv[1])

            if out == 1 and not t_pos in grid:

                # store actions to evalute step length in later stage
                actions_copy.append(ta)
                queue.append((t_pos, machine.getState(), actions_copy))
                grid[t_pos] = out

            elif out == 2:

                # best path was found, exit
                actions_copy.append(ta)
                path = actions_copy
                end = t_pos
                break
        if end != pos:
            break

    print('Task1 :',len(path), end)
    grid = {}
    queue = [(pos, machine.getState())]
    queue_next_spread = []
    min = 0
    # same principle for task2, but count after each spread iteration
    # all new qued actions will be added to a spread queue, when it is
    # copied to queue a minute is added

    while len(queue) > 0:

        # try this state
        c_pos, c_machine_state = queue[0]
        del queue[0]

        for ta, tv in actions:

            machine_state_copy  = copy.deepcopy(c_machine_state)

            machine.setState(machine_state_copy)
            out = machine.run(ta)

            t_pos = (c_pos[0]+tv[0], c_pos[1]+tv[1])

            if out == 1 and not t_pos in grid:
                queue_next_spread.append((t_pos, machine.getState()))
                grid[t_pos] = out

        if len(queue) == 0:
            queue = copy.deepcopy(queue_next_spread)
            queue_next_spread = []
            min += 1

    print('Task2', min-1)
