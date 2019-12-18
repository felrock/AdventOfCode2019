"""
Since part two was revealed to me I now recognize that this method is
really slow compared to what it could be. Multiplying is just waste of
computation since we are only multiplying with 1, 0, -1. There are
plenty of numbers in the signal that will be excluded of the sum, where
the filter is zero. These excluded numbers indexes can be stored.

This speeds up task1 from 2.27s to 0.2s

"""


import sys

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        # read line and remove newline
        string  = f.readline()[:-1]
        numbers = list(map(int, string[:]))

        # phase nums
        phase_numbers     = [1, 0, -1]
        ones_start_index  = 0
        mones_start_index = 0
        phase_length      = 0

        # test 100 phases
        for _ in range(int(sys.argv[2])):

            new_num    = []

            for phase in range(len(numbers)):

                index = phase
                sum_numbers = 0
                step = 2*phase +2
                sign_shift = 0

                while index < len(numbers):
                    # pos sum
                    if sign_shift == 0:

                        sum_numbers += sum(numbers[index:index+phase+1])
                        sign_shift = 1
                    else:
                        sum_numbers -= sum(numbers[index:index+phase+1])
                        sign_shift = 0

                    # skip zeros
                    index += step
                new_num.append(abs(sum_numbers)%10)
            numbers = new_num

        print(''.join(list(map(str, new_num))))
