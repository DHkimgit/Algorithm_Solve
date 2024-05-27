from itertools import permutations

N, M = map(int, input().split())

array = list(map(int, input().split()))

result = []

for i in permutations(array, M):
    result.append(i)

result.sort()

for i in range(len(result)):
    for j in range(M):
        if j == M - 1:
            print(result[i][j])
        else:
            print(result[i][j], end=' ')
