import sys




if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        # read line and remove newline
        string = f.readline()[:-1]
        numbers= list(map(int, string[:]))

        # phase nums
        phase_numbers = [0, 1, 0, -1]
        phase = []
        all_phases = []

        for i in range(len(numbers)):
            phase.append(phase_numbers[i % 4])

        # add first phase
        all_phases.append(phase.copy()[1:])
        new_phase = phase.copy()
        for i in range(1, len(numbers)):
            new_phase = []
            while len(new_phase) < len(numbers):
                for j in range(


        # test 100 phases
        for _ in range(4):
            new_num = []
            for ph in all_phases:

                new_num.append(abs(sum([x*y for x, y in zip(ph, numbers)]))%10)
                print(ph)
            print('numbers,', numbers, 'new_num', new_num)
            print(ph)
            numbers = new_num
        print(new_num)
