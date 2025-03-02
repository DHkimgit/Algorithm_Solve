from itertools import permutations

N, K = map(int, input().split())
A = list(map(int, input().split()))

routines = []

for i in permutations(A, N):
    routines.append(i)

def check_routine(routine:dict, K: int):
    weight = 500
    for i in routine:
        weight -= K
        weight += i
        if weight < 500:
            return False 
    
    return weight >= 500

result = 0

for i in routines:
    if check_routine(i, K):
        result += 1

print(result)