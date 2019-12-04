



if __name__ == '__main__':

    with open('input.txt', 'r') as f:

        low, high = f.readline().split('-')
        low = int(low)
        high = int(high)
        passwords = []

        for num in range(low, high+1):
            prev_cv= ''
            num_str = str(num)
            found_dub = False
            found_inc = True

            # find pair
            for i in range(len(num_str)-1):
                if num_str[i] == num_str[i+1]:
                    found_dub = True
                if num_str[i] > num_str[i+1]:
                    found_inc = False
                    break

            if found_dub and found_inc:
                passwords.append(num_str)

        print(len(passwords))
