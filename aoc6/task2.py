import sys

def walk(itm, relation):
    # walks the relation tree, add nodes to dict

    walk = {}
    key_temp = itm

    while key_temp in relation:

        walk[relation[key_temp]] = 1
        key_temp = relation[key_temp]

    return walk

def countNonEqRelation(a, b):
    # takes two dicts and counts items that are
    # non similar, looks

    count = 0
    for key, _ in a.items():
        if not key in b:
            count += 1

    for key, _ in b.items():
        if not key in a:
            count += 1

    return count

if __name__ == '__main__':

    orbits = []
    with open(sys.argv[1], 'r') as f:

        for line in f:
            orbits.append(line)

    direct_orbits = len(orbits)
    indirect_orbits = 1
    objects = {}
    relation = {}
    me = 'YOU'
    santa = 'SAN'

    # get all the relations in a dict
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

    # walk me and santa upp the relation tree
    walk_me = walk(me, relation)
    walk_santa = walk(santa, relation)

    count = countNonEqRelation(walk_me, walk_santa)

    print('moved between me and santa', count)
