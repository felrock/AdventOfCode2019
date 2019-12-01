sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        sum += (int(line) // 3) - 2
print(sum)
