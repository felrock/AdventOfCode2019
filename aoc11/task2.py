import sys
from collections import defaultdict
from intcode import *
import numpy as np


# set 1 for outputs verbose = 1
verbose = 1

class IntCodeMachine():

    def __init__(self):

        self.pc = 0
        self.r = 0
        self.ram = None
        self.halt = False

    def load(self, filename):
        """
            Read program code from file
        """

        f = open(filename, 'r')

        # Read input
        input_string = f.readline()

        # Make integers
        oc = input_string.split(',')
        oc = list(map(int, oc))
        self.ram = defaultdict(lambda: 0)

        # load into ram
        for i in range(len(oc)):
            self.ram[i] = oc[i]

    def run(self, in_sig=None):
        """
            Runs the current state, program counter, inputs on the
            intcode machine. start is used to determine if this is
            the first run or not.
        """

        while self.ram[ self.pc ] != 99:
            print('Opcode :', self.ram[self.pc], self.pc)
            if self.ram[ self.pc ] % 10 == 1:
                # Addition

                var1, var2, var3 = self.param()
                if var3 > 0:
                    self.ram[var3] = var1 + var2

                else:
                    self.ram[self.ram[self.pc+3]] = var1 + var2

                # step
                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 2:
                # Multiplication

                var1, var2, var3 = self.param()
                if var3 > 0:
                    self.ram[var3] = var1 * var2

                else:
                    self.ram[self.ram[self.pc+3]] = var1 * var2

                # step
                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 3:
                # Input, only boot up stuff at start

                if self.ram[self.pc] == 203:
                    self.ram[self.r + self.ram[self.pc+1]] = in_sig

                else:
                    self.ram[self.ram[self.pc+1]] = in_sig

                # step
                self.pc += 2

            elif self.ram[ self.pc ] % 10 == 4:
                # Output

                var1, var2, var3 = self.param()

                # step
                self.pc += 2
                return var1

            elif self.ram[ self.pc ] % 10 == 5:
                # jump if true

                var1, var2, var3 = self.param()
                if var1 != 0:
                    self.pc = var2

                else:
                    self.pc += 3

            elif self.ram[ self.pc ] % 10 == 6:
                # jump if true

                var1, var2, var3 = self.param()
                if var1 == 0:
                    self.pc = var2

                else:
                    self.pc += 3

            elif self.ram[ self.pc ] % 10 == 7:
                # Less than

                var1, var2, var3 = self.param()
                if var3 == 0:
                    var3 = self.ram[self.pc+3]

                if var1 < var2:
                    self.ram[ var3 ] = 1

                else:
                    self.ram[ var3 ] = 0

                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 8:
                # equals

                var1, var2, var3 = self.param()
                if var3 == 0:
                    var3 = self.ram[self.pc+3]

                if var1 == var2:
                    self.ram[ var3 ] = 1

                else:
                    self.ram[ var3 ] = 0

                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 9:
                # update relative pointer

                print(self.ram[self.pc])
                var1, var2, var3 = self.param()
                self.r += var1
                self.pc += 2

        # amp halted return True
        self.halt = True
        return -1

    def param(self):
        """
            Parse intermediate and position values
        """

        # remove opcode
        v = str(self.ram[self.pc])
        if len(v) == 1:

            return 0,0,0
        else:

            v = v[:-2]
            v1 = v[-1]
            v = v[:-1]
            if not v:
                return self.values(int(v1), 0, 0)
            v2 = v[-1]
            v = v[:-1]
            if not v:

                return self.values(int(v1), int(v2), 0)
            else:

                return self.values(int(v1), int(v2), int(v))

    def values(self, p1, p2, p3):

        # first
        var1, var2, var3 = 0, 0, 0
        if p1 == 1:
            var1 = self.ram[self.pc+1]

        elif p1 == 2:
            var1 = self.ram[self.r+self.ram[self.pc+1]]

        else:
            var1 = self.ram[self.ram[self.pc+1]]

        # second
        if p2 == 1:
            var2 = self.ram[self.pc+2]

        elif p2 == 2:
            var2 = self.ram[self.r + self.ram[self.pc+2]]

        # thrid
        if p3 == 2:
            var3 = self.r + self.ram[self.pc+3]


        return var1, var2, var3

def rot(dir, new_dir):

    left, right = 0, 1
    dir_up =   (0, -1)
    dir_left = (-1, 0)
    dir_down = (0, 1)
    dir_right =(1, 0)

    if new_dir == left:

        if dir == dir_up:
            return dir_left

        if dir == dir_down:
            return dir_right

        if dir == dir_right:
            return dir_up

        return dir_down
    else:

        if dir == dir_up:
            return dir_right

        if dir == dir_down:
            return dir_left

        if dir == dir_left:
            return dir_up

        return dir_down



if __name__ == '__main__':

    machine = IntCode(sys.argv[1])
    panels = defaultdict(lambda: 0)
    start = (0, 0)
    position = start
    dir = (0, 1)
    black = 0
    white = 1
    left = 0
    current_color = white

    while not machine.halt:

        # get vals
        out1 = machine.run(current_color)
        out2 = machine.run(current_color)

        if out1 == black:
            panels[position] = black
        else:
            panels[position] = white

        dir = rot(dir, out2)
        position = (position[0]+dir[0], position[1]+dir[1])
        #print('current pos', position)
        current_color = panels[position]
        #print('current_color', current_color)

    minX = min([ k[0] for k in panels.keys() ])
    minY = min([ k[1] for k in panels.keys() ])
    maxX = max([ k[0] for k in panels.keys() ])
    maxY = max([ k[1] for k in panels.keys() ])

    moveX = abs(minX)
    moveY = abs(minY)

    grid = [['.' for _ in range(moveX+maxX+1)] for _ in range(moveY+maxY+1) ]
    for key, item in panels.items():
        if item == white:
            grid[(key[1]+moveY)][(key[0]+moveX)] = '#'


    grid.reverse()
    for col in grid:
        col.reverse()
        for row in col:
            print(row, end='')
        print()
