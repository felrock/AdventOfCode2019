from itertools import combinations
import sys

def applyGrav(pos1, pos2, mv1, mv2):

    # zero
    if pos1[0] < pos2[0]:
        mv1[0] += 1
        mv2[0] -= 1

    elif pos1[0] > pos2[0]:
        mv1[0] -= 1
        mv2[0] += 1

    # one
    if pos1[1] < pos2[1]:
        mv1[1] += 1
        mv2[1] -= 1

    elif pos1[1] > pos2[1]:
        mv1[1] -= 1
        mv2[1] += 1

    # two
    if pos1[2] < pos2[2]:
        mv1[2] += 1
        mv2[2] -= 1

    elif pos1[2] > pos2[2]:
        mv1[2] -= 1
        mv2[2] += 1

    return mv1, mv2

def updatePos(pos, velo):

    return [pos[0]+velo[0],
            pos[1]+velo[1],
            pos[2]+velo[2]]

def getEnergy(pos, velo):

    potential =  abs(pos[0])+abs(pos[1])+abs(pos[2])
    kinetic = abs(velo[0])+abs(velo[1])+abs(velo[2])
    return potential * kinetic

if __name__ == '__main__':


    with open(sys.argv[1], 'r') as f:

        bod = []
        vel = []
        steps = 1000
        for line in f:

            x, y, z = line.split(',')
            x = int(x[3:])
            y = int(y[3:])
            z = int(z[3:-2])
            bod.append([x, y, z])
            vel.append([0, 0, 0])


        body_index = [ i for i in range(len(bod))]
        comb = list(combinations(body_index, 2))
        print('all combos', comb)
        for i in range(steps):

            # update velo
            for c in comb:
                c0 = c[0]
                c1 = c[1]
                vel[c0], vel[c1] = applyGrav(bod[c0],
                                             bod[c1],
                                             vel[c0],
                                             vel[c1])

            #step
            for j in range(len(bod)):
                bod[j] = updatePos(bod[j], vel[j])

        all_energy = 0
        for b, v in zip(bod, vel):
            all_energy += getEnergy(b, v)
        print(all_energy)






















