import sys
import itertools


# set 1 for outputs
verbose = 1

def enterFuncDebug(*args):
    """
        prints args for debug purposes
    """

    string = '# Entering {} : index {}, in {}, p {}, start {}'.format(*args)
    print(string)

def getParamVals(oc, i):
    """
        Parse intermediate and position values
    """

    # get param vals
    num = oc[i]
    p = num//100
    if (p & 1):
        var1 = oc[i+1]
    else:
        var1 = oc[oc[i+1]]

    if (p & 10):
        var2 = oc[i+2]
    else:
        var2 = oc[oc[i+2]]

    return var1, var2

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

def machine(phase, sig_input, state, pc, start):
    """
        Runs the current state, program counter, inputs on the
        intcode machine. start is used to determine if this is
        the first run or not.
    """

    # init
    i = pc
    oc = state
    phase_start = start

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

            if phase_start:
                # start means phase input, only once

                oc[oc[i+1]] = phase
                phase_start = False
            else:
                oc[oc[i+1]] = sig_input

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

    # amp halted return True
    return 0, oc, i, True

if __name__ == '__main__':

    # create permutations of pos intput
    perm = list(itertools.permutations([5,6,7,8,9], 5))
    #perm = [[9,8,7,6,5]]

    # read program
    program = loadProgram()

    # start up settings
    e = 0
    max = 0
    for p in perm:

        # states, RAM
        stateA = program.copy()
        stateB = program.copy()
        stateC = program.copy()
        stateD = program.copy()
        stateE = program.copy()

        # halts
        haltA = False
        haltB = False
        haltC = False
        haltD = False
        haltE = False

        # program counters
        iA = 0
        iB = 0
        iC = 0
        iD = 0
        iE = 0

        start = True
        while not (haltA and haltB and haltC and haltD and haltE):
            if verbose:
                enterFuncDebug('A', iA, e, p[0], start)

            a, stateA, iA, haltA = machine(p[0],e,stateA,iA,start)
            if verbose:
                enterFuncDebug('B', iB, a, p[1], start)

            b, stateB, iB, haltB = machine(p[1],a,stateB,iB,start)
            if verbose:
                enterFuncDebug('C', iC, b, p[2], start)

            c, stateC, iC, haltC = machine(p[2],b,stateC,iC,start)
            if verbose:
                enterFuncDebug('D', iD, c, p[3], start)

            d, stateD, iD, haltD = machine(p[3],c,stateD,iD,start)
            if verbose:
                enterFuncDebug('E', iE, d, p[4], start)

            e, stateE, iE, haltE = machine(p[4],d,stateE,iE,start)
            start = False
            if verbose:
                print('# Iteration finished, outputs were, ',a,b,c,d,e)

            if e > max:
                max = e

    print('Max output was: ', max)
