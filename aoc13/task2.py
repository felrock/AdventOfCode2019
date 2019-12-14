from intcode import *
import sys
import os
import time

def makeNewGrid(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def printGrid(grid):
    for col in grid:
        for row in col:
            print(row, end='')
        print()


if __name__ == '__main__':

    # constants
    machine = IntCode(sys.argv[1])
    tiles = [' ', '#', '0', 'p', 'x' ]
    noop = 0
    move_left = -1
    move_right= 1
    width = 37
    height= 20

    # game state
    count = 0
    user_action = noop
    score = 0
    grid = makeNewGrid(width, height)
    pos = (0, 0)
    ball = (0, 0)

    while True:

        if count == width*height:
            # write to terminal window
            printGrid(grid)
            os.system('clear')

            # simple agent, follow ball
            if ball[0] > pos[0]:
                user_action = move_right
            elif ball[0] < pos[0]:
                user_action = move_left
            else:
                user_action = noop

        else:
            # draw the entire game before trying to
            # control the agent or print to terminal
            count += 1

        # get machine outputs
        from_left = machine.run(user_action)
        from_top = machine.run(user_action)
        type = machine.run(user_action)

        # machine is done running
        if machine.halt:
            break

        # add tile updates
        if from_left >= 0:
            grid[from_top-1][from_left-1] = tiles[type]
            if type == 3:
                pos = (from_left, from_top)
            elif type == 4:
                ball = (from_left, from_top)
        else:
            score = type

    print(score)
