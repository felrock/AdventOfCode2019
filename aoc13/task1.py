from intcode import *
import sys



if __name__ == '__main__':

    machine = IntCode(sys.argv[1])
    cnt = 0
    while not machine.halt:
        from_left = machine.run()
        from_top = machine.run()
        type = machine.run()
        if type:
            if type == 2:
                cnt += 1

    print(cnt)
