from itertools import combinations

N, S = map(int, input().split())

array = list(map(int, input().split()))

result = 0

for i in range(1, N+1):
    comb = []
    
    for k in combinations(array, i):
        comb.append(k)

    for j in range(len(comb)):
        comb_sum = 0
        for l in range(i):
            comb_sum += comb[j][l]
        
        if comb_sum == S:
            result += 1

print(result)
    