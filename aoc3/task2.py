def walk(steps, c_pos, dest):

    steps_wire = 0

    for s in steps:

        if s[0] == 'R':
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0]+1, c_pos[1])
                steps_wire += 1
                if c_pos == dest:
                    return steps_wire
                move -= 1
        elif s[0] == 'U':
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0], c_pos[1]+1)
                steps_wire += 1
                if c_pos == dest:
                    return steps_wire
                move -= 1
        elif s[0] == 'L':
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0]-1, c_pos[1])
                steps_wire += 1
                if c_pos == dest:
                    return steps_wire
                move -= 1
        else:
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0], c_pos[1]-1)
                steps_wire += 1
                if c_pos == dest:
                    return steps_wire
                move -= 1

def makeWire(steps, c_pos, steps_d):

    for s in steps1:

        if s[0] == 'R':
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0]+1, c_pos[1])
                line1[c_pos] = 1
                move -= 1
        elif s[0] == 'U':
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0], c_pos[1]+1)
                line1[c_pos] = 1
                move -= 1
        elif s[0] == 'L':
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0]-1, c_pos[1])
                line1[c_pos] = 1
                move -= 1
        else:
            move = int(s[1:])
            while move > 0:
                c_pos = (c_pos[0], c_pos[1]-1)
                line1[c_pos] = 1
                move -= 1



if __name__ == '__main__':

    with open('input.txt', 'r') as f:

        # input
        steps1 = f.readline()
        steps2 = f.readline()

        steps1 = steps1.split(',')
        steps2 = steps2.split(',')

        start = (0,0)
        c_pos = (0,0)

        line1 = {}
        makeWire(steps1, c_pos, line1)
        intersects = {}

        c_pos = start
        for s in steps2:

            if s[0] == 'R':
                move = int(s[1:])
                while move > 0:
                    c_pos = (c_pos[0]+1, c_pos[1])
                    if c_pos in line1:
                        intersects[c_pos] = 1
                    move -= 1
            elif s[0] == 'U':
                move = int(s[1:])
                while move > 0:
                    c_pos = (c_pos[0], c_pos[1]+1)
                    if c_pos in line1:
                        intersects[c_pos] = 1
                    move -= 1
            elif s[0] == 'L':
                move = int(s[1:])
                while move > 0:
                    c_pos = (c_pos[0]-1, c_pos[1])
                    if c_pos in line1:
                        intersects[c_pos] = 1
                    move -= 1
            else:
                move = int(s[1:])
                while move > 0:
                    c_pos = (c_pos[0], c_pos[1]-1)
                    if c_pos in line1:
                        intersects[c_pos] = 1
                    move -= 1

        ww_dict = {}
        dist = -1
        # walk to all the intersections
        for key, item in intersects.items():

            d = walk(steps2, (0,0), key)+walk(steps1, (0,0), key)
            if dist == -1:
                dist = d
            elif dist > d:
                dist = d

        print(dist)

