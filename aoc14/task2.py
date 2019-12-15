import sys
import math


# dicts for loopups
chem_link  = {}
chem_amt   = {}
chem_rest  = {}
chem_stats = {}

def getOreCount(node, amp):

    if chem_link[node][0][1] == 'ORE':

        # update chem stats dict
        if node in chem_stats:
            chem_stats[node] += amp*chem_amt[node]
        else:
            chem_stats[node] = amp*chem_amt[node]

    else:

        for cmp in chem_link[node]:

            lbl = cmp[1]            # component label
            val = amp*int(cmp[0])   # amount of component needed(amped)
            apb = chem_amt[lbl]     # amount per batch

            # look if there are stored rests
            if lbl in chem_rest:
                val -= chem_rest[lbl]
                del chem_rest[lbl]

            # calculate batches, round up
            if val % apb == 0:
                batch_size = val // apb
            else:
                batch_size = (val // apb) + 1

            # cal rest
            rest = batch_size*apb - val

            # add to rest dep
            if rest > 0:
                chem_rest[lbl] = rest

            getOreCount(lbl, batch_size)



if __name__ == '__main__':


    with open(sys.argv[1], 'r') as f:

        for line in f:

            # remove newline
            line = line[:-1]

            # split
            lhs, rhs = line.split(' => ')

            # right hand side parsing
            amt, label = rhs.split(' ')
            chem_amt[label] = int(amt)

            # left hand side parsing
            components = []
            for comp in lhs.split(', '):
                val, lbl = comp.split(' ')
                components.append((int(val), lbl))
            chem_link[label] = components

    # run recursive search
    tot = 0
    fuel = 1
    while tot < 10**12:

        getOreCount('FUEL', fuel)

        # calculate ore use with chem stats dict
        tot = 0
        for key, item in chem_stats.items():

            amt_per_batch = chem_amt[key]
            ore_per_batch = chem_link[key][0][0]

            if item % amt_per_batch == 0:
                batches = item // amt_per_batch
            else:
                batches = item // amt_per_batch

            tot += batches*ore_per_batch
        print(tot)
        fuel += 1
        if fuel == 10:
            sys.exit()

    print(fuel)
