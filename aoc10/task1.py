import math
import sys

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
    for i in range(height):
        positions.append((0, i))

    for i in range(width):
        positions.append((i, height-1))

    for i in range(height):
        positions.append((width-1, height-1-i))

    for i in range(width):
        positions.append((width-1-i, 0))

    return positions

def inRange(lower, upper, pos):

    if lower[0] <= pos[0] and lower[1] <= pos[1] and upper[0] >= pos[0] and upper[1] >= pos[1]:
        return True
    return False

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        asteroids = {}
        x, y = 0, 0
        width = 28
        height = 27

        for line in f:

            for chr in line:

                if chr == '#':
                    asteroids[(x,y)] = 1
                x += 1

            y += 1
            x = 0

        maxA = 0
        posA = None
        for asteroid1 in asteroids.keys():

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
