word = str(input())
result = 0
matrix = [([0, 1, 2], 3), ([3, 4, 5], 4), ([6, 7, 8], 5), ([9, 10, 11], 6), 
          ([12, 13, 14], 7), ([15, 16, 17, 18], 8), ([19, 20, 21], 9), ([22, 23, 24, 25], 10)]

for char in word:
    target = ord(char) - 65
    for i in range(len(matrix)):
        if target in matrix[i][0]:
            result += matrix[i][1]
            break
print(result)        