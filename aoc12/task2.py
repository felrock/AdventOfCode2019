from itertools import combinations
import sys

# https://www.programiz.com/python-programming/examples/lcm
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def applyGrav(pos1, pos2, mv1, mv2):

    # zero

    for i in range(len(pos1)):
       if pos1[i] < pos2[i]:
           mv1[i] += 1
           mv2[i] -= 1

       elif pos1[i] > pos2[i]:
           mv1[i] -= 1
           mv2[i] += 1

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

        # create all the body to body combinations
        body_index = [ i for i in range(len(bod))]
        comb = list(combinations(body_index, 2))
        nums = []
        for dim in range(3):
            state_dict = {}
            i = 0
            while True:
                # update velo
                for c in comb:
                    c0 = c[0]
                    c1 = c[1]
                    vel[c0], vel[c1] = applyGrav(bod[c0],
                                                 bod[c1],
                                                 vel[c0],
                                                 vel[c1])
                # step
                for j in range(len(bod)):
                    bod[j] = updatePos(bod[j], vel[j])

                # add state to dict
                state = []
                for k in range(len(bod)):
                    state.append(bod[k][dim])
                    state.append(vel[k][dim])
                state = tuple(state)

                if state in state_dict:
                    break
                else:
                    state_dict[state] = 1
                i += 1

            nums.append(i)

        print(compute_lcm(compute_lcm(nums[2], nums[1]), nums[0]))
