import sys


if __name__ == '__main__':

    orbits = []
    with open(sys.argv[1], 'r') as f:

        for line in f:
            orbits.append(line)

    direct_orbits = len(orbits)
    indirect_orbits = 1
    objects = {}
    relation = {}

    for orb in orbits:

        a, b = orb.split(')')
        b = b[:-1]

        # get all the items
        if not a in objects:
            objects[a] = 1
        if not b in objects:
            objects[b] = 1

        # add orbit relation
        relation[b] = a

    for key, item in objects.items():

        indir_temp = -1
        key_temp = key

        # walk the relation tree
        while key_temp in relation:
            key_temp = relation[key_temp]
            indir_temp += 1

        indirect_orbits += indir_temp

    # print stuff
    print('dir',direct_orbits,' indirect_orbits',indirect_orbits)
    print(direct_orbits + indirect_orbits)

