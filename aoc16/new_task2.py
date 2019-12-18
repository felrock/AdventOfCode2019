"""


Since part two was revealed to me I now recognize that this method is
really slow compared to what it could be. Multiplying is just waste of
computation since we are only multiplying with 1, 0, -1. There are
plenty of numbers in the signal that will be excluded of the sum, where
the filter is zero. These excluded numbers indexes can be stored.

This speeds up task1 from 2.27s to 0.2s

Having 10,000 times the input signal creates a lot of repetition,

so if we look for a the start of a sequence we could take sum the
sequence over 10,000*input_size

I looked for clues on reddit..

One clue cracked the whole thing open, "check if the offset index
is located in the second part of the input numbers". This is huge,
if the offset in the second half, we only need to care about the
positive summation. Solution is as follows.

"""


import sys

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        # read line and remove newline
        string  = f.readline()[:-1]
        numbers = list(map(int, string[:]))
        offset = int(string[:7])
        numbers = (numbers*10000)[offset:]
        for _ in range(100):
            num_sum = 0
            for i in range(len(numbers)-1, -1, -1):
                numbers[i] = num_sum = (num_sum + numbers[i])%10


print(''.join(list(map(str, numbers))[:8]))
