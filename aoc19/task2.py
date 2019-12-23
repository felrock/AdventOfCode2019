from intcode import *
import sys

if __name__ == '__main__':

    machine = IntCode(sys.argv[1])
    steps = [500, 100, 50, 20, 10, 1]
    si = 0
    cur  = 500

    while True:
        # walk beam in y-axis
        most_right = [1, cur]
        for i in range(1, cur, 10):
            t = machine.run([i, cur])
            if t:
                most_right = [i, cur]

            machine.reset()

        # move forward until beam ends
        machine.reset()
        while machine.run(most_right):
            most_right[0] += 1
            machine.reset()

        # move one back into the beam
        most_right[0] -= 1

        # reset
        machine.reset()

        # test 100 down 100 left
        most_right1 = [most_right[0]-99, most_right[1]+99]
        t1 = machine.run(most_right1)
        machine.reset()

        # test 100 down 100 left
        most_right2 = [most_right[0]-100, most_right[1]+99]
        t2 = machine.run(most_right2)

        if t2 and t1:
            cur -= steps[si]
            si += 1
            continue
        elif not t2 and t1:
            print(most_right1[0]*10000 + most_right1[1]-99)
            break
        else:
            cur += steps[si]
            continue

