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

    # variables to step fuel count, incrementing with
    # one takes too long
    tot = 0
    fuel = 1
    steps = [100000, 10000, 1000, 100, 10, 1]
    step_index = 0

    while True:

        # try with fuel count
        getOreCount('FUEL', fuel)

        # calculate ore use with chem stats dict
        tot = 0
        for key, item in chem_stats.items():

            amt_per_batch = chem_amt[key]
            ore_per_batch = chem_link[key][0][0]

            # round up batch size
            if item % amt_per_batch == 0:
                batch_size = item // amt_per_batch
            else:
                batch_size = item // amt_per_batch

            tot += batch_size*ore_per_batch

        if tot > 10**12 and step_index != len(steps)-1:
            # too much ore was used, reduce fuel and
            # decrease steps count for a more presicion
            fuel -= steps[step_index]
            step_index += 1

        elif tot > 10**12 and step_index == len(steps)-1:
            # found best fuel count, exit loop
            fuel -= steps[step_index]
            break

        # step fuel and clear previous executions dict
        fuel += steps[step_index]
        chem_stats = {}


    print('One trillion ore fuel amount:', fuel)



