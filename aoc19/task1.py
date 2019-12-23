from intcode import *
import sys

if __name__ == '__main__':

    out_sum = 0
    machine = IntCode(sys.argv[1])
    for i in range(50):
        for j in range(50):

            if machine.run([i, j]):
                out_sum += 1
            machine.reset()
    print(out_sum)
