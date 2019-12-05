



if __name__ == '__main__':

    with open('input.txt', 'r') as f:

        # input
        steps1 = f.readline()
        steps2 = f.readline()

        steps1 = steps1.split(',')
        steps2 = steps2.split(',')

        line1 = {}
        intersects = {}

        start = (0,0)
        c_pos = (0,0)

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
        dists = []
        for key, item in intersects.items():
            dists.append(abs(key[0])+abs(key[1]))
        dists.sort(reverse=True)
        print(dists[-1])
