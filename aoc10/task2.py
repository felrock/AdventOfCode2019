import math
import sys
import numpy as np

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """

    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """

    v1_u = unit_vector(np.array(v1))
    v2_u = unit_vector(np.array(v2))
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def getVec(pos1, pos2):
    """
        get vec as steps
    """
    x1 = pos2[0] - pos1[0]
    y1 = pos2[1] - pos1[1]
    gcd1 = math.gcd(abs(x1), abs(y1))

    if gcd1 > 0:
        x = x1//gcd1
    else:
        x = x1
    if gcd1 > 0:
       y = y1//gcd1
    else:
       y = y1

    return x, y

def getOuterPos(height, width):
    """
        get the positions that furthest away from the asteroid.
    """

    positions = []
    for i in range(width/2):
        positions.append(((width/2)+i, 0))

    for i in range(height):
        positions.append((width-1, i))

    for i in range(width):
        positions.append((width-i, height-1))

    for i in range(height):
        positions.append((0, height-1-i))

    for i in range((width/2)-1):
        positions.append((i, 0))

    return positions

def inRange(lower, upper, pos):

    if lower[0] <= pos[0] and lower[1] <= pos[1] and upper[0] >= pos[0] and upper[1] >= pos[1]:
        return True
    return False

def findRemove(itm, list):

    for i in list:

        if i[0] == itm[0] and i[1] == itm[1]:
            break
    list.remove(i)


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        asteroids = []
        asteroidsD = {}
        x, y = 0, 0
        width = 28
        height = 27
        center = (17, 23)
        start = (1, 0)

        for line in f:

            for chr in line:

                if chr == '#':
                    if (x, y) != center:
                        vec = getVec(center, (x, y))
                        ang = angle_between(start, vec)
                        asteroids[(x,y)] = (ang,vec)
                        asteroidsD[(x, y)] = 1
                x += 1

            y += 1
            x = 0

        maxA = 0
        posA = None

        asteroids.sort(key=lambda x:x[2])
        count = 0
        for ast in asteroids:


            vec = ast[3]
            pos = (ast[0], ast[1])
            cur = center
            while cur != pos:

                if cur in asteroidsD:



                cur = (vec[0]+cur[0], vec[1]+cur[1])




            count = 0
            for asteroid2 in asteroids.keys():

                if asteroid1 == asteroid2:
                    continue


                vec = getVec(asteroid1, asteroid2)
                newPos = (asteroid1[0]+vec[0], asteroid1[1]+vec[1])
                while inRange((0,0), (width, height), newPos):
                    if newPos == asteroid2:
                        count += 1
                        break
                    elif newPos in asteroids:
                        break

                    newPos = (newPos[0]+vec[0], newPos[1]+vec[1])
            if count > maxA:
                maxA = count
                posA = asteroid1


        print('Asteroid {} has {} asteroids in range'.format(posA,maxA))
