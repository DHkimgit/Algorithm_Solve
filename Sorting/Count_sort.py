array = [7, 5, 3, 3, 0, 8, 5, 6, 2, 1, 3 ,4, 2, 4, 8]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
