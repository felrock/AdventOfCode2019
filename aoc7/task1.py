import sys
import itertools

def getParamVals(oc, i):

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

def intcodeMachine(inputs):

    k = 0
    output = 0

    f = open(sys.argv[1], 'r')

    # Read input
    input_string = f.readline()

    # Make integers
    oc = input_string.split(',')
    oc = list(map(int, oc))

    # vars
    i = 0
    step = 0
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
            # Input

            oc[oc[i+1]] = inputs[k]
            k += 1

            # step
            i += 2

        elif oc[i] == 4:
            # Output

            return oc[oc[i+1]]
            # step
            i += 2

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

    return output

if __name__ == '__main__':

    # create permutations of pos intput
    perm = list(itertools.permutations([0,1,2,3,4], 5))
    max = 0

    for p in perm:

        a= intcodeMachine([p[0],0])
        b= intcodeMachine([p[1],a])
        c= intcodeMachine([p[2],b])
        d= intcodeMachine([p[3],c])
        e= intcodeMachine([p[4],d])
        if e > max:
            max = e
    print(max)
