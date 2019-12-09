import sys
import itertools


# set 1 for outputs
verbose = 1


class IntCodeMachine():

    def __init__(self):

        self.pc = 0
        self.r = 0
        self.ram = []

    def run(self, input=None):
        """
            Runs the current state, program counter, inputs on the
            intcode machine. start is used to determine if this is
            the first run or not.
        """

        # init
        i = self.pc
        r = self.r
        oc = self.pc

        while oc[i] != 99:

            if (oc[i]%10) == 1:
                # Addition
                var1, var2 = getParamVals(oc, i)
                oc[oc[i+3]] = var1 + var2

                # step
                i += 4

            elif (oc[i]%10) == 2:
                # Multiplication
                var1, var2 = getParamVals(oc, i)
                oc[oc[i+3]] = var1 * var2

                # step
                i += 4

            elif oc[i] == 3:
                # Input, only boot up stuff at start

                oc[oc[i+1]] = input
                # step
                i += 2

            elif oc[i] == 4:
                # Output

                # amp continues, return halt false
                if verbose:
                    print('# Exit with output at ', i+2, oc[i])
                return oc[oc[i+1]], oc, i+2, False
                # step

            elif oc[i]%10 == 5:
                # jump if true

                var1, var2 = getParamVals(oc, i)
                if var1 != 0:
                    i = var2
                else:
                    i += 3

            elif oc[i]%10 == 6:
                # jump if true

                var1, var2 = getParamVals(oc, i)
                if var1 == 0:
                    i = var2
                else:
                    i += 3

            elif oc[i]%10 == 7:
                # Less than

                var1, var2 = getParamVals(oc, i)
                if var1 < var2:
                    oc[oc[i+3]] = 1
                else:
                    oc[oc[i+3]] = 0
                i += 4

            elif oc[i]%10 == 8:
                # equals

                var1, var2 = getParamVals(oc, i)
                if var1 == var2:
                    oc[oc[i+3]] = 1
                else:
                    oc[oc[i+3]] = 0
                i += 4

            elif oc[i]%10 == 9:

                self.r = oc[i+1]
                i += 2

        # amp halted return True
        return 0, oc, i, True

    def getParamVals(self, oc, i):
        """
            Parse intermediate and position values
        """

        # remove opcode
        p = oc[i]//100

        if (p & 1):
            var1 = oc[i+1]
        elif p & 2:
            var1 = oc[oc[r]]
        else:
            var1 = oc[oc[i+1]]
        # shift one, 2nd para
        p >>= 1
        if (p & 1):
            var1 = oc[i+1]
        elif p & 2:
            var1 = oc[oc[r]]
        else:
            var1 = oc[oc[i+1]]

        return var1, var2


def enterFuncDebug(*args):
    """
        prints args for debug purposes
    """

    string = '# Entering {} : index {}, in {}, p {}, start {}'.format(*args)
    print(string)


def loadProgram():
    """
        Read program code from file
    """

    f = open(sys.argv[1], 'r')

    # Read input
    input_string = f.readline()

    # Make integers
    oc = input_string.split(',')
    oc = list(map(int, oc))

    return oc


if __name__ == '__main__':

    # create permutations of pos intput
    perm = list(itertools.permutations([5,6,7,8,9], 5))
    #perm = [[9,8,7,6,5]]

    # read program
    program = loadProgram()
