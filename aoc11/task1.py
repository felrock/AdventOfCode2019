import sys
from collections import defaultdict

# set 1 for outputs verbose = 1
verbose = 1

class IntCodeMachine():

    def __init__(self):

        self.pc = 0
        self.r = 0
        self.ram = []
        self.halt = False
        self.exd = {}

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
        self.ram = defaultdict()

        # load into ram
        for i in range(len(oc)):
            self.ram[i] = oc[i]

    def run(self):
        """
            Runs the current state, program counter, inputs on the
            intcode machine. start is used to determine if this is
            the first run or not.
        """

        while self.ram[ self.pc ] != 99:
            #print('cur opcode', self.ram[self.pc])

            if self.ram[ self.pc ] % 10 == 1:
                # Addition

                var1, var2, var3 = self.getParamVals()
                if var3 > 0:
                    self.ram[var3] = var1 + var2

                else:
                    self.ram[self.ram[self.pc+3]] = var1 + var2

                # step
                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 2:
                # Multiplication

                var1, var2, var3 = self.getParamVals()
                if var3 > 0:
                    self.ram[var3] = var1 * var2

                else:
                    self.ram[self.ram[self.pc+3]] = var1 * var2

                # step
                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 3:
                # Input, only boot up stuff at start

                print('Input: ', end='')
                if self.ram[self.pc] == 203:
                    self.ram[self.r + self.ram[self.pc + 1]] = int(input())

                else:
                    self.ram[ self.ram[ self.pc + 1 ] ] = int(input())

                # step
                self.pc += 2

            elif self.ram[ self.pc ] % 10 == 4:
                # Output

                var1, var2, var3 = self.getParamVals()
                # step
                self.pc += 2
                return var1

            elif self.ram[ self.pc ] % 10 == 5:
                # jump if true

                var1, var2, var3 = self.getParamVals()
                if var1 != 0:
                    self.pc = var2

                else:
                    self.pc += 3

            elif self.ram[ self.pc ] % 10 == 6:
                # jump if true

                var1, var2, var3 = self.getParamVals()
                if var1 == 0:
                    self.pc = var2

                else:
                    self.pc += 3

            elif self.ram[ self.pc ] % 10 == 7:
                # Less than

                var1, var2, var3 = self.getParamVals()
                if var3 == 0:
                    var3 = self.ram[self.pc+3]

                if var1 < var2:
                    self.ram[ var3 ] = 1

                else:
                    self.ram[ var3 ] = 0

                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 8:
                # equals

                var1, var2, var3 = self.getParamVals()
                if var3 == 0:
                    var3 = self.ram[self.pc+3]

                if var1 == var2:
                    self.ram[ var3 ] = 1

                else:
                    self.ram[ var3 ] = 0

                self.pc += 4

            elif self.ram[ self.pc ] % 10 == 9:

                var1, var2, var3 = self.getParamVals()
                self.r += var1
                self.pc += 2

        # amp halted return True
        self.halt = True
        return 0

    def getParamVals(self):
        """
            Parse intermediate and position values
        """

        # remove opcode
        p = self.ram[self.pc]//100
        p1 = p % 10
        p2 = (p // 10)%10
        p3 = (p // 10)//10
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

def enterFuncDebug(*args):
    """
        prints args for debug purposes
    """

    string = '# Entering {} : index {}, in {}, p {}, start {}'.format(*args)
    print(string)


if __name__ == '__main__':

    machine = IntCodeMachine()
    machine.load(sys.argv[1])

    while not machine.halt:

        print('output: ', machine.run())
