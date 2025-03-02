word = str(input())
matrix = [-1 for i in range(26)]

for i in range(len(word)):
    j = word[i]
    index = ord(j) - 97
    if matrix[index] == -1:
         matrix[index] = i

for i in matrix:
    print(i, end=' ')