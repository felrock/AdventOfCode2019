import sys


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        # Read input
        input_string = f.readline()

        # Make integers
        oc = input_string.split(',')
        oc = list(map(int, oc))
        org_oc = oc.copy()

        # brute force solution
        for verb in range(99):
            for noun in range(99):

                # vars
                i = 0
                step = 4
                oc = org_oc.copy()
                oc[1] = noun
                oc[2] = verb
                while oc[i] != 99:

                    if oc[i] == 1:
                        oc[oc[i+3]] = oc[oc[i+2]] + oc[oc[i+1]]

                    elif oc[i] == 2:
                        oc[oc[i+3]] = oc[oc[i+2]] * oc[oc[i+1]]

                    else:
                        print('error, opcode ', oc[i])
                        sys.exit()

                    i += step

                if oc[0] == 19690720:
                    print(100*noun + verb)
