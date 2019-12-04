
if __name__ == '__main__':

    with open('input.txt', 'r') as f:

        low, high = f.readline().split('-')
        low = int(low)
        high = int(high)
        passwords = []

        for num in range(low, high+1):

            num_str = str(num)
            found_dub = False
            found_dec = True
            eq_num = 0

            # find pair
            for i in range(len(num_str)-1):

                if num_str[i] == num_str[i+1]:
                    eq_num += 1
                else:
                    if eq_num == 1:
                        found_dub = True
                    eq_num = 0

                if num_str[i] > num_str[i+1]:

                    found_dec = False
                    break

            if (found_dub or eq_num == 1) and found_dec:
                passwords.append(num_str)

        print(len(passwords))
