import math
M, N = map(int, input().split())

array = []

for i in range(M, N+1):
    array.append(i)

def check_prime_number(N):
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

for i in range(len(array)):
    if array[i] == 0 or array[i] == 1:
        continue
    
    if check_prime_number(array[i]) == True:
        j = 2
        while array[i] * j < array[-1]:
            array[i + array[i]*(j-1)] = 0
            j += 1
    
    else:
        j = 2
        while array[i] * j < array[-1]:
            array[i + array[i]*(j-1)] = 0
            j += 1
        array[i] = 0

if array[0] == 1:
    for i in range(1, len(array)):
        if array[i] != 0:
            print(array[i])

else:
    for i in range(len(array)):
        if array[i] != 0:
            print(array[i])
