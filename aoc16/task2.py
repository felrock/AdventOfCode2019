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

        # add first phase
        for i in range(1, len(numbers)+1):

            new_phase = []
            num_index = 0
            while len(new_phase) < len(numbers)+1:
                new_phase += [phase_numbers[num_index%4]]*i
                num_index += 1

            diff = len(new_phase)-len(numbers)-1
            if diff > 0:
                new_phase = new_phase[1:-diff]
            else:
                new_phase = new_phase[1:]
            all_phases.append(new_phase)

        # test 100 phases
        t = {}
        for _ in range(100):
            new_num = []
            for ph in all_phases:
                new_num.append(abs(sum([x*y for x, y in zip(ph, numbers)]))%10)
            string = ''.join(list(map(str, numbers)))
            print(string)
            numbers = new_num
        for key, item in t.items():

            print(item)
        print(''.join(list(map(str, numbers))[:8]))
