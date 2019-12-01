

def addFuel(fuel):
    more_fuel = (fuel//3) - 2

    if more_fuel > 0:
        return more_fuel + addFuel(more_fuel)
    else:
        return 0

if __name__ == '__main__':

    sum = 0
    with open('input.txt', 'r') as f:
        for line in f:
            sum += addFuel(int(line))
    print(sum)
