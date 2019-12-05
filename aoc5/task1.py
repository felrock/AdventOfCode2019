import sys
def getParamVals(num, oc):

    # get param vals
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

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

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

                var1, var2 = getParamVals(oc[i], oc)
                oc[oc[i+3]] = var1 + var2

                # step
                step = 4

            elif (oc[i]%10) == 2:
                # Multiplication

                var1, var2 = getParamVals(oc[i], oc)
                oc[oc[i+3]] = var1 * var2

                # step
                step = 4

            elif oc[i] == 3:
                # Input

                print('give input: ', end='')
                x = input()
                oc[oc[i+1]] = int(x)

                # step
                step= 2

            elif oc[i] == 4:
                # Output

                var1 = oc[oc[i+1]]
                print('Output :', var1)
                # step
                step = 2
            i += step
