import sys
from intcode import *

def isAligned(point, grid):

    x, y = point[0], point[1]
    if x + 1 < len(grid[0])-1 and grid[y][x+1] != '#':
        return False

    if x - 1 > 0 and grid[y][x-1] != '#':
        return False

    if y + 1 < len(grid)-1 and grid[y+1][x] != '#':
        return False

    if y - 1 > 0 and grid[y-1][x] != '#':
        return False

    return True




if __name__ == '__main__':

    machine = IntCode(sys.argv[1])
    grid = []
    row  = []
    while not machine.halt:
        out = machine.run()
        if out == 35:
            row.append('#')
        elif out == 46:
            row.append('.')
        elif out == 10:
            grid.append(row)
            row = []
        elif out:
            row.append(chr(out)+'')
    para = 0
    grid = grid[:-1]
    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if isAligned((j, i), grid) and grid[i][j] == '#':
                para += i*j
                print('x', end='')
            else:
                print(grid[i][j], end='')
        print()

    print(para)
